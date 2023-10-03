import zipfile
from pathlib import Path
import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

directory = Path(__file__).parent


def run():
    logging.debug(directory.parts)

    with zipfile.ZipFile(directory / 'sample.zip', mode='r') as archive:
        with archive.open('hello.txt', mode='r') as hello:
            for line in hello:
                print(line)


if __name__ == '__main__':
    run()
