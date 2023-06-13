"""Module for start FastApi-application."""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio.client import Redis
import asyncpg

from src.core.config import settings

description = """
### API for redirecting to long links.<br>
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_connection = await Redis(host=settings.redis_host, port=settings.redis_port)
    pg_connection = await asyncpg.connect(settings.pg_dsn)
    print(pg_connection)
    spam = await pg_connection.execute('CREATE SCHEMA IF NOT EXISTS us_schema;')
    print(spam)
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
