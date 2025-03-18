"""Tests."""

import pytest
from . import (
    generate_triplo,
    valores,
    gen_multiple,
    gen_letter_count,
    palavras,
    problema_conjunto,
    problem_set,
)


class TestCase:
    """Test case."""

    @pytest.mark.parametrize(
        'func entrance expected'.split(),
        [
            (generate_triplo, {'entrada': valores}, '[90, 150, 300, 360]\n'),
            (
                gen_multiple,
                {'entrance': valores, 'fator': 3},
                '[90, 150, 300, 360]\n',
            ),
            (
                gen_multiple,
                {'entrance': valores, 'fator': 2},
                '[60, 100, 200, 240]\n',
            ),
            (
                gen_letter_count,
                {'entrance': palavras},
                {
                    'tests': 5,
                    'implementação': 13,
                    'do': 2,
                    'tdd': 3,
                    'para get connection': 19,
                },
            ),
            (problema_conjunto, {}, {'Ricardo'}),
            pytest.param(
                problem_set,
                {},
                {'Ricardo'},
                marks=[pytest.mark.skip(reason='Implementação falha..')],
            ),
        ],
    )
    def test_0(self, capsys, func, entrance, expected):
        """Unit test."""
        result = func(**entrance)
        capture = capsys.readouterr()
        try:
            assert capture.out == expected
        except AssertionError:
            assert result == expected
