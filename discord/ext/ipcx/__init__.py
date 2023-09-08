from typing import Literal, NamedTuple

# Thank you Umbra for pointing these out as public classes
# Idea comes from Soheab on the dpy server
from .server import Server as Server
from .server import route as route

__all__ = ["Server", "route"]


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "final"]

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.micro}-{self.releaselevel}"


version_info = VersionInfo(major=0, minor=1, micro=0, releaselevel="alpha")

# Since this class is always exported, we just want to delete it at the end
# So others can't use it
del VersionInfo
