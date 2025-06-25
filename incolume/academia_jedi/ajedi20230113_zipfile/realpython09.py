"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample


def run():
    """Run it."""
    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        for filename in archive.namelist():
            print(filename)


if __name__ == '__main__':
    run()
