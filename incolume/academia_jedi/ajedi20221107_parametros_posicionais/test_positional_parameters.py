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


@pytest.mark.parametrize(
    'tparam dparam expected'.split(),
    (
        ((10, 20, 30), {'d': 40, 'e': 50, 'f': 60}, None),
    ),
)
def test_func(tparam, dparam, expected):
    assert func(*tparam, **dparam) == expected


@pytest.mark.parametrize(
    'a b c d'.split(),
    (
        (1, 2),
    ),
)
class MyTestCase:
    def test_something(self, a, b):
        assert func(a, b)
