"""Tests."""

import pytest
from . import generate_triplo, valores, gen_multiple


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
        ],
    )
    def test_0(self, capsys, func, entrance, expected):
        """Unit test."""
        func(**entrance)
        capture = capsys.readouterr()

        assert capture.out == expected
