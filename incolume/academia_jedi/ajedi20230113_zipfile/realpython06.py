import zipfile
from pathlib import Path

directory = Path(__file__).parent

hello = directory.joinpath('hello.txt')
hello.write_text('hello')
hello.with_stem('new_hello').write_text('hello again.')


def run():
    with zipfile.ZipFile(directory / 'hello.zip', mode='a') as archive:
        archive.write(directory / 'new_hello.txt')

    with zipfile.ZipFile(directory / 'hello.zip') as archive:
        archive.printdir()


if __name__ == '__main__':
    run()
