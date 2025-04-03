"""Module."""

import secrets
import sqlite3
import string
from pathlib import Path

import pandas as pd

conn: sqlite3.Connection = sqlite3.connect('web.db')


def data_frame_fake(limit: int = 100, columns: int = 4) -> pd.DataFrame:
    """Gera um dataframe fake."""
    limit = max(limit, 10)
    serie = pd.date_range(start='1/1/2025', periods=limit)
    data = [
        [secrets.randbelow(350) for _ in range(columns)] for _ in range(limit)
    ]
    return pd.DataFrame(
        index=serie, columns=list(string.ascii_uppercase[:columns]), data=data
    )


def dataframe2sql(
    dataframe: pd.DataFrame,
    fileoutput: Path,
    tablename: str,
    connection: sqlite3.Connection,
) -> bool:
    """Dataframe to SQL."""
    dataframe.to_sql(name=tablename, con=connection)
