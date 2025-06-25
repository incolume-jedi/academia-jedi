import logging

# ruff: noqa: D100, D419, FBT003
from incolume.academia_jedi.ajedi20230122_python_overload.tratativa1 import (
    inverse,
)
from incolume.academia_jedi.ajedi20230122_python_overload.tratativa2 import (
    HandlerReverse,
)

__author__ = '@britodfbr'  # pragma: no cover

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """"""
    logging.debug('..')
    print(inverse('abc'))
    print(inverse(123))
    print(inverse(123.4))
    print(inverse(False))

    hadler = HandlerReverse()
    print(hadler.reverse('abc'))
    print(hadler.reverse(123))
    print(hadler.reverse(123.4))
    print(hadler.reverse(True))


if __name__ == '__main__':  # pragma: no cover
    run()
