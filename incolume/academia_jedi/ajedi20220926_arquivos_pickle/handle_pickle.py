# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover
import logging
import pickle
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol \
    .generator_pessoas import massa_pessoas
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.models import \
    Pessoa

logFormat = '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;' \
            ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logFormat)


def pickle_0_write_one():
    logging.debug('ran..')
    pessoas = massa_pessoas()
    p1 = pessoas[0]
    logging.debug(p1)
    logging.debug(f"{isinstance(p1, Pessoa)=}")
    with open("pessoa.pkl", "wb") as file:
        pickle.dump(p1, file)
        logging.debug(f"{file.name} writed")


def pickle_1_read():
    logging.debug('ran..')
    with open("pessoa.pkl", 'rb') as file:
        p1 = pickle.load(file)
        logging.debug(f"{file.name} readed")
    logging.debug(p1)
    logging.debug(f"{isinstance(p1, Pessoa)=}")


def run():
    pickle_0_write_one()
    pickle_1_read()


if __name__ == '__main__':    # pragma: no cover
    run()
