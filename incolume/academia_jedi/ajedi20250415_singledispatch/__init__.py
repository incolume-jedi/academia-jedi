"""Module."""

# ruff: noqa: T201
from __future__ import annotations

import cmath
from functools import singledispatch
from typing import Union, List, Set

from icecream import ic

__all__ = ['cmath']


ic()


@singledispatch
def fun(arg, *, verbose: bool = False) -> str | tuple:  # noqa: ANN001
    """Main function."""
    ic('base')
    result = f'{arg}'
    if verbose:
        result = 'Let me just say,', result
    return result


@fun.register
def _(arg: int, *, verbose: bool = False) -> int | tuple:
    """Case int type."""
    ic('int')
    result = arg
    if verbose:
        result = 'Strength in numbers, eh?', result
    return result


@fun.register
def _(arg: tuple, *, verbose: bool = False) -> tuple:
    """Case list type."""
    ic('tuple')
    result = []
    if verbose:
        result.append('Enumerate this tuple:')
    for i, elem in enumerate(arg):
        result.append((i, elem))
    return tuple(result)


@fun.register
def _(arg: float, *, verbose: bool = False) -> float | tuple:
    """Case int or float type."""
    ic('float')
    result = arg
    if verbose:
        result = 'Strength in numbers, eh?', result
    return result


@fun.register
def _(arg: Union[List, Set], *, verbose: bool = False) -> list:
    """Case set or list type."""
    ic('Union[list|set]')
    result = []
    if verbose:
        result.append(f'Enumerate this {type(arg).__name__}:')
    for i, elem in enumerate(sorted(arg)):
        result.append((i, elem))
    return result


@fun.register(complex)
def _(arg: complex, *, verbose: bool = False) -> tuple:
    """Case set or list type."""
    ic('complex')
    result = (arg.real, arg.imag)
    if verbose:
        result = 'Better than complicated.', result

    return result


@fun.register(list)
def _(arg: list, *, verbose: bool = False) -> list:
    """Case list of integer type."""
    ic('list2')
    result = []
    if verbose:
        result.append('Enumerate this:')
    for i, elem in enumerate(arg):
        result.append((i, elem))
    return result


fun.register(type(None), lambda _: print('Nothing..'))
