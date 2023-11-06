"""Test preventing del obj."""
import pytest
from incolume.academia_jedi.ajedi20231106_preventing_del_obj.main import Foo, Bar

__author__ = "@britodfbr"  # pragma: no cover


def test_Bar():
    """Test bar"""
    f = Bar()
    f.name
    assert f.name == 'Bar'


def test_foo():
    """Test foo."""
    f = Foo()
    with pytest.raises(AttributeError, match='*object has no attribute*'):
        del f.name
        assert f.name == ''


