"""Module."""

import zipfile
from pathlib import Path

from icecream import ic
from incolume.academia_jedi.ajedi20230113_zipfile import base_dir, logger

root = base_dir / 'root_dir'
root.mkdir(exist_ok=True, parents=True)
logger.debug(ic('%s %s', root, root.exists()))

hello = base_dir.joinpath(
    'root_dir',
    'python_zipfile',
    f'{Path(__file__).stem}.zip',
)
hello.parent.mkdir(parents=True, exist_ok=True)
logger.debug(ic(hello))


def run():
    """Run it."""
    # Gerar o zip com pacote .pyc
    with zipfile.PyZipFile(hello.as_posix(), mode='w') as zip_module:
        zip_module.writepy(Path(__file__).as_posix())

    # Exibe o conteúdo do pacote python zip
    with zipfile.PyZipFile(hello.as_posix(), mode='r') as zip_module:
        zip_module.printdir()


if __name__ == '__main__':  # pragma: no cover
    run()
