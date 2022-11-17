import pytest
from .positional_parameters import (
    func,
    divmod,
)

__author__ = '@britodfbr'  # pragma: no cover


# @pytest.mark.parametrize(
#     'tparam dparam expected'.split(),
#     (
#         ((10, 20, 30), {'d': 40, 'e': 50, 'f': 60}, None),
#     ),
# )
# def test_func(tparam, dparam, expected):
#     assert func(*tparam, **dparam) == expected
#
#
# @pytest.mark.parametrize(
#     'a b c d'.split(),
#     (
#         (1, 2),
#     ),
# )
# class MyTestCase:
#     def test_something(self, a, b):
#         assert func(a, b)

def test_func(capsys):
    func(10, 20, 30, d=40, e=50, f=60)
    msgerr, msgout = capsys.readouterr()
    assert msgerr.strip() == '10 20 30 40 50 60'


def test_func1():
    with pytest.raises(
        TypeError,
        match=r"got some positional-only "
              r"arguments passed as keyword arguments: 'b'"
    ):
        func(10, b=20, c=30, d=40, e=50, f=60)  # b cannot be keyword argument


def test_func2():
    with pytest.raises(
        TypeError,
        match=r"takes 4 positional arguments but 5 positional "
              "arguments \(and 1 keyword-only argument\) were given"
    ):
        func(10, 20, 30, 40, 50, f=60)  # b cannot be keyword argument


def test_divmod():
    assert divmod(1, 2)


def test_divmod1():
    with pytest.raises(TypeError, match=''):
        divmod(1, b=2)


def test_divmod2():
    with pytest.raises(TypeError, match=''):
        divmod(a=1, b=2)


def test_divmod3():
    with pytest.raises(TypeError, match=''):
        divmod(None, None, a=1)
