from incolume.academia_jedi.ajedi20231004_largest_sum_continuous_subarray_pythonico import (
    max_sub_array_sum,
    max_sub_array_sum1,
)

__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    def test_something(self, capsys):
        a = [-2, -3, 4, -1, -2, 1, 5, -3]
        max_sub_array_sum(a, len(a))
        output, _ = capsys.readouterr()
        assert output == (
            'Maximum contiguous sum is 7\n'
            'Starting Index 2\nEnding Index 6\n'
        )

    def test_max_sub_array_sum_1(self, capsys):
        a = [-2, -3, 4, -1, -2, 1, 5, -3]
        result = max_sub_array_sum1(a)
        output, _ = capsys.readouterr()
        assert output == ''
        assert result == 7
