"""Module."""

# ruff: noqa: T201 UP035
from __future__ import annotations

import cmath
import sys
from functools import singledispatch
from typing import List, Set, Union

from icecream import ic
from incolume.academia_jedi import logger

__all__ = ['cmath']


ic()


@singledispatch
def fun(arg: str, *, verbose: bool = False) -> str | tuple:
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


if sys.version_info < (3, 11):

    @fun.register
    def _(arg: list, *, verbose: bool = False) -> list:
        """Case list type."""
        ic('list')
        result = []
        if verbose:
            result.append(f'Enumerate this {type(arg).__name__}:')
        for i, elem in enumerate(sorted(arg)):
            result.append((i, elem))
        return result

    @fun.register
    def _(arg: set, *, verbose: bool = False) -> list:
        """Case set type."""
        ic('set')
        result = []
        if verbose:
            result.append(f'Enumerate this {type(arg).__name__}:')
        for i, elem in enumerate(sorted(arg)):
            result.append((i, elem))
        return result
else:
    try:

        @fun.register
        def _(arg: list | set, *, verbose: bool = False) -> list:
            """Case set or list type."""
            ic('list | set')
            result = []
            if verbose:
                result.append(f'Enumerate this {type(arg).__name__}:')
            for i, elem in enumerate(sorted(arg)):
                result.append((i, elem))
            return result
    except TypeError:
        logger.exception('Python 3.11+ is required for this feature.')


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
