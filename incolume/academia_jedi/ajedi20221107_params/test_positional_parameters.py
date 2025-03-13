"""Test module."""

import pytest

from .positional_params import mydivmod, func

__author__ = '@britodfbr'  # pragma: no cover


# @pytest.mark.parametrize(
#     ),
# def test_func(tparam, dparam, expected):
#
#
# @pytest.mark.parametrize(
#     ),
# class MyTestCase:
#     def test_something(self, a, b):


def test_func(capsys):
    """Unittest."""
    func(10, 20, 30, d=40, e=50, f=60)
    result = capsys.readouterr()
    assert result.out.strip() == '10 20 30 40 50 60'


def test_func1():
    """Unittest."""
    with pytest.raises(
        TypeError,
        match=r'got some positional-only '
        r"arguments passed as keyword arguments: 'b'",
    ):
        func(10, b=20, c=30, d=40, e=50, f=60)  # b cannot be keyword argument


def test_func2():
    """Unittest."""
    with pytest.raises(
        TypeError,
        match=r'takes 4 positional arguments but 5 positional '
        r'arguments \(and 1 keyword-only argument\) were given',
    ):
        func(10, 20, 30, 40, 50, f=60)  # b cannot be keyword argument


def test_divmod():
    """Unittest."""
    assert mydivmod(1, 2)


def test_divmod1():
    """Unittest."""
    with pytest.raises(TypeError, match=''):
        mydivmod(1, b=2)


def test_divmod2():
    """Unittest."""
    with pytest.raises(TypeError, match=''):
        mydivmod(a=1, b=2)


def test_divmod3():
    """Unittest."""
    with pytest.raises(TypeError, match=''):
        mydivmod(None, None, a=1)
