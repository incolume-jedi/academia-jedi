"""Main Module."""

from icecream import ic
from incolume.academia_jedi import logger


def run():
    """Run main module."""
    logger.debug(ic('starting ..'))


if __name__ == '__main__':
    run()
