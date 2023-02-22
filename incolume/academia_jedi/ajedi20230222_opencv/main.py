"""Main Module."""
import logging
from incolume.academia_jedi.ajedi20230222_opencv import tratativa1


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    tratativa1.run()
    

if __name__ == "__main__":
    run()
