"""Exhaustiveness."""

from enum import Enum
from typing import NoReturn


class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'


def exhaustiveness_check(value: NoReturn) -> NoReturn:
    assert False, f'This code should never be reached, got: {value}'


def some_func(color: Color) -> str:
    match color:
        case Color.RED:
            return 'Color is red.'
        case Color.GREEN:
            return 'Color is green.'
    exhaustiveness_check(color)
    return None


def run():
    print(some_func(Color.RED))


if __name__ == '__main__':  # pragma: no cover
    run()
