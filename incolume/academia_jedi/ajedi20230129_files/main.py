"""Main Module."""
import logging
from files_shelve import run as run1
from files_csv import run as run2
from files_json import run as run3
from files_pickles import run as run4
from files_dbm import run as run5


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
    "%(module)s;%(funcName)s;%(message)s",
)


def main():
    """Run main module."""
    run1()
    run2()
    run3()
    run4()
    run5()


if __name__ == "__main__":
    main()
