# !/usr/bin/env python

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
__author__ = '@britodfbr'  # pragma: no cover
import logging
import pickle

from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.generator_pessoas import (
    massa_pessoas,
)
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.models import (
    Pessoa,
)

logFormat = (
    '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;'
    ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
)
logging.basicConfig(level=logging.DEBUG, format=logFormat)


def pickle_0_write_one():
    logging.debug('ran..')
    pessoas = massa_pessoas()
    p1 = pessoas[0]
    logging.debug(p1)
    logging.debug(f'{isinstance(p1, Pessoa)=}')

    with open('pessoa.pkl', 'wb') as file:
        pickle.dump(p1, file)

        logging.debug(f'{file.name} writed')


def pickle_1_read():
    logging.debug('ran..')

    with open('pessoa.pkl', 'rb') as file:
        p1 = pickle.load(file)

        logging.debug(f'{file.name} readed')
    logging.debug(p1)
    logging.debug(f'{isinstance(p1, Pessoa)=}')


def pickle_2_write_all():
    logging.debug('ran..')
    pessoas = massa_pessoas()
    logging.debug(f'{len(pessoas)=}')

    with open('pessoas.pkl', 'wb') as file:
        pickle.dump(pessoas, file)

        logging.debug(f'{file.name} writed')


def pickle_3_read_all():
    logging.debug('ran..')

    with open('pessoas.pkl', 'rb') as file:
        pessoas = pickle.load(file)

    logging.debug(f'{type(pessoas)=}')
    logging.debug(f'{type(pessoas[0])=}')
    logging.debug(f'{len(pessoas)=}')
    for i, pessoa in enumerate(pessoas):
        logging.debug(f'{i}: {pessoa}')


def run():
    pickle_0_write_one()
    pickle_1_read()
    pickle_2_write_all()
    pickle_3_read_all()


if __name__ == '__main__':  # pragma: no cover
    run()
