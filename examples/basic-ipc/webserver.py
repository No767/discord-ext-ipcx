from quart import Quart

from discord.ext import ipcx

app = Quart(__name__)
ipc_client = ipcx.Client(
    secret_key="my_secret_key"  # nosec
)  # secret_key must be the same as your server


@app.route("/")
async def index():
    member_count = await ipc_client.request(
        "get_member_count", guild_id=12345678
    )  # get the member count of server with ID 12345678

    return str(member_count)  # display member count


if __name__ == "__main__":
    app.run()
