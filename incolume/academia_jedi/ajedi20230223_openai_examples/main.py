"""Main Module."""
import logging
from platform import python_version


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)

if '3.8.6' > python_version() > '3.11.0':
    msg = (
        f"Python-{python_version()} is incompatible! "
        f"Use 3.8.6 < version < 3.11.0"
    )
    logging.warning(msg)
    print(msg)


def run():
    """Run main module."""
    logging.debug('starting ..')


if __name__ == "__main__":
    run()
