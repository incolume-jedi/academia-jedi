import logging
import zipfile
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

root = Path(__file__).parent
logging.debug(root)
# TODO: Descompactar o sample.zip em /tmp/root_dir


def append_member(zip_file, member):
    with zipfile.ZipFile(zip_file, mode='a') as archive:
        logging.debug(f'Appended {zip_file} into {archive.filename}')
        archive.write(member)


def get_file_from_stream():
    """Simulate a stream of files."""
    yield from root.rglob('**/*.md')


def run(zipname: str = ''):
    zipname = zipname or root / 'incremental.zip'

    for filename in get_file_from_stream():
        append_member(zipname, filename)

    with zipfile.ZipFile(zipname, mode='r') as archive:
        archive.printdir()


if __name__ == '__main__':
    run()
