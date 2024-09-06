from psycopg import Connection, Cursor
from typing import Tuple
from .settings import Settings
from .database import create_connection_and_cursor

config = Settings()


app_db: Tuple[Connection, Cursor] = create_connection_and_cursor(config)
