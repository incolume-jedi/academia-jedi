"""Module."""

# ruff:noqa: T201 S603
import subprocess
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import logger

root = Path(__file__).parent
logger.debug(root)


def run():
    """Run it."""
    p = subprocess.Popen(
        'poetry run python -m zipfile --list sample.zip'.split(),
        stdout=subprocess.PIPE,
    )

    print(p.communicate())

    fzip: Path = root / 'source_dir.zip'
    dout: Path = root / 'output_dir/'

    with subprocess.Popen(
        f'poetry run python -m zipfile -c {fzip} {dout}'.split(),
        stdout=subprocess.PIPE,
    ) as proc:
        print(proc.stdout.read())


if __name__ == '__main__':  # pragma: no cover
    run()
