import zipfile
from pathlib import Path
import datetime
import logging
import io
import tempfile


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)

root = Path(__file__).parent
logging.debug(root)
# TODO: Descompactar o sample.zip em /tmp/root_dir

if __name__ == "__main__":
    directory = Path(tempfile.gettempdir(), "root_dir/")
    logging.debug(directory)

    with zipfile.ZipFile(root/"directory_tree.zip", mode="w") as archive:
        for file_path in directory.rglob("*"):
            archive.write(
                file_path,
                arcname=file_path.relative_to(directory)
            )

    with zipfile.ZipFile(root/"directory_tree.zip", mode="r") as archive:
        archive.printdir()
