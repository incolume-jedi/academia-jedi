"""Argumento python."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from typing import NoReturn


def f(a: int, b: int = 0, c: int = 0, d: int = 0) -> tuple:
    """Funct."""
    return a, b, c, d


def g(a: int, /, b: int = 0, c: int = 0, d: int = 0) -> tuple:
    """Funct."""
    return a, b, c, d


def h(a: int = 0, /, b: int = 0, *, c: int = 0, d: int = 0) -> tuple:
    """Funct."""
    return a, b, c, d


def i(*args: int, **kwargs: int) -> dict:
    """Funct."""
    return {'args': args, **kwargs}


def j(a: int, /, *args: int, **kwargs: int) -> dict:
    """Funct."""
    return {'args': args, **kwargs}


def k(a: int, /, *args: int, **kwargs: int) -> dict:
    """Funct."""
    return {'args': (a, *args), **kwargs}


def run() -> NoReturn:
    """Run it."""
    print(
        f(1),
        f(1, 2, 3, 4),
        f(a=1, d=2, b=3, c=4),
        g(1),
        g(1, 2, 3, 4),
        g(1, b=2, c=3, d=4),
        h(),
        h(1),
        h(1, b=2, c=3, d=4),
        h(1, 2, c=3, d=4),
        h(1, 2, d=4, c=3),
        i(1, 2, 3, 4),
        i(2, 1, 4, 3),
        i(b=2, a=1, d=4, c=3),
        j(1, b=2, d=4, c=3),
        k(1, b=2, d=4, c=3),
        k(1, 2, d=4, c=3),
        sep='\n',
    )


if __name__ == '__main__':
    run()
