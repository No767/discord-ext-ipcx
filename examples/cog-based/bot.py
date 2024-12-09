import logging

from cogs import EXTENSIONS

import discord
from discord.ext import commands, ipcx

TOKEN = ""
SECRET_KEY = ""  # This key must be the exact same on the webserver


class MyBot(commands.Bot):
    def __init__(self, intents: discord.Intents, *args, **kwargs):
        super().__init__(command_prefix="!", intents=intents, *args, **kwargs)
        self.ipc = ipcx.Server(self, secret_key=SECRET_KEY)
        self.log = logging.getLogger("discord.ext.ipcx")

    async def setup_hook(self):
        """One time setup hook"""
        for extension in EXTENSIONS:
            await self.load_extension(extension)
        await self.ipc.start()

    async def on_ipc_ready(self):
        """Called when the IPC server is starting up"""
        self.log.info("Starting IPC Server")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        self.log.error("Error in %s: %s", endpoint, error)


intents = discord.Intents.default()
intents.message_content = True

bot = MyBot(intents=intents)

if __name__ == "__main__":
    bot.run(TOKEN)
