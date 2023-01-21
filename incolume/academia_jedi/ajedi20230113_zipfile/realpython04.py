import zipfile
from pathlib import Path

directory = Path(__file__).parent

hello = directory.joinpath("hello.txt")
hello.write_text("hello")


def run():
    with zipfile.ZipFile(hello.with_suffix(".zip"), mode="w") as archive:
        archive.write(hello)


if __name__ == "__main__":  # pragma: no cover
    run()
