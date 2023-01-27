"""Exemplo singledispatch."""

from functools import singledispatch
import logging

__author__ = "@britodfbr"  # pragma: no cover


@singledispatch
def inverse(arg):
    logging.debug("..")
    ...


@inverse.register
def _(arg: int):
    logging.info(f"{arg=}; {type(arg)=}")
    return -arg


@inverse.register
def _(arg: str):
    logging.info(f"{arg=}; {type(arg)=}")
    return arg[::-1]


@inverse.register
def _(arg: float):
    logging.info(f"{arg=}; {type(arg)=}")
    return -arg


@inverse.register
def _(arg: bool):
    logging.info(f"{arg=}; {type(arg)=}")
    return not arg
