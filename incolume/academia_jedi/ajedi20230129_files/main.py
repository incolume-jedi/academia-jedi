"""Main Module."""

from incolume.academia_jedi.ajedi20230129_files.files_csv import run as run2
from incolume.academia_jedi.ajedi20230129_files.files_dbm import run as run5
from incolume.academia_jedi.ajedi20230129_files.files_json import run as run3
from incolume.academia_jedi.ajedi20230129_files.files_pickles import (
    run as run4,
)
from incolume.academia_jedi.ajedi20230129_files.files_shelve import run as run1


def main():
    """Run main module."""
    run1()
    run2()
    run3()
    run4()
    run5()


if __name__ == '__main__':
    main()
