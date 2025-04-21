"""DB conection."""


import psycopg2
from dotenv import load_dotenv
from icecream import ic
from contextlib import contextmanager
import os


load_dotenv()

DATABASE = os.getenv('DB_DATABASE')
HOST = os.getenv('LOCALHOST')
USERSERVER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
PORT = os.getenv('DB_PORT')

@contextmanager
def instance_cursor():
    """Cursor."""
    conn = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        if conn:
            cursor.close()
            conn.close()
            ic('Conexão com PostgreSQL fechada.')
