# !/usr/bin/env python

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import inspect
import logging
from pathlib import Path

import pandas as pd
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.generator_pessoas import (
    massa_pessoas,
)

logFormat = (
    '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;'
    ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
)
logging.basicConfig(level=logging.DEBUG, format=logFormat)
__author__ = '@britodfbr'  # pragma: no cover


def get_df():
    df = pd.DataFrame(massa_pessoas())
    logging.debug(df.shape)
    print(df.info())
    return df


def pd_0_write_csv():
    logging.debug('ran..')
    df = get_df()
    df.to_csv('pessoas.csv', index=False)


def pd_1_write_json():
    logging.debug('ran..')
    df = get_df()
    df.to_json('pessoas.json', indent=4)


def pd_2_read_all():
    logging.debug('ran..')
    df1 = pd.read_csv('pessoas.csv')
    print(df1.head())

    df2 = pd.read_json('pessoas.json')
    print(df2.info())
    print(df2.head())


def pd_3_write_json():
    logging.debug('ran..')
    df = get_df()
    print(df.head())
    print(df.info())

    df.to_json(
        f'{Path(inspect.stack()[0][1]).stem}.json',
        indent=4,
        orient='records',
    )


def pd_4_read_all():
    logging.debug('ran..')
    df1 = pd.read_csv('pessoas.csv')
    print(df1.head())

    df2 = pd.read_json('pessoas.json')
    print(df2.head())
    # Converter ms@json para datetime
    df2.data_de_nascimento = pd.to_datetime(df2.data_de_nascimento, unit='ms')
    print(df2.head())
    print(df2.info())


def run():
    pd_4_read_all()


if __name__ == '__main__':  # pragma: no cover
    run()
