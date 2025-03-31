"""Module.

Pacote de distribuição python.
"""

import logging
import zipfile
from pathlib import Path

from icecream import ic
from incolume.academia_jedi.ajedi20230113_zipfile import base_dir

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


root = Path(__file__).parent / 'python-zipfile'
root.mkdir(exist_ok=True, parents=True)
logging.debug(ic('%s %s', root, root.exists()))

hello_pkg = base_dir.joinpath(
    'root_dir',
    'python_zipfile',
    'hello.zip',
)
hello_pkg.parent.mkdir(parents=True, exist_ok=True)
logging.debug(ic(hello_pkg))


def run():
    """Run it."""
    # Gerar o zip com pacote .pyc
    with zipfile.PyZipFile(hello_pkg.as_posix(), mode='w') as zip_module:
        [zip_module.writepy(x.as_posix()) for x in root.rglob('*.py')]

    # Exibe o conteúdo do pacote python zip
    with zipfile.PyZipFile(hello_pkg.as_posix(), mode='r') as zip_module:
        zip_module.printdir()


if __name__ == '__main__':  # pragma: no cover
    run()
