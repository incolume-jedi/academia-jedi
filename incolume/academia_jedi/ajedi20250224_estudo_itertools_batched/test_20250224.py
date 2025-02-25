"""Test Module for studing itertools.batched."""

import pytest
import incolume.academia_jedi.ajedi20250224_estudo_itertools_batched as pkg


class TestCase:
    """Unit test."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'array': [1, 2, 3], 'length': 2},
                [(1, 2), (3,)],
                marks=[],
            ),
            pytest.param(
                {'array': [1, 2, 3], 'length': 3},
                [(1, 2, 3)],
                marks=[],
            ),
            pytest.param(
                {'array': [1, 2, 3, 4, 5, 6], 'length': 3},
                [(1, 2, 3), (4, 5, 6)],
                marks=[],
            ),
            pytest.param(
                {'array': range(10), 'length': 4},
                [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9)],
                marks=[],
            ),
            pytest.param(
                {'array': range(10), 'length': 5},
                [(0, 1, 2, 3, 4), (5, 6, 7, 8, 9)],
                marks=[],
            ),
            pytest.param(
                {'array': range(10), 'length': 2},
                [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)],
                marks=[],
            ),
            pytest.param('', '', marks=[pytest.mark.skip]),
        ],
    )
    def test_0(self, entrance, expected):
        """Unittest."""
        assert pkg.running(**entrance) == expected
