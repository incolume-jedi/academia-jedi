import zipfile
import logging
from pathlib import Path
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)

root = Path(__file__).parent
logging.debug(root)

packhello = root.joinpath('python-zipfile', "hello.zip")
logging.debug(packhello)


def run():
    sys.path.insert(0, packhello.as_posix())
    logging.debug(sys.path[0])
    from hello import hello

    print(hello.greet("Pythonista"))


if __name__ == '__main__':  # pragma: no cover
    run()
