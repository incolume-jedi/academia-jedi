"""Module."""
# ruff: noqa: T201

import cmath
from functools import singledispatch
from typing import Union

from icecream import ic

__all__ = ['cmath']


ic()


@singledispatch
def fun(arg, *, verbose: bool = False) -> str | tuple:  # noqa: ANN001
    """Main function."""
    # ic()
    result = f'{arg}'
    if verbose:
        # ic()
        result = 'Let me just say,', result
    return result


@fun.register
def _(arg: int, *, verbose: bool = False) -> int | tuple:
    """Case int type."""
    result = arg
    if verbose:
        result = 'Strength in numbers, eh?', result
    return result


@fun.register
def _(arg: list[str], *, verbose: bool = False) -> tuple:
    """Case list type."""
    result = []
    if verbose:
        result.append('Enumerate this:')
    for i, elem in enumerate(arg):
        result.append((i, elem))
    return tuple(result)


@fun.register
def _(arg: float, *, verbose: bool = False) -> float | tuple:
    """Case int or float type."""
    result = arg
    if verbose:
        result = 'Strength in numbers, eh?', result
    return result


@fun.register
def _(arg: Union[list, set], *, verbose: bool = False) -> list:
    """Case set or list type."""
    result = []
    if verbose:
        result.append(f'Enumerate this {type(arg).__name__}:')
    for i, elem in enumerate(arg):
        result.append((i, elem))
    return result


@fun.register(complex)
def _(arg: complex, *, verbose: bool = False) -> None:
    """Case set or list type."""
    if verbose:
        print('Better than complicated.', sep=' ')
    print(arg.real, arg.imag)


@fun.register(list)
def _(arg: list[int], *, verbose: bool = False) -> None:
    """Case list of integer type."""
    result = []
    if verbose:
        result.append('Enumerate this:')
    for i, elem in enumerate(arg):
        result.append((i, elem))


fun.register(type(None), lambda _: print('Nothing..'))
