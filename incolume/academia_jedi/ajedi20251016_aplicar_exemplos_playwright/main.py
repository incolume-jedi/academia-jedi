"""Module."""

import incolume.academia_jedi.ajedi20251016_aplicar_exemplos_playwright.tratativa1 as ex1
import incolume.academia_jedi.ajedi20251016_aplicar_exemplos_playwright.tratativa2 as ex2
import incolume.academia_jedi.ajedi20251016_aplicar_exemplos_playwright.tratativa3 as ex3
import incolume.academia_jedi.ajedi20251016_aplicar_exemplos_playwright.tratativa4 as ex4
from icecream import ic
from incolume.academia_jedi import utils


@utils.nonexequi(
    # suppress=False
)
def tratativa1() -> None:
    """Example 1."""
    site = utils.config(ex2.str_html)
    ic(site)
    ex1.actions()


@utils.nonexequi(
    # suppress=False
)
def tratativa2() -> None:
    """Example 2."""
    site = utils.config(ex2.str_html)
    ic(site)
    ex2.actions()


@utils.nonexequi(
    suppress=False,
)
def tratativa3() -> None:
    """Example 3."""
    site = utils.config(ex2.str_html)
    ic(site)
    ex3.actions()


@utils.nonexequi(suppress=False)
def tratativa4() -> None:
    """Example 4."""
    site = utils.config(ex2.str_html)
    ic(site)
    ex4.actions()


def main():
    """Run it."""
    ic('Hello from ajedi20251016-aplicar-exemplos-playwright!')
    ic(utils.check_web_resource())
    tratativa1()
    tratativa2()
    tratativa3()
    tratativa4()


if __name__ == '__main__':
    main()
