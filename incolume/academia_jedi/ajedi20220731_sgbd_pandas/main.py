import sqlite3

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
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
