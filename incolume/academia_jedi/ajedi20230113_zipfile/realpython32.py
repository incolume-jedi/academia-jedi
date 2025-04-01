"""Module."""

# ruff:noqa: T201
import sys

from incolume.academia_jedi.ajedi20230113_zipfile import logger
from incolume.academia_jedi.ajedi20230113_zipfile.realpython31 import hello_pkg

def run():
    """Run it."""
    sys.path.insert(0, hello_pkg.as_posix())
    logger.debug(sys.path[0])
    from hello import hello

    print(hello.greet('Pythonista'))


if __name__ == '__main__':  # pragma: no cover
    run()
