from __future__ import annotations

import asyncio
import logging
import sys
from typing import TYPE_CHECKING, Any, Optional

import aiohttp

from .errors import NotConnectedError

if TYPE_CHECKING:
    from types import TracebackType

if sys.version_info >= (3, 13):
    from typing import Self, TypeVar
else:
    from typing_extensions import Self, TypeVar


_T = TypeVar("_T", default=Any)

_log = logging.getLogger(__name__)


class Client:
    """
    Handles webserver side requests to the bot process.

    Operations with ``async with`` will automatically initialize the client and automatically cleans up.

    Parameters
    ----------
    host: str
        The IP or host of the IPC server, defaults to localhost
    port: Optional[int]
        The port of the IPC server. If not supplied the port will be found automatically, defaults to None
    multicast_port: Optional[int]
        The multicast post of the IPC server. If not supplied, the port used will be 20000.
    secret_key: Optional[str]
        The secret key for your IPC server. Must match the server secret_key or requests will not go ahead, defaults to None
    """

    def __init__(
        self,
        host: str = "localhost",
        port: Optional[int] = None,
        multicast_port: int = 20000,
        secret_key: Optional[str] = None,
    ) -> None:
        self.secret_key = secret_key

        self.host = host
        self.port = port
        self.multicast_port = multicast_port

        self.session: Optional[aiohttp.ClientSession] = None

    @property
    def url(self) -> str:
        return f"ws://{self.host}:{self.port or self.multicast_port}"

    async def __aenter__(self) -> Self:
        self._get_session()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()

    def _get_session(self) -> aiohttp.ClientSession:
        if not self.session:
            self.session = aiohttp.ClientSession()
        return self.session

    async def _get_port(self) -> int:
        if not self.port:
            _log.debug(
                "No port was provided - initiating multicast connection at %s.",
                self.url,
            )
            session = self._get_session()
            async with session.ws_connect(self.url, autoping=False) as multicast:
                payload = {
                    "connect": True,
                    "headers": {"Authorization": self.secret_key},
                }

                await multicast.send_json(payload)
                recv = await multicast.receive()

                _log.debug("Multicast Server > %r", recv)

                if recv.type in (
                    aiohttp.WSMsgType.CLOSE,
                    aiohttp.WSMsgType.CLOSED,
                ):
                    _log.error(
                        "WebSocket connection unexpectedly closed. Multicast Server is unreachable."
                    )
                    msg = "Multicast server connection failed."
                    raise NotConnectedError(msg)

                port_data = recv.json()
                self.port = port_data["port"]

        return self.port

    async def close(self) -> None:
        """Properly closes the :class:`aiohttp.ClientSession` session used for connections

        .. warning::

            This is required in order to clean up any remaining connections held in :class:`aiohttp.ClientSession`.
            Without doing so, your webserver will complain about having an unclosed client session, which is the result
            of not closing it manually.
        """
        if self.session:
            await self.session.close()

    async def request(self, endpoint: str, **kwargs: Any) -> _T:  # noqa: ANN401
        """Make a request to the IPC server process.

        Parameters
        ----------
        endpoint: str
            The endpoint to request on the server
        **kwargs
            The data to send to the endpoint
        """
        _log.info("Requesting IPC Server for %r with %r", endpoint, kwargs)
        if not self.port:
            self.port = await self._get_port()

        session = self._get_session()
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

            _log.debug("Client < %r", recv)

            if recv.type == aiohttp.WSMsgType.PING:
                _log.info("Received request to PING")
                await websocket.ping()

                return await self.request(endpoint, **kwargs)

            if recv.type == aiohttp.WSMsgType.PONG:
                _log.info("Received PONG")
                return await self.request(endpoint, **kwargs)

            if recv.type == aiohttp.WSMsgType.CLOSED:
                _log.error(
                    "WebSocket connection unexpectedly closed. IPC Server is unreachable. Attempting reconnection in 5 seconds."
                )

                await asyncio.sleep(5)

                return await self.request(endpoint, **kwargs)

            return recv.json()
