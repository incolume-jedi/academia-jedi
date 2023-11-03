"""Database module."""
import logging
import sqlite3
from os import getenv
from pathlib import Path

__author__ = '@britodfbr'  # pragma: no cover


def get_connection(filesqlite: Path | None = None) -> sqlite3.Connection:
    """Connetion database."""
    if not filesqlite:
        filesqlite = (
            Path(getenv('APP_INCOLUME_DB'))
            if getenv('APP_INCOLUME_DB')
            else None
        )
    if not filesqlite:
        filesqlite = Path(__file__).parent / 'db/cad.db'

    logging.debug(filesqlite.as_posix())
    return sqlite3.connect(filesqlite, check_same_thread=False)


def create_table() -> bool:
    """Create table."""
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        contact TEXT,
        age INTEGER,
        gender TEXT,
        email TEXT,
        address TEXT
        )""",
    )
    conn.commit()
    return True
