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
        self.loop = asyncio.get_event_loop()

        self.secret_key = secret_key

        self.host = host
        self.port = port

        self.websocket = None
        self.multicast = None

        self.multicast_port = multicast_port

    @property
    def url(self):
        return "ws://{0.host}:{1}".format(
            self, self.port if self.port else self.multicast_port
        )

    async def init_sock(self) -> aiohttp.ClientWebSocketResponse:
        """Attempts to connect to the server

        Returns
        -------
        :class:`aiohttp.ClientWebSocketResponse`
            The websocket connection to the server
        """
        log.debug("Initiating WebSocket connection.")

        # This is done to prevent the "Unhandled closing" issues that happen with aiohttp
        # This is also what jsk does as well, as more than likely in a quart app, they aren't managing the lifecycle of the app
        async with aiohttp.ClientSession() as session:
            if not self.port:
                log.debug(
                    "No port was provided - initiating multicast connection at %s.",
                    self.url,
                )
                self.multicast = await session.ws_connect(self.url, autoping=False)

                payload = {
                    "connect": True,
                    "headers": {"Authorization": self.secret_key},
                }

                await self.multicast.send_json(payload)
                recv = await self.multicast.receive()

                log.debug("Multicast Server > %r", recv)

                if recv.type in (aiohttp.WSMsgType.CLOSE, aiohttp.WSMsgType.CLOSED):
                    log.error(
                        "WebSocket connection unexpectedly closed. Multicast Server is unreachable."
                    )
                    raise NotConnectedError("Multicast server connection failed.")

                port_data = recv.json()
                self.port = port_data["port"]

            websocket = await session.ws_connect(
                self.url, autoping=False, autoclose=False
            )
            log.info("Client connected to %s", self.url)

            return websocket

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
        if not self.websocket:
            self.websocket = await self.init_sock()

        payload = {
            "endpoint": endpoint,
            "data": kwargs,
            "headers": {"Authorization": self.secret_key},
        }

        await self.websocket.send_json(payload)

        recv = await self.websocket.receive()

        log.debug("Client < %r", recv)

        if recv.type == aiohttp.WSMsgType.PING:
            log.info("Received request to PING")
            await self.websocket.ping()

            return await self.request(endpoint, **kwargs)

        if recv.type == aiohttp.WSMsgType.PONG:
            log.info("Received PONG")
            return await self.request(endpoint, **kwargs)

        if recv.type == aiohttp.WSMsgType.CLOSED:
            log.error(
                "WebSocket connection unexpectedly closed. IPC Server is unreachable. Attempting reconnection in 5 seconds."
            )

            await asyncio.sleep(5)

            await self.init_sock()

            return await self.request(endpoint, **kwargs)

        return recv.json()
