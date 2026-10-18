from __future__ import annotations

from typing import TYPE_CHECKING

from discord.ext import commands, ipcx

if TYPE_CHECKING:
    from discord.ext.ipcx.server import IpcServerResponse


class IPCRoutes(commands.Cog):
    """Cog for managing IPC routes."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @ipcx.route()
    async def get_member_count(self, data: IpcServerResponse) -> int:
        guild = self.bot.get_guild(data.guild_id)

        if guild is None:
            return 0
        return guild.member_count


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(IPCRoutes(bot))
