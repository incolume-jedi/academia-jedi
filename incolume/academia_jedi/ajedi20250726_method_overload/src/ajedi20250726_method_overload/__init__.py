"""Module for ajedi20250726-method-overload."""

from __future__ import annotations

from decimal import Decimal
from functools import singledispatchmethod


class Negator:
    """Class providing overloaded negation methods for various types."""

    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        """Negate the given argument.

        Raises:
        ------
        NotImplementedError
            If negation is not implemented for the argument's type.
        """
        msg = f'Cannot negate a {type(arg).__name__} value: {arg}'
        raise NotImplementedError(msg)

    @neg.register(Decimal)
    @neg.register(float)
    @neg.register(int)
    @classmethod
    def _(cls, arg):
        return -arg

    @neg.register(bool)
    @classmethod
    def _(cls, arg):
        return not arg


def main() -> None:
    """Hello from ajedi20250726-method-overload!"""
