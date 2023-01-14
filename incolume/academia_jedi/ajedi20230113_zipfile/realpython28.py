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


def run():
    logging.debug('Creted object zipfile to handler')
    hello_txt = zipfile.Path(root/"sample.zip", "hello.txt")

    print(
        hello_txt,
        hello_txt.name,
        hello_txt.is_file(),
        hello_txt.exists(),
        hello_txt.read_text(),
        sep='\n'
    )

    with hello_txt.open(mode="r") as hello:
        for line in hello:
            print(line)


if __name__ == "__main__":
    run()
