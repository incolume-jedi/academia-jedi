# !/usr/bin/env python
# -*- coding: utf-8 -*-
from positional_parameters import (
divmod,
func,
myfunc,
myfunc1,
myfunc2,
myfunc3,
myfunc4
)


__author__ = "@britodfbr"  # pragma: no cover


def example1():
    """Argumentos predefinidos como posicionais e/ou chaveados."""

    def func(a, b, /, c, d, *, e, f):
        print(a, b, c, d, e, f)

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

    def divmod(a, b, /):
        """Emulate the built in divmod() function"""
        return a // b, a % b

    divmod(10, 3)  # Válido

    try:
        divmod(a=10, b=3)
    except TypeError as e:
        print(e)


def example3():
    """Argumentos posicionais/chaveados. Comportamento padrão python"""

    def myfunc(a, b):
        return a, b

    print(
        myfunc(1, 2),
        myfunc(1, b=2),
        myfunc(a=1, b=2),
        myfunc(b=2, a=1),
    )


def example4():
    """Argumentos posicionais exclusivamente."""

    def myfunc(a, b, /):
        return a, b

    print(myfunc(1, 2), )
    try:
        myfunc(1, b=2),
    except TypeError as e:
        print(e)
    try:
        myfunc(a=1, b=2),
    except TypeError as e:
        print(e)
    try:
        myfunc(b=2, a=1),
    except TypeError as e:
        print(e)


def example5():
    """Argumentos chaveados exclusivamente."""

    def myfunc(*, a, b):
        return a, b

    try:
        myfunc(1, 2)
    except TypeError as e:
        print(e)
    try:
        myfunc(1, b=2)
    except TypeError as e:
        print(e)

    print(myfunc(a=1, b=2))
    print(myfunc(b=2, a=1))


def example6():
    """Ambos argumentos posicionais e chaveados."""

    def myfunc(a=None, b=None, /, **kwargs):
        return a, b, kwargs

    print(
        myfunc(1, 2),
        myfunc(a=1, b=2),
        myfunc(1, b=2),
        myfunc(a=1),
        myfunc(b=2),
        myfunc(1),
        myfunc(None, 2),
        myfunc(1, 2, a=1, b=2),
    )


def example7():
    """"""
    def myfunc(a=None, b=None, **kwargs):
        return a, b, kwargs
    print(
        myfunc(1),
        myfunc(None, 2),
        myfunc(a=1, b=2),
        myfunc(1, 2),
        myfunc(1, b=2),
        myfunc(a=1),
        myfunc(b=2),
    )
    try:
        myfunc(None, a=1)
        myfunc(1, 2, a=1, b=2),
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
        print('')
        print(f'{func.__name__}'.ljust(90, '-'))
        print(f'{func.__name__:^90}')
        print('doc:', f'{func.__doc__}')
        print('doc'.rjust(90, '-'))
        func()
        print(f'{func.__name__:->90}')
        print('')


if __name__ == '__main__':  # pragma: no cover
    run()
