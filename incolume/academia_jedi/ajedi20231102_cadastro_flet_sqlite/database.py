"""Database module."""
import logging
import sqlite3
from os import getenv
from dotenv import load_dotenv
from pathlib import Path

__author__ = "@britodfbr"  # pragma: no cover

load_dotenv()


def get_connection(filesqlite: Path = None) -> sqlite3.Connection:
    """Connetion database."""
    file = (filesqlite or
            Path(getenv('APP_INCOLUME_DB')) or Path(__file__) / 'db/cad.db')
    logging.debug(f'{file.as_posix()=}')
    conn = sqlite3.connect(file, check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()
