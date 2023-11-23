"""
Discord.py IPC Extension
~~~~~~~~~~~~~~~~~~~~~~~~

A upgraded version of discord-ext-ipc that now works with discord.py v2.

:copyright: (c) 2020-present Ext-Creators, No767
:license: Apache-2.0, see LICENSE for more details
"""

__title__ = "discord-ext-ipcx"
__author__ = "Ext-Creators, No767"
__license__ = "Apache-2.0"
__copyright__ = "(c) 2020-present Ext-Creators, No767"
__version__ = "0.1.1"

from typing import Literal, NamedTuple

# Thank you Umbra for pointing these out as public classes
# Idea comes from Soheab on the dpy server
from .client import Client as Client
from .server import Server as Server, route as route


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "final"]

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.micro}-{self.releaselevel}"


version_info = VersionInfo(major=0, minor=2, micro=0, releaselevel="final")

# Since this class is always exported, we just want to delete it at the end
# So others can't use it
del VersionInfo
