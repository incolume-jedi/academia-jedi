import dbm

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import logging
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import dotenv
from incolume.academia_jedi.ajedi20230211_massa_dados_faker_protocol.generator_pessoas import (
    massa_pessoas,
)

__author__ = '@britodfbr'  # pragma: no cover

config = dotenv.load_dotenv(dotenv.find_dotenv())
logging.debug(config)

fileoutput = Path(__file__).parent / 'databases' / os.getenv('BASENAME')
fileoutput.parent.mkdir(exist_ok=True, parents=True)
logging.debug(fileoutput)

file = fileoutput.with_name(f'{fileoutput.stem}_people.dbm')
logging.debug(file)


def ex01():
    """Dados em cache dbm."""
    logging.debug('..')

    # Open database, creating it if necessary.
    """
    Value|Meaning
    'r'| Open existing database for reading only (default)
    'w'| Open existing database for reading and writing
    'c'| Open database for reading and writing, creating it if it doesn’t exist
    'n'| Always create a new, empty database, open for reading and writing
    """
    with dbm.open(NamedTemporaryFile().name, 'c') as db:
        # Record some values
        db[b'hello'] = b'there'
        db['www.python.org'] = 'Python Website'
        db['www.cnn.com'] = 'Cable News Network'

        # Note that the keys are considered bytes now.
        assert db[b'www.python.org'] == b'Python Website'

        # Notice how the value is now in bytes.
        assert db['www.cnn.com'] == b'Cable News Network'

        # Often-used methods of the dict interface work too.
        print(db.get('python.org', 'not present'))
    # db is automatically closed when leaving the with statement.


def ex02():
    """# Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    """
    try:
        with dbm.open(NamedTemporaryFile().name, 'c') as db:
            db['www.yahoo.com'] = 4
    except TypeError as e:
        logging.exception(e)


def ex03():
    """"""
    with dbm.open(file.as_posix(), 'c') as records:
        records['0'] = 'zero'
        records['1'] = 'um'
        records['2'] = 'dois'
        records['3'] = 'três'
        records['4'] = 'quatro'

    # with dbm.open(file.as_posix(), 'r') as db:


def ex04():
    """"""
    filename = NamedTemporaryFile().name
    with dbm.open(filename, 'n') as db:
        logging.debug(filename)
        # inserting the new key and
        # values in the database.
        db['name'] = 'GeeksforGeeks'
        db['phone'] = '8888'
        db['Short name'] = 'GfG'
        db['Date'] = '01/01/2000'

        # the value through get method.
        print(db.get('name'))
        print()

        # printing the values of
        # database through values()
        # method (iterator).
        for value in db.values():
            print(value)
        print()

        # printing the values through
        # key iterator.
        for key in db:
            print(db.get(key))
        print()

        # popping out the key, value
        # pair corresponding to
        # 'phone' key.
        db.pop('phone')

        # printing the key, value
        # pairs present in database.
        for key, value in db.items():
            print(key, value)

        # clearing all the key values
        # in database.
        db.clear()

        # Below loop will print nothing
        # as database is cleared above.
        for key, value in db.items():
            print(key, value)

        # closing the database.
        db.close()


def ex05():
    """"""
    logging.debug('..')
    with dbm.dumb.open():
        ...


def ex0x():
    """Gravar dados em arquivo dbm."""
    logging.debug('..')

    people = massa_pessoas(quantidade=3)

    print(people)

    with dbm.open(file.as_posix(), 'c') as f:
        logging.debug(type(f))
        for idx, person in enumerate(people):
            i = bytes(idx)
            f[i] = person

    # with dbm.open() as f:


def run():
    logging.debug('running..')
    ex01()
    ex02()
    ex03()
    ex04()


if __name__ == '__main__':  # pragma: no cover
    run()
