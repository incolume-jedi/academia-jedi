"""Module."""

# ruff: noqa: E501

import contextlib
from subprocess import Popen

import incolume.academia_jedi.ajedi20251013_getting_elements_in_a_table_with_playwright.example2 as ex2
from icecream import ic
from incolume.academia_jedi.ajedi20251013_getting_elements_in_a_table_with_playwright import (
    example0 as ex0,
)
from incolume.academia_jedi.ajedi20251013_getting_elements_in_a_table_with_playwright import (
    example1 as ex1,
)
from incolume.academia_jedi.ajedi20251013_getting_elements_in_a_table_with_playwright import (
    utils,
)


def tratativa1() -> None:
    """Example 0."""
    site = utils.config(ex0.html_text)
    ic(site)
    with contextlib.suppress(FileNotFoundError):
        Popen(f'python -m http.server 8000 -d {site.parent}', shell=True)
    ex0.automation1('http://localhost:8000', filename=utils.filename)


def tratativa2() -> None:
    """Example 1."""
    site = utils.config(ex1.str_html)
    ic(ex1.str_html)
    ic(site)
    with contextlib.suppress(FileNotFoundError):
        Popen(f'python -m http.server 8000 -d {site.parent}', shell=True)
    ex1.actions()


def tratativa3() -> None:
    """Exemplo 2."""
    site = utils.config(content_index=ex2.str_html)
    ic(site)
    # with contextlib.suppress(OSError):
    #     Popen(f'python -m http.server 8000 -d {site.parent}', shell=True)
    ex2.actions('http://localhost:8000')


def main() -> None:
    """Run it."""
    ic('Hello from ajedi20251013-getting-elements-in-a-table-with-playwright!')
    # tratativa1()
    # tratativa2()
    tratativa3()


if __name__ == '__main__':
    main()
