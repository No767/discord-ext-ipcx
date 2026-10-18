# Copyright (c) 2020-present Ext-Creators, No767
# SPDX-License-Identifier: Apache-2.0

from discord.errors import DiscordException


class IPCError(DiscordException):
    """Base IPC exception class."""


class NoEndpointFoundError(IPCError):
    """Raised upon requesting an invalid endpoint."""


class ServerConnectionRefusedError(IPCError):
    """Raised upon a server refusing to connect / not being found."""


class JSONEncodeError(IPCError):
    """Raise upon un-serializable objects are given to the IPC."""


class NotConnectedError(IPCError):
    """Raised upon websocket not connected."""
