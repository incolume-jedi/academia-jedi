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
    with zipfile.ZipFile(
        directory / 'sample_file_pwd.zip', mode='r'
    ) as archive:
        for line in archive.read('hello.txt', pwd=b'secret1').split(b'\n'):
            print(line)

    with zipfile.ZipFile(
        directory / 'sample_file_pwd1.zip', mode='r'
    ) as archive:
        for line in archive.read('new_hello.txt', pwd=b'secret2').split(b'\n'):
            print(line)


if __name__ == '__main__':
    run()
