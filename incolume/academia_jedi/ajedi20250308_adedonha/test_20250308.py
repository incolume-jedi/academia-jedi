"""Submodule test."""

from typing import NoReturn
import pytest
import incolume.academia_jedi.ajedi20250308_adedonha as pkg


class TestAdedonha:
    """Test case."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, 'A'),
            (5, 'E'),
            (26, 'Z'),
            (10, 'J'),
            (100, 'V'),
            (80, 'B'),
            (15, 'O'),
            (19, 'S'),
            (36, 'J'),
            (1000, 'L'),
            pytest.param(
                '',
                {
                    'expected_exception': TypeError,
                    'match': 'only numeric values',
                },
                marks=[],
            ),
            pytest.param(
                'a',
                {
                    'expected_exception': TypeError,
                    'match': 'only numeric values',
                },
                marks=[],
            ),
            pytest.param(
                1.1,
                {
                    'expected_exception': TypeError,
                    'match': 'only numeric values',
                },
                marks=[],
            ),
            pytest.param(
                '3j',
                {
                    'expected_exception': TypeError,
                    'match': 'only numeric values',
                },
                marks=[],
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        if isinstance(expected, dict):
            with pytest.raises(**expected):
                pkg.adedonha(entrance)
        else:
            assert pkg.adedonha(entrance) == expected
