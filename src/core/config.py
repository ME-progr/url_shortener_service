"""Модуль содержит настройки для работы FastApi-приложения."""

from os import path as os_path
from pathlib import Path

from pydantic import BaseSettings, Field

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG_ENV = os_path.join(BASE_DIR, 'core', '.env.debug')
PROD_ENV = os_path.join(BASE_DIR, 'core', '.env.prod')

project_env = DEBUG_ENV


class Settings(BaseSettings):
    project_name: str = Field(env='PROJECT_NAME')

    debug: str = Field(env='DEBUG')

    cache_lifetime: str = Field(env='CACHE_LIFETIME')
    redis_host: str = Field(env='REDIS_HOST')
    redis_port: int = Field(env='REDIS_PORT')

    pg_host: str = Field(env='POSTGRES_HOST')
    pg_port: int = Field(env='POSTGRES_PORT')

    class Config:
        env_file = project_env


settings = Settings()
