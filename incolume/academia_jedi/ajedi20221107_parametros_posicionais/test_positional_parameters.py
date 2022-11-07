import pytest
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


class MyTestCase:
    def test_something(self, a, b):
        assert func(a, b)
