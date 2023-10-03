# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import inspect
import json
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


def json_0_write_pessoas():
    logging.debug(f'ran ..')
    pessoas = massa_pessoas(is_json=True)
    with open('pessoas.json', 'w') as file:
        json.dump(pessoas, file, indent=4)


def json_1_read_pessoas():
    """Ler arquivo JSON e trazer valores como dict"""
    logging.debug(f'ran ..')
    with open('pessoas.json') as file:
        pessoas = [json.loads(pessoa) for pessoa in json.load(file)]

    for pessoa in pessoas:
        logging.debug(pessoa)


def json_2_read_pessoas():
    """Ler arquivo JSON e trazer valores como instancia de Pessoa"""
    logging.debug(f'ran ..')
    with open('pessoas.json') as file:
        pessoas = [Pessoa(**json.loads(pessoa)) for pessoa in json.load(file)]

    for pessoa in pessoas:
        logging.debug(pessoa)


def run():
    json_0_write_pessoas()
    json_1_read_pessoas()
    json_2_read_pessoas()


if __name__ == '__main__':  # pragma: no cover
    run()
