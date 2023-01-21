import zipfile
from pathlib import Path

directory = Path(__file__).parent

hello = directory.joinpath("hello.txt")
hello.write_text("hello again.")


def run():
    """raise FileNotFoundError:
    [Errno 2] No such file or directory: 'missing/hello.zip'"""
    with zipfile.ZipFile("missing/hello.zip", mode="w") as archive:
        archive.write("hello.txt")


if __name__ == "__main__":
    run()
