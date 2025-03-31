"""Module."""

# ruff:noqa: T201
import logging
import sys

from incolume.academia_jedi.ajedi20230113_zipfile.realpython31 import hello_pkg

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run it."""
    sys.path.insert(0, hello_pkg.as_posix())
    logging.debug(sys.path[0])
    from hello import hello

    print(hello.greet('Pythonista'))


if __name__ == '__main__':  # pragma: no cover
    run()
