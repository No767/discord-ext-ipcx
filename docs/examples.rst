Examples
^^^^^^^^

Here are some ways you can use this library in your own bot. Make sure to adjust it to your own bot's needs. 
For GitHub based examples, please see the `examples directory <https://github.com/No767/discord-ext-ipcx/tree/main/examples>`_

Basic IPC
---------

``bot.py``

.. code-block:: python
    
    import logging

    import discord
    from discord.ext import commands, ipcx


    class MyBot(commands.Bot):
        def __init__(self, intents: discord.Intents, *args, **kwargs):
            super().__init__(command_prefix="!", intents=intents, *args, **kwargs)
            self.ipc = ipcx.Server(
                self, secret_key="my_secret_key"  # nosec
            )
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


``webserver.py``

.. code-block:: python

    from quart import Quart

    from discord.ext import ipcx

    app = Quart(__name__)
    ipc_client = ipcx.Client(
        secret_key="my_secret_key"  # nosec # secret_key must be the same as your server
    )


    @app.route("/")
    async def index():
        member_count = await ipc_client.request(
            "get_member_count", guild_id=12345678
        )  # get the member count of server with ID 12345678

        return str(member_count)  # display member count

    @app.after_serving
    async def close_session():
        await ipc_client.close()

    if __name__ == "__main__":
        app.run()


Cog-based IPC
-------------

``cogs/__init__.py`` (This is to automatically load the cogs)

.. code-block:: python

    from pkgutil import iter_modules

    EXTENSIONS = [module.name for module in iter_modules(__path__, f"{__package__}.")]

``cogs/ipc.py``

.. code-block:: python

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


``bot.py``

.. code-block:: python

    import logging

    from cogs import EXTENSIONS

    import discord
    from discord.ext import commands, ipcx


    class MyBot(commands.Bot):
        def __init__(self, intents: discord.Intents, *args, **kwargs):
            super().__init__(command_prefix="!", intents=intents, *args, **kwargs)
            self.ipc = ipcx.Server(
                self, secret_key="my_secret_key"  # nosec
            )
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

    TOKEN = "INSERT YOUR TOKEN HERE"  # nosec
    bot = MyBot(intents=intents)

    if __name__ == "__main__":
        bot.run(TOKEN)


``webserver.py``

.. code-block:: python

    from quart import Quart

    from discord.ext import ipcx

    app = Quart(__name__)
    ipc_client = ipcx.Client(
        secret_key="my_secret_key"  # nosec # secret_key must be the same as your server
    )


    @app.route("/")
    async def index():
        member_count = await ipc_client.request(
            "get_member_count", guild_id=12345678
        )  # get the member count of server with ID 12345678

        return str(member_count)  # display member count

    @app.after_serving
    async def close_session():
        await ipc_client.close()

    if __name__ == "__main__":
        app.run()