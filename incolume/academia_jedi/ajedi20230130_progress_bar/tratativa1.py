import logging
from time import sleep

from tqdm import tqdm

from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.generator_pessoas import (
    massa_pessoas,
)

__author__ = '@britodfbr'  # pragma: no cover


def tratativa1():
    """Sem progress bar."""
    for pessoa in massa_pessoas():
        logging.debug(pessoa)


def tratativa2():
    """Com progress bar."""
    for pessoa in tqdm(massa_pessoas()):
        sleep(0.3)
        logging.debug(pessoa)


def run():
    tratativa1()
    tratativa2()


if __name__ == '__main__':  # pragma: no cover
    run()
