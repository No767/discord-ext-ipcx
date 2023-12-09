import asyncio
import logging
from typing import Any, Optional

import aiohttp

from .errors import NotConnectedError

log = logging.getLogger(__name__)


class Client:
    """
    Handles webserver side requests to the bot process.

    Parameters
    ----------
    host: str
        The IP or host of the IPC server, defaults to localhost
    Optional[port]: int
        The port of the IPC server. If not supplied the port will be found automatically, defaults to None
    multicast_port: Optional[int]
        The mutlicast post of the IPC server. If not supplied, the port used will be 20000.
    secret_key: Union[str, bytes]
        The secret key for your IPC server. Must match the server secret_key or requests will not go ahead, defaults to None
    """

    def __init__(
        self,
        host: str = "localhost",
        port: Optional[int] = None,
        multicast_port: int = 20000,
        secret_key: Optional[str] = None,
    ):
        self.secret_key = secret_key

        self.host = host
        self.port = port
        self.multicast_port = multicast_port

        self.session = None

    @property
    def url(self):
        return "ws://{0.host}:{1}".format(
            self, self.port if self.port else self.multicast_port
        )

    async def close(self) -> None:
        """Properly closes the :class:`aiohttp.ClientSession` session used for connections

        .. warning::

            This is required in order to clean up any remaining connections held in :class:`aiohttp.ClientSession`.
            Without doing so, your webserver will complain about having an unclosed client session, which is the result
            of not closing it manually.
        """
        if self.session:
            await self.session.close()

    async def _get_session(self) -> aiohttp.ClientSession:
        if not self.session:
            self.session = aiohttp.ClientSession()
        return self.session

    async def get_port(self) -> int:
        """Attempts to obtain the provided port.

        If not found, then an connection to the multicast server is made to attempt to obtain the port.

        Returns
        -------
        int
            The port number
        """
        if not self.port:
            log.debug(
                "No port was provided - initiating multicast connection at %s.",
                self.url,
            )
            session = await self._get_session()
            async with session.ws_connect(self.url, autoping=False) as multicast:
                payload = {
                    "connect": True,
                    "headers": {"Authorization": self.secret_key},
                }

                await multicast.send_json(payload)
                recv = await multicast.receive()

                log.debug("Multicast Server > %r", recv)

                if recv.type in (aiohttp.WSMsgType.CLOSE, aiohttp.WSMsgType.CLOSED):
                    log.error(
                        "WebSocket connection unexpectedly closed. Multicast Server is unreachable."
                    )
                    raise NotConnectedError("Multicast server connection failed.")

                port_data = recv.json()
                self.port = port_data["port"]

        return self.port

    async def request(self, endpoint: str, **kwargs) -> Any:
        """Make a request to the IPC server process.

        Parameters
        ----------
        endpoint: str
            The endpoint to request on the server
        **kwargs
            The data to send to the endpoint
        """
        log.info("Requesting IPC Server for %r with %r", endpoint, kwargs)
        if not self.port:
            self.port = await self.get_port()

        session = await self._get_session()
        async with session.ws_connect(
            self.url, autoping=False, autoclose=False
        ) as websocket:

            payload = {
                "endpoint": endpoint,
                "data": kwargs,
                "headers": {"Authorization": self.secret_key},
            }

            await websocket.send_json(payload)

            recv = await websocket.receive()

            log.debug("Client < %r", recv)

            if recv.type == aiohttp.WSMsgType.PING:
                log.info("Received request to PING")
                await websocket.ping()

                return await self.request(endpoint, **kwargs)

            if recv.type == aiohttp.WSMsgType.PONG:
                log.info("Received PONG")
                return await self.request(endpoint, **kwargs)

            if recv.type == aiohttp.WSMsgType.CLOSED:
                log.error(
                    "WebSocket connection unexpectedly closed. IPC Server is unreachable. Attempting reconnection in 5 seconds."
                )

                await asyncio.sleep(5)

                return await self.request(endpoint, **kwargs)

            return recv.json()
