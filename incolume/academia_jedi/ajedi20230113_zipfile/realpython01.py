import zipfile
from pathlib import Path


def run():
    zipname = Path(__file__).resolve().parent / 'sample.zip'
    assert zipname.exists(), f'Ops..., {zipname}'

    with zipfile.ZipFile(zipname) as archive:
        archive.printdir()


if __name__ == '__main__':
    run()
