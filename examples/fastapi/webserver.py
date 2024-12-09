from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI

from discord.ext import ipcx

if TYPE_CHECKING:
    from typing_extensions import Self


class MyApp(FastAPI):
    client: ipcx.Client

    def __init__(self, *args, **kwargs):
        super().__init__(lifespan=self.lifespan, *args, **kwargs)

    @asynccontextmanager
    async def lifespan(self, app: Self):
        async with ipcx.Client(secret_key="my_secret_key") as app.client:  # nosec # secret_key must be the same as your server
            yield


app = MyApp()


@app.get("/")
async def index():
    member_count = await app.client.request(
        "get_member_count", guild_id=12345678
    )  # get the member count of server with ID 12345678

    return str(member_count)  # display member count


if __name__ == "__main__":
    uvicorn.run(app)
