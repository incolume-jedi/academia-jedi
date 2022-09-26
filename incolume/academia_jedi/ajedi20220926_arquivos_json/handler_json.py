# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import inspect
import json
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol \
    .generator_pessoas import massa_pessoas

logFormat = '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;' \
            ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logFormat)


def json_0():
    logging.debug(f"ran ..")
    pessoas = massa_pessoas(is_json=True)
    with open("pessoas.json", "w") as file:
        json.dump(pessoas, file, indent=4)


def run():
    json_0()


if __name__ == '__main__':    # pragma: no cover
    run()
