"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import (
    base_dir,
    filezip_sample,
)

zipnames = (
    filezip_sample,
    base_dir / 'bad_sample.zip',
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
