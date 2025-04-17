"""Module."""
# ruff:noqa: T201

import logging

from incolume.academia_jedi.ajedi20230127_str_trans.tratativa1 import (
    elements_this,
)


def tratativa1():
    """Tratativa."""
    entrance, cipher, _ = elements_this()
    logging.debug(entrance)

    decoder = str.maketrans(cipher)
    logging.debug(decoder)

    result = entrance.translate(decoder)
    logging.debug(result)

    return result


if __name__ == '__main__':
    print(tratativa1())
