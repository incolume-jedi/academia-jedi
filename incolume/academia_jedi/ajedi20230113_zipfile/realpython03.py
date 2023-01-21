import zipfile
from pathlib import Path


def tratativa2(filename):
    print("===")
    if zipfile.is_zipfile(filename):
        with zipfile.ZipFile(filename, "r") as archive:
            archive.printdir()
    else:
        print("File is not a zip file")


def run():
    zipnames = (
        Path(__file__).resolve().parent / "sample.zip",
        Path(__file__).resolve().parent / "bad_sample.zip",
    )
    for file in zipnames:
        tratativa2(file)


if __name__ == "__main__":
    run()
