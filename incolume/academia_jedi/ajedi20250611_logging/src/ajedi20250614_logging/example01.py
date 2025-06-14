"""Example 1."""

import logging
from inspect import stack

logging.getLogger(__name__).addHandler(logging.NullHandler())


def staff():
    """Staff function."""
    logging.info('Ran %s', stack()[0][3])
