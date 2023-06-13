"""Модуль, запускающий FastApi-приложение."""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio.client import Redis

from src.core.config import settings

description = """
### API для перенаправления на длинные ссылки.<br>
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_connection = await Redis(host=settings.redis_host, port=settings.redis_port)
    await redis_connection.set('test_key', '11111111111111')
    yield

    await redis_connection.close()

app = FastAPI(
    title=settings.project_name,
    description=description,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


if __name__ == '__main__':

    if settings.debug.lower() == 'true':
        uvicorn.run(
            'main:app',
            host='0.0.0.0',
            port=8000,
        )
