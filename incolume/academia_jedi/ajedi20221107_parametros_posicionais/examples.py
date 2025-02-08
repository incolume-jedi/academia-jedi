# !/usr/bin/env python

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from positional_parameters import (
    divmod,
    func,
    myfunc,
    myfunc1,
    myfunc2,
    myfunc3,
    myfunc4,
)

__author__ = '@britodfbr'  # pragma: no cover


def example1():
    """Argumentos predefinidos como posicionais e/ou chaveados."""
    func(10, 20, 30, d=40, e=50, f=60)  # Válido
    try:
        func(10, b=20, c=30, d=40, e=50, f=60)  # b cannot be keyword argument
    except TypeError as e:
        print(e)

    try:
        func(10, 20, 30, 40, 50, f=60)  # e must be a keyword argument
    except TypeError as e:
        print(e)


def example2():
    """Argumentos exclusivamente posicionais."""
    divmod(10, 3)  # Válido

    try:
        divmod(a=10, b=3)
    except TypeError as e:
        print(e)


def example3():
    """Argumentos posicionais/chaveados. Comportamento padrão python."""
    print(
        myfunc(1, 2),
        myfunc(1, b=2),
        myfunc(a=1, b=2),
        myfunc(b=2, a=1),
    )


def example4():
    """Argumentos posicionais exclusivamente."""
    print(
        myfunc2(1, 2),
    )
    try:
        (myfunc2(1, b=2),)
    except TypeError as e:
        print(e)
    try:
        (myfunc2(a=1, b=2),)
    except TypeError as e:
        print(e)
    try:
        (myfunc2(b=2, a=1),)
    except TypeError as e:
        print(e)


def example5():
    """Argumentos chaveados exclusivamente."""
    try:
        myfunc3(1, 2)
    except TypeError as e:
        print(e)
    try:
        myfunc3(1, b=2)
    except TypeError as e:
        print(e)

    print(myfunc3(a=1, b=2))
    print(myfunc3(b=2, a=1))


def example6():
    """Ambos argumentos posicionais e chaveados."""
    print(
        myfunc4(1, 2),
        myfunc4(a=1, b=2),
        myfunc4(1, b=2),
        myfunc4(a=1),
        myfunc4(b=2),
        myfunc4(1),
        myfunc4(None, 2),
        myfunc4(1, 2, a=1, b=2),
    )


def example7():
    """"""
    print(
        myfunc1(1),
        myfunc1(None, 2),
        myfunc1(a=1, b=2),
        myfunc1(1, 2),
        myfunc1(1, b=2),
        myfunc1(a=1),
        myfunc1(b=2),
    )
    try:
        myfunc1(None, a=1)
        (myfunc1(1, 2, a=1, b=2),)
    except TypeError as e:
        print(e)


def run():
    funcs = [
        example1,
        example2,
        example3,
        example4,
        example5,
        example6,
        example7,
    ]

    for func in funcs:
        print()
        print(f'{func.__name__}'.ljust(90, '-'))
        print(f'{func.__name__:^90}')
        print('doc:', f'{func.__doc__}')
        print('doc'.rjust(90, '-'))
        func()
        print(f'{func.__name__:->90}')
        print()


if __name__ == '__main__':  # pragma: no cover
    run()
