"""Module for create Database."""

import logging
import sqlite3
import sys
from pathlib import Path
from typing import NoReturn

from icecream import ic

file_db = Path(__file__).parent / 'db' / 'dbone.db'

try:
    file_db.read_text()
except (FileExistsError, FileNotFoundError):
    logging.debug(ic(f'Ops: {file_db}'))
    sys.exit()


conn = sqlite3.connect(file_db.as_posix(), check_same_thread=False)

# THIS SCRIPT IS CREATE TABEL AUTOMATICALLY WHEN YOU RUN THE FLET APP


def create_table() -> NoReturn:
    """Create database."""
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    contact TEXT,
    age INTEGER,
    gender TEXT,
    email TEXT,
    address TEXT)""")
    conn.commit()
