import zipfile
from pathlib import Path
import logging
import tempfile

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)

root = Path(__file__).parent
logging.debug(root)


def run():
    # TODO: Descompactar o sample.zip em /tmp/root_dir

    directory = Path(tempfile.gettempdir(), "root_dir/")
    logging.debug(directory)

    with zipfile.ZipFile(root / "directory_tree.zip", mode="w") as archive:
        for file_path in directory.rglob("*"):
            archive.write(file_path, arcname=file_path.relative_to(directory))

    with zipfile.ZipFile(root / "directory_tree.zip", mode="r") as archive:
        archive.printdir()


if __name__ == "__main__":
    run()
