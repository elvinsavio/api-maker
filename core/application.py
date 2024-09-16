import os
from psycopg.errors import UniqueViolation
from app import app_db
from models.response import Response

from libs.logs import logger
from libs.strings import sanitize_folder_name


def create_new_application(name: str, description: str, prefix: str) -> Response:
    conn, cur = app_db

    def rollback(error, name):
        logger.error("Failed to create application {name} -> {error}")
        conn.rollback()

    try:
        logger.info(f"Creating new application {name}")
        # db write
        query = "INSERT INTO apps (name, description, prefix) VALUES (%s, %s, %s);"
        cur.execute(query, (name, description, prefix))

        # folder
        folder_name = sanitize_folder_name(name)
        folder_path = os.path.abspath(f"./__application__/{folder_name}")
        os.makedirs(folder_path)

        conn.commit()
        return ("Ok", None)
    except UniqueViolation as e:
        rollback(error=e, name=name)
        return (None, "Key already exists")
    except Exception as e:
        rollback(error=e, name=name)
        return (None, str(e))
