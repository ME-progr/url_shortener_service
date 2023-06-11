"""Модуль, запускающий FastApi-приложение (`uvicorn` сервер)."""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.core.config import settings


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


if __name__ == '__main__':

    if settings.debug.lower() == 'true':
        uvicorn.run(
            'main:app',
            host='0.0.0.0',
            port=8000,
        )
