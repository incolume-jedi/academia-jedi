import pytest
from incolume.academia_jedi.ajedi20231115_typing_overload.main import double
from incolume.academia_jedi.ajedi20231115_typing_overload.main import process

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseDoble:
    """Test doble."""
    def test_doble_int(self) -> None:
        """Test it."""
        assert double(1) == 2

    def test_doble_seq(self) -> None:
        """Test it."""
        assert double((1, 2, 3)) == [2, 4, 6]


class TestCaseProcess:
    """Test Process."""
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, "<class 'int'>"),
            (1., "<class 'float'>"),
            ('1', "<class 'str'>"),
            (None, "<class 'NoneType'>"),
            (False, "<class 'bool'>"),
        ],
    )
    def test_process(self, entrance, expected):
        """Test process."""
        assert process(entrance) == expected
