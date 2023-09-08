from discord.ext import commands, ipcx


class IPCRoutes(commands.Cog):
    """Cog for managing IPC routes."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @ipcx.route()
    async def get_member_count(self, data):
        guild = self.bot.get_guild(data.guild_id)

        if guild is None:
            return 0
        return guild.member_count


async def setup(bot: commands.Bot):
    await bot.add_cog(IPCRoutes(bot))
