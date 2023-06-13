"""The module contains various database utilities."""

from asyncpg.connection import Connection

from src.core.config import settings

async def prepare_pg_db(pg_connection: Connection):
    """Function for prepare postgres database on startup."""

    await pg_connection.execute(f'CREATE SCHEMA IF NOT EXISTS {settings.pg_schema};')
    # await pg_connection.execute(f'''
    #                                 CREATE TABLE IF NOT EXISTS {settings.pg_schema}.{settings.pg_table}
    #                                 id
    #
    #
    # ''')
