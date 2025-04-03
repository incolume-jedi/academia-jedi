"""Modelo."""

# ruff: noqa: T201
import json
import logging

from incolume.academia_jedi.ajedi20230129_files import (
    config,
    dados_dict,
    dados_json,
    fileoutput,
)
from incolume.academia_jedi.ajedi20230211_massa_dados_faker_protocol.models import (  # noqa: E501
    Pessoa,
)

__author__ = '@britodfbr'  # pragma: no cover
logging.debug(config)
logging.debug(fileoutput)


def ex1():
    """Create JSON file."""
    logging.debug(dados_json)
    with fileoutput.with_suffix('.json').open('w') as file:
        json.dump(
            dados_dict,
            file,
            indent=2,
        )


def ex2():
    """Read JSON file."""
    with fileoutput.with_suffix('.json').open() as file:
        people = json.load(file)
        for person in people:
            logging.debug('%s: %s', person, type(person))
            print(person.get('nome_completo'))


def ex3():
    """Create JSON file."""
    logging.debug(dados_dict)
    with fileoutput.with_suffix('.json').open() as file:
        p = json.load(file)
        people = [Pessoa(**d) for d in p]
        print(people)
    for person in people:
        print(person.to_dict())


def run() -> None:
    """Run it."""
    ex1()
    ex2()
    ex3()


if __name__ == '__main__':  # pragma: no cover
    run()
