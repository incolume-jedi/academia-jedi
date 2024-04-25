import pytest
from incolume.academia_jedi.ajedi20231115_functools_singledispatch.main import (
    fun,
)

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseSingleDispatch:
    """Exemplas for singledispatch."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('ola', 'Let me just say, ola'),
            (True, 'Strength in boolean, eh? True'),
            ([1, 2, 3], 'Enumerate this:\n0 1\n1 2\n2 3'),
            (1, 'Strength in numbers, eh? 1'),
            (1.0, 'Strength in numbers, eh? 1.0'),
            ((1, 2, 3), 'Enumerate this:\n0 1\n1 2\n2 3'),
            ({1, 2, 3}, 'Enumerate this:\n0 1\n1 2\n2 3'),
            (3 + 2j, 'Better than complicated. 3.0 2.0'),
        ],
    )
    def test_0(self, entrance, expected, capsys):
        """"""
        fun(entrance, True)
        out, err = capsys.readouterr()
        assert out.strip() == expected
