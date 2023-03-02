"""Exhaustiveness."""
import logging
from enum import Enum
from typing import NoReturn
import os


class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"


def exhaustiveness_check(value: NoReturn) -> NoReturn:
    assert False, "This code should never be reached, got: {0}".format(value)


def some_func(color: Color) -> str:
    match color:
        case Color.RED:
            return "Color is red."
        case Color.GREEN:
            return "Color is green."
    exhaustiveness_check(color)


def run():
    try:
        print(some_func(Color.BLUE))
    except AssertionError as e:
        e.add_note("Ops..")
        logging.error(e)


if __name__ == "__main__":  # pragma: no cover
    run()
