"""Test."""

from typing import NoReturn
import pytest
from . import qsort, array


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        pytest.param(array, [2, 5, 6, 14, 20]),
        pytest.param(
            [21, 7, 14, 6, 5, 20, 12, 10],
            [5, 6, 7, 10, 12, 14, 20, 21],
        ),
        pytest.param(
            [99, 14, 6, -273.15, 55, -459.67, 5, 20, 2, -1],
            [-459.67, -273.15, -1, 2, 5, 6, 14, 20, 55, 99],
        ),
    ],
)
def test_quicksort(entrance, expected) -> NoReturn:
    """Unittest."""
    assert qsort(entrance) == expected
