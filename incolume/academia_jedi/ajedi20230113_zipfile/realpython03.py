"""Module."""

import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample

# ruff:noqa: T201

zipnames = (
    filezip_sample,
    Path(__file__).resolve().parent / 'bad_sample.zip',
)


def tratativa2(filename):
    """Tratativa de exceções no acesso ao zip."""
    print('===')
    if zipfile.is_zipfile(filename):
        with zipfile.ZipFile(filename, 'r') as archive:
            archive.printdir()
    else:
        print('File is not a zip file')


def run():
    """Run it."""
    for file in zipnames:
        tratativa2(file)


if __name__ == '__main__':
    run()
