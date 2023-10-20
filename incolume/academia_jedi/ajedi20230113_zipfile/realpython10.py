import logging
import zipfile
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

directory = Path(__file__).parent


def run():
    logging.debug(directory.parts)

    with zipfile.ZipFile(directory / 'hello.zip', mode='r') as archive:
        logging.debug(archive.namelist())
        for line in archive.read(
            Path(*directory.parts[1:]).joinpath('hello.txt').as_posix()
        ).split(b'\n'):
            print(line)


if __name__ == '__main__':
    run()
