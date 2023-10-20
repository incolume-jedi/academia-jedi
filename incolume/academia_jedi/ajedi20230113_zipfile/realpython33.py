import logging
import subprocess
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

root = Path(__file__).parent
logging.debug(root)


def run():
    p = subprocess.Popen(
        'poetry run python -m zipfile --list sample.zip',
        stdout=subprocess.PIPE,
        shell=True,
    )

    print(p.communicate())

    with subprocess.Popen(
        [
            f"poetry run python -m zipfile -c {root/'source_dir.zip'} {root/'output_dir/'}"
        ],
        stdout=subprocess.PIPE,
    ) as proc:
        print(proc.stdout.read())


if __name__ == '__main__':  # pragma: no cover
    run()
