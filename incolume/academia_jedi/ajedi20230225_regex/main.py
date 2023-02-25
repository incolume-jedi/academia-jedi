"""Main Module."""
import logging
import exemplos


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    exemplos.run()


if __name__ == "__main__":
    run()
