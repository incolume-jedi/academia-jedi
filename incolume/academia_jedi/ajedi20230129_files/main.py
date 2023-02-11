"""Main Module."""
import logging
from files_shelve import run as run1
from files_csv import run as run2
from files_pickles import run as run4


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)


def main():
    """Run main module."""
    run1()
    run2()
    run4()


if __name__ == "__main__":
    main()
