import zipfile
from pathlib import Path

directory = Path(__file__).parent


def run():
    with zipfile.ZipFile(directory / 'sample.zip', mode='r') as archive:
        for filename in archive.namelist():
            print(filename)


if __name__ == '__main__':
    run()
