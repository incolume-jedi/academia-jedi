# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover


def func(a, b, /, c, d, *, e, f):
    """Argumentos predefinidos como posicionais e/ou chaveados."""
    print(a, b, c, d, e, f)


def divmod(a, b, /):
    """Emulate the built in divmod() function"""
    return a // b, a % b


def myfunc(a, b):
    """Argumentos posicionais/chaveados. Comportamento padrão python"""
    return a, b


def myfunc1(a=None, b=None, **kwargs):
    """Argumentos posicionais/chaveados. Comportamento padrão"""
    return a, b, kwargs


def myfunc2(a, b, /):
    """Argumentos posicionais exclusivamente."""
    return a, b


def myfunc3(*, a, b):
    """Argumentos chaveados exclusivamente."""
    return a, b


def myfunc4(a=None, b=None, /, **kwargs):
    """Ambos argumentos posicionais e chaveados."""
    return a, b, kwargs
