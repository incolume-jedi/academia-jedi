"""Module."""

import random
import secrets
import sqlite3
import string

import pandas as pd

conn: sqlite3.Connection = sqlite3.connect('web-sqlite.db')
cursor: sqlite3.Cursor = conn.cursor()


def data_frame_fake(
    limit_max: int = 100,
    limit_min: int = 10,
    columns: int = 4,
) -> pd.DataFrame:
    """Gera um dataframe fake."""
    limit_min = max(10, limit_min)
    data = [
        [max(secrets.randbelow(350), limit_min) for _ in range(columns)]
        for _ in range(limit_max)
    ]
    df0 = pd.DataFrame(
        columns=list(string.ascii_uppercase[:columns]),
        data=data,
    )
    df0['TIMESTAMP'] = pd.date_range(
        start='1/1/2025',
        freq='14h',
        periods=limit_max,
    )
    df0['SITUACAO'] = [secrets.choice([1, 2]) for _ in range(limit_max)]
    df0['RATIO'] = [random.uniform(1, 2) for _ in range(limit_max)]
    return df0


def dataframe2sql(
    tablename: str,
    dataframe: pd.DataFrame | None = None,
    connection: sqlite3.Connection | None = None,
) -> bool:
    """Dataframe to SQL."""
    connection = connection or conn
    dataframe = dataframe or data_frame_fake()
    return dataframe.to_sql(name=tablename, con=connection, if_exists='append')


def comand_sql() -> bool:
    """Comandos SQL."""
