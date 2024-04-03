"""Module for create Database."""

import sqlite3
from pathlib import Path
from typing import NoReturn

file_db = Path(__file__).parent / 'db' / 'dbone.db'
assert file_db.is_file(), f'Ops: {file_db}'


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
