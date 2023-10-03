import zipfile
from pathlib import Path
import logging


def tratativa1(zipname):
    print('===')
    try:
        with zipfile.ZipFile(zipname) as archive:
            archive.printdir()
    except zipfile.BadZipFile as error:
        logging.error(error)


def run():
    zipnames = (
        Path(__file__).resolve().parent / 'sample.zip',
        Path(__file__).resolve().parent / 'realpython02.py',
    )
    for file in zipnames:
        tratativa1(file)


if __name__ == '__main__':
    run()
