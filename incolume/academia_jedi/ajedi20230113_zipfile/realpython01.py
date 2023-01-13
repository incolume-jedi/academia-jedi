import zipfile
from pathlib import Path


if __name__ == '__main__':
    zipname = Path(__file__).resolve().parent/'sample.zip'
    assert zipname.exists(), f"Ops..., {zipname}"

    with zipfile.ZipFile(zipname) as archive:
        archive.printdir()

