import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import os
import shelve
from pathlib import Path

import dotenv
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.generator_pessoas import (
    massa_pessoas,
)

__author__ = '@britodfbr'  # pragma: no cover

config = dotenv.load_dotenv(dotenv.find_dotenv())
logging.debug(config)

dados = massa_pessoas(is_json=False)
logging.debug(dados)

fileoutput = Path(__file__).parent / 'databases' / os.getenv('BASENAME')
fileoutput.parent.mkdir(exist_ok=True, parents=True)
logging.debug(fileoutput)


def ex01():
    """Gravar dados em shelve file."""
    with shelve.open(fileoutput.as_posix()) as db:
        db['a'] = 1
        db['b'] = 2
        db['c'] = 3
        db['d'] = 4
        logging.debug(dict(db.items()))


def ex02():
    """Ler dados em shelve file."""
    with shelve.open(fileoutput.as_posix()) as db:
        print(dict(db.items()), type(db), db.get('a'), sep='\n')
        logging.debug(db.items())


def ex03():
    """Atualizar dados em shelve file."""
    data: dict = {'f': 1, 'a': 5}
    with shelve.open(fileoutput.as_posix()) as db:
        db.update(data)
        logging.debug(dict(db.items()))


def ex04():
    """Objetos em shelve file."""
    file = fileoutput.with_name('Obj').as_posix()
    with shelve.open(file) as db:
        db['0'] = dados[0]
        logging.debug(dict(db.items()))

    with shelve.open(file) as db:
        print(dict(db.items()))


def ex05():
    """Objetos em shelve file."""
    file = fileoutput.with_name('Obj2').as_posix()
    with shelve.open(file) as db:
        for i, data in enumerate(dados):
            db[str(i)] = data
        logging.debug(dict(db.items()))

    with shelve.open(file) as db:
        print(dict(db.items()))


def ex06():
    """Recuperações de dados."""
    file = fileoutput.with_name('Obj2').as_posix()
    with shelve.open(file) as db:
        for person in db.items():
            print(person)

        print(db['99'])  # raise Erro se 99 não existir
        print(db.get('100'))  # None
        print(db.get('100', 'Ops'))  # Ops

        db.setdefault('2', 0)
        print(db.get('99'))


def run():
    logging.debug('running..')
    ex01()
    ex02()
    ex03()
    ex02()
    ex04()
    ex05()
    print('===' * 30)
    ex06()


if __name__ == '__main__':  # pragma: no cover
    run()
