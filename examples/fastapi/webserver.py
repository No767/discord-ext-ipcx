from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI

from discord.ext import ipcx

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from typing_extensions import Self


SECRET_KEY = ""  # This key must be the exact same on the bot


class MyApp(FastAPI):
    client: ipcx.Client

    def __init__(self) -> None:
        super().__init__(lifespan=self.lifespan)

    @asynccontextmanager
    async def lifespan(self, app: Self) -> AsyncGenerator[None]:
        async with ipcx.Client(secret_key=SECRET_KEY) as app.client:
            yield


app = MyApp()


@app.get("/")
async def index() -> str:
    member_count = await app.client.request(
        "get_member_count", guild_id=12345678
    )  # get the member count of server with ID 12345678

    return str(member_count)  # display member count


if __name__ == "__main__":
    uvicorn.run(app)
