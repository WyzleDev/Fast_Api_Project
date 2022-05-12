from hypercorn.asyncio import serve
from hypercorn.config import Config
from api.api import app


async def run_api():
    await serve(app, Config())
