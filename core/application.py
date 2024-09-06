from psycopg.errors import UniqueViolation
from app import app_db
from models.response import Response


def create_new_application(name: str, description: str, prefix: str) -> Response:
    conn, cur = app_db

    try:
        query = "INSERT INTO apps (name, description, prefix) VALUES (%s, %s, %s);"
        cur.execute(query, (name, description, prefix))
        conn.commit()
        return ("Ok", None)
    except UniqueViolation:
        return (None, "Key already exists")
    except Exception as e:
        return (None, e)
