import sqlite3
from inspect import stack
from pathlib import Path
from typing import Any

import pandas as pd
from faker import Faker
from sqlalchemy import create_engine

Faker(seed=13)
fake = Faker()


def massa_test():
    """Gera a massa de dados para testar ação da engine."""
    result = []
    for i in range(1, 101):
        name = f'{fake.first_name()} {fake.last_name()}'
        result.append(
            {
                'nome': name,
                'email': f'{name.casefold().replace(" ", "_")}@example.org',
                'id': f'{i:03}',
            },
        )
    return result


def example01():
    """Pandas + SQLite + SQLAlchemy rodando em RAM."""
    engine = create_engine(
        'sqlite+pysqlite:///:memory:',
        echo=True,
        future=True,
    )

    df = pd.DataFrame(massa_test())
    print(df.head())

    df.to_sql('users', engine, if_exists='replace', index=False)


def example02():
    """Pandas + SQLite + SQLAlchemy."""
    file_db = Path(__file__).parent.joinpath('db', f'{stack()[0][3]}.sqlite')
    file_db.parent.mkdir(exist_ok=True, parents=True)
    engine = create_engine(
        f'sqlite+pysqlite:///{file_db.as_posix()}',
        echo=True,
        future=True,
    )

    df = pd.DataFrame(massa_test())
    df.to_sql('users', engine, if_exists='replace', index=False)


def example03():
    """Pandas + SQLite."""
    file_db = Path(__file__).parent.joinpath('db', f'{stack()[0][3]}.sqlite')
    con = sqlite3.connect(file_db.as_posix())
    df = pd.DataFrame(massa_test())
    df.to_sql('users', con, index=False, if_exists='replace')


def sql2df(database: str, engine: Any):
    """ """
    return pd.read_sql(f'select * from {database}', engine)


def example04():
    """ """

    files = Path('db').glob('*')
    for db in files:
        print(sql2df('users', sqlite3.connect(db)).head())


def run():
    """Run code."""
    example01()
    example02()
    example03()
    example04()


if __name__ == '__main__':
    run()
