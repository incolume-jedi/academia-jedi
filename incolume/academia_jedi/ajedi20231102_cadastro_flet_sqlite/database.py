"""Database module."""

from __future__ import annotations

import logging
import sqlite3
from os import getenv
from pathlib import Path

from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover


def get_connection(filesqlite: Path | None = None) -> sqlite3.Connection:
    """Connetion database."""
    if not filesqlite and getenv('APP_INCOLUME_DB'):
        filesqlite = Path(getenv('APP_INCOLUME_DB'))
    if not filesqlite:
        filesqlite = Path(__file__).parent.joinpath('db', 'cad.db')

    filesqlite.parent.mkdir(exist_ok=True, parents=True)

    logging.debug(ic(filesqlite.as_posix()))
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
    logging.info(ic('Tabela `user` criada com sucesso.'))
    return True
