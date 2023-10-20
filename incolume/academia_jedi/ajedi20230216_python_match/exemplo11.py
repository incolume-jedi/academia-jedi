"""Exhaustiveness.
Personalização com entrada em string
"""
import logging
from enum import Enum
from typing import NoReturn


class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'


def exhaustiveness_check(value: NoReturn) -> NoReturn:
    assert False, 'This code should never be reached, got: {0}'.format(value)


def some_func0(color: str) -> str:
    logging.debug(color)
    logging.debug(color.title())
    colors = [c.value for c in list(Color)]
    logging.debug(colors)
    match = color.title() if color.title() in colors else None
    print(match)
    match match:
        case 'Red':
            return 'Color is red.'
        case 'Green':
            return 'Color is green.'
    exhaustiveness_check(color)


def some_func1(color: str) -> str:
    logging.debug(Color)
    logging.debug(Color.__members__)
    logging.debug(Color.__members__.keys())
    logging.debug(Color.__members__.values())
    logging.debug(Color.__members__.items())
    logging.debug(
        {x: Color.__getitem__(x).value for x in Color.__members__.keys()}
    )
    logging.debug({x: y.value for x, y in Color.__members__.items()})
    logging.debug({x.name: x.value for x in Color.__members__.values()})
    logging.debug(Color.__getitem__('BLUE'))
    logging.debug(Color('Green'))
    match = Color(color.title())
    logging.debug(match)
    match match:
        case Color.RED:
            return 'Color is red.'
        case Color.GREEN:
            return 'Color is green.'
    exhaustiveness_check(color)


def some_func(color: str) -> str:
    logging.debug(color)
    match = Color(color.title())
    logging.debug(match)
    match match:
        case Color.RED:
            return 'Color is red.'
        case Color.GREEN:
            return 'Color is green.'
    exhaustiveness_check(color)


def run():
    colors = (
        'green',
        'blue',
        'purple',
        'black',
        'yellow',
        'red',
    )
    for color in colors:
        try:
            print(some_func(color))
        except (AssertionError, ValueError) as e:
            logging.error(f'<{type(e).__name__}: {e}>')


if __name__ == '__main__':  # pragma: no cover
    run()
