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

    with zipfile.ZipFile(directory / 'sample.zip', mode='a') as archive:
        with archive.open('new_hello.txt', 'w') as new_hello:
            new_hello.write(b'Hello, World!')

    with zipfile.ZipFile(directory / 'sample.zip', mode='r') as archive:
        archive.printdir()
        print('------')
        print(archive.read('new_hello.txt'))


if __name__ == '__main__':
    run()
