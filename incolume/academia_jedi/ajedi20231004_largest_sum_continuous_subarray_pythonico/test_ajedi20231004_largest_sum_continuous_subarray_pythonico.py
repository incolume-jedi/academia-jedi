import pytest

from incolume.academia_jedi.ajedi20231004_largest_sum_continuous_subarray_pythonico import (
    max_sub_array_sum,
    max_sub_array_sum1,
    max_subarray_sum,
)

__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    def test_something(self, capsys):
        entrance = [-2, -3, 4, -1, -2, 1, 5, -3]
        result = max_sub_array_sum(entrance, len(entrance))
        output, _ = capsys.readouterr()
        assert result == (
            'Maximum contiguous sum is 7,\n'
            'Starting Index 2,\nEnding Index 6'
        )
        assert output == ''

    def test_max_sub_array_sum_1(self, capsys):
        a = [-2, -3, 4, -1, -2, 1, 5, -3]
        result = max_sub_array_sum1(a)
        output, _ = capsys.readouterr()
        assert output == ''
        assert result == 7


    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ([-1, -2, -3, -4], 0),
            ([-10, -2, -3, -1], 0),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
            ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([10, -11, 2, 3, 4, 5, -5, 6, 7, -50, 8, -7, 9], 22),
            ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
        ],
    )
    def test_max_subarray_sum(self, entrance, expected):
        """Test de max."""
        assert max_subarray_sum(entrance) == expected
