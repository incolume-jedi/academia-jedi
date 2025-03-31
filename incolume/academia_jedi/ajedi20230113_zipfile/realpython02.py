"""Exemplo realpython."""

import logging
import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample

# ruff:noqa: T201

zipnames = (
    filezip_sample,
    Path(__file__).resolve().parent / 'realpython02.py',
)


def tratativa1(zipname):
    """Tratativa de exceções no acesso ao zip."""
    print('===')
    try:
        with zipfile.ZipFile(zipname) as archive:
            archive.printdir()
    except zipfile.BadZipFile:
        logging.exception('Falha no arquivo zip')
        raise
    except FileNotFoundError as e:
        logging.exception(e.strerror)
        raise


def run():
    """Run it."""
    for file in zipnames:
        tratativa1(file)


if __name__ == '__main__':
    run()
