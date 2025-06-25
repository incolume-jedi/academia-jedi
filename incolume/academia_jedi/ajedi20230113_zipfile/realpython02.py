"""Exemplo realpython."""

import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample, logger

# ruff: noqa: TRY301

zipnames = (
    filezip_sample,
    Path(__file__).parent / 'realpython02.py',
)


def tratativa1(zipname: Path | str) -> None:
    """Tratativa de exceções no acesso ao zip."""
    print('===')

    try:
        if zipname in [None, '']:
            msg = 'No such file or directory'
            raise FileNotFoundError(msg)

        with zipfile.ZipFile(zipname) as archive:
            archive.printdir()
    except zipfile.BadZipFile:
        logger.exception('Falha no arquivo zip')
        raise
    except FileNotFoundError as e:
        logger.exception(e.strerror)
        raise


def run():
    """Run it."""
    for file in zipnames:
        tratativa1(file)


if __name__ == '__main__':
    run()
