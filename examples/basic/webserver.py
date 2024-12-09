from quart import Quart

from discord.ext import ipcx

SECRET_KEY = "" # This key must be the exact same on the bot

app = Quart(__name__)
ipc_client = ipcx.Client(
    secret_key=SECRET_KEY
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
