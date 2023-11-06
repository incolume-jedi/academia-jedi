# !/usr/bin/env python
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
    ...


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
