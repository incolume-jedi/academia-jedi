"""Exhaustiveness.

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
Personalização com entrada em string.
"""

import logging
from enum import Enum
from typing import NoReturn


class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'


def exhaustiveness_check(value: NoReturn) -> NoReturn:
    assert False, f'This code should never be reached, got: {value}'


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
    return None


def some_func1(color: str) -> str:
    logging.debug(Color)
    logging.debug(Color.__members__)
    logging.debug(Color.__members__.keys())
    logging.debug(Color.__members__.values())
    logging.debug(Color.__members__.items())
    logging.debug(
        {x: Color.__getitem__(x).value for x in Color.__members__},
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
    return None


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
    return None


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
            logging.exception(f'<{type(e).__name__}: {e}>')


if __name__ == '__main__':  # pragma: no cover
    run()
