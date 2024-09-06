import psycopg

def create_connection_and_cursor(config):
    """Create and return a new connection and cursor."""
    try:
        conn = psycopg.connect(
            dbname=config.db_name,
            user=config.db_user,
            password=config.db_password,
            host=config.db_host,
            port=5432  # or any other port if needed
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg.Error as e:
        print(f"Unable to connect to the database: {e}")
        raise
