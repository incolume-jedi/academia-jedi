"""Module."""
# ruff: noqa: T201

import cmath
from functools import singledispatch
from inspect import Parameter, signature, stack
from typing import Union, get_type_hints

from icecream import ic

__all__ = ['cmath']


ic()


@singledispatch
def fun(arg, *, verbose: bool = False) -> str | tuple:  # noqa: ANN001
    """Main function."""
    ic(
        Parameter(
            stack()[0][3],
            Parameter.POSITIONAL_OR_KEYWORD,
        ).name,
    )
    result = f'{arg}'
    if verbose:
        result = 'Let me just say,', result
    return result


@fun.register
def _(arg: int, *, verbose: bool = False) -> int | tuple:
    """Case int type."""
    ic(
        Parameter(
            stack()[0][3],
            Parameter.POSITIONAL_OR_KEYWORD,
        ).name,
    )
    result = arg
    if verbose:
        result = 'Strength in numbers, eh?', result
    return result


@fun.register
def _(arg: list, *, verbose: bool = False) -> tuple:
    """Case list type."""
    ic(
        Parameter(
            stack()[0][3],
            Parameter.POSITIONAL_OR_KEYWORD,
        ).name,
    )
    result = []
    if verbose:
        result.append('Enumerate this:')
    for i, elem in enumerate(arg):
        result.append((i, elem))
    return tuple(result)


@fun.register
def _(arg: float, *, verbose: bool = False) -> float | tuple:
    """Case int or float type."""
    ic(
        Parameter(
            stack()[0][3],
            Parameter.POSITIONAL_OR_KEYWORD,
        ).name,
    )
    result = arg
    if verbose:
        result = 'Strength in numbers, eh?', result
    return result


@fun.register
def _(arg: Union[list, set], *, verbose: bool = False) -> list:
    """Case set or list type."""
    ic(
        Parameter(
            stack()[0][3],
            Parameter.POSITIONAL_OR_KEYWORD,
        ).name,
    )
    result = []
    if verbose:
        result.append(f'Enumerate this {type(arg).__name__}:')
    for i, elem in enumerate(arg):
        result.append((i, elem))
    return result


@fun.register(complex)
def _(arg: complex, *, verbose: bool = False) -> None:
    """Case set or list type."""
    ic(
        Parameter(
            stack()[0][3],
            Parameter.POSITIONAL_OR_KEYWORD,
        ).name,
    )
    if verbose:
        print('Better than complicated.', sep=' ')
    print(arg.real, arg.imag)


@fun.register(list)
def _(arg: list, *, verbose: bool = False) -> list:
    """Case list of integer type."""
    ic(
        Parameter(
            stack()[0][3],
            Parameter.POSITIONAL_OR_KEYWORD,
        ).name,
    )
    result = []
    if verbose:
        result.append('Enumerate this:')
    for i, elem in enumerate(arg):
        result.append((i, elem))
    return result


fun.register(type(None), lambda _: print('Nothing..'))
