"""Module."""

import logging
from typing import NoReturn

import ex_fpdf2 as ex1

__author__ = '@britodfbr'  # pragma: no cover


logging.basicConfig(level=logging.INFO)


def run() -> NoReturn:
    """Run it."""
    ex1.example_minimal()
    ex1.example_report1()
    ex1.tuto02()


if __name__ == '__main__':  # pragma: no cover
    run()
