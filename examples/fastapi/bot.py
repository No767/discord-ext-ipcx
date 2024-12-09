import logging

import discord
from discord.ext import commands, ipcx


class MyBot(commands.Bot):
    def __init__(self, intents: discord.Intents, *args, **kwargs):
        super().__init__(command_prefix="!", intents=intents, *args, **kwargs)
        self.ipc = ipcx.Server(self, secret_key="my_secret_key")  # nosec
        self.log = logging.getLogger("discord.ext.ipcx")

    async def setup_hook(self):
        """One time setup hook"""
        await self.ipc.start()

    async def on_ipc_ready(self):
        """Called when the IPC server is starting up"""
        self.log.info("Starting IPC Server")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        self.log.error("Error in %s: %s", endpoint, error)


intents = discord.Intents.default()
intents.message_content = True

TOKEN = "INSERT YOUR TOKEN HERE"  # nosec
bot = MyBot(intents=intents)


# This route returns the member count of the guild with the ID provided
@bot.ipc.route()
async def get_member_count(data):
    guild = bot.get_guild(data.guild_id)

    if guild is None:
        return 0
    return guild.member_count


if __name__ == "__main__":
    bot.run(TOKEN)
