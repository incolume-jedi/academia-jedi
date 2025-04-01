"""Module."""

# ruff:noqa: T201
import subprocess
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import logger

root = Path(__file__).parent
logger.debug(root)


def run():
    """Run it."""
    p = subprocess.Popen(
        'poetry run python -m zipfile --list sample.zip',
        stdout=subprocess.PIPE,
        shell=True,
    )

    print(p.communicate())

    with subprocess.Popen(
        [
            f"poetry run python -m zipfile -c {root / 'source_dir.zip'} {root / 'output_dir/'}",
        ],
        stdout=subprocess.PIPE,
    ) as proc:
        print(proc.stdout.read())


if __name__ == '__main__':  # pragma: no cover
    run()
