import zipfile
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)

root = Path(__file__).parent
logging.debug(root)

hello = root.joinpath('python-zipfile', "hello.zip")
logging.debug(hello)


def run():
    # Gerar o zip com pacote .pyc
    with zipfile.PyZipFile(hello.as_posix(), mode="w") as zip_module:
        zip_module.writepy(hello.with_suffix(".py").as_posix())

    # Exibe o conteúdo do pacote python zip
    with zipfile.PyZipFile(hello.as_posix(), mode="r") as zip_module:
        zip_module.printdir()


if __name__ == '__main__':  # pragma: no cover
    run()
