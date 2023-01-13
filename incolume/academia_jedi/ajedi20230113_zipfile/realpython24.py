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

if __name__ == "__main__":

    directory = Path(root/"output_dir/")

    with zipfile.ZipFile(root/"comp_dir.zip", "w", zipfile.ZIP_DEFLATED,
                         compresslevel=9) as archive:
        for file_path in directory.rglob("*"):
            archive.write(file_path, arcname=file_path.relative_to(directory))
