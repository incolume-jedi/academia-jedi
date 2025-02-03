"""Solving question."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

# !/usr/bin/env python
__author__ = '@britodfbr'  # pragma: no cover

import logging
import sys
from sys import maxsize


def max_sub_array_sum(array: list, size: int) -> str:
    """Function to find the maximum contiguous subarray.

    and print its starting and end index.
    """
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(size):
        max_ending_here += array[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return (
        f'Maximum contiguous sum is {max_so_far},\n'
        f'Starting Index {start},\n'
        f'Ending Index {end}'
    )


def max_sub_array_sum1(arr: list) -> int:
    """Max subarray sum."""
    # Base case: when there is only one element in the array
    if len(arr) == 1:
        return arr[0]

    # Recursive case: divide the problem into smaller sub-problems
    m = len(arr) // 2

    # Find the maximum subarray sum in the left half
    left_max = max_sub_array_sum1(arr[:m])

    # Find the maximum subarray sum in the right half
    right_max = max_sub_array_sum1(arr[m:])

    # Find the maximum subarray sum that crosses the middle element
    left_sum = -sys.maxsize - 1
    right_sum = -sys.maxsize - 1
    sum_value = 0

    # Traverse the array from the middle to the right
    for i in range(m, len(arr)):
        sum_value += arr[i]
        right_sum = max(right_sum, sum_value)

    sum_value = 0

    # Traverse the array from the middle to the left
    for i in range(m - 1, -1, -1):
        sum_value += arr[i]
        left_sum = max(left_sum, sum_value)

    cross_max = left_sum + right_sum

    # Return the maximum of the three subarray sums
    return max(cross_max, left_max, right_max)


def max_subarray_sum(array: list) -> int:
    """Max subarray sum."""
    result, soma = 0, 0
    for num in array:
        soma += num
        soma = max(0, soma)
        result = max(result, soma)

    return result


if __name__ == '__main__':  # pragma: no cover
    # Driver program to test max_sub_array_sum
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_sub_array_sum(a, len(a))

    # Example usage
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_sum = max_sub_array_sum1(arr)
    logging.info('Maximum contiguous sum is %s', max_sum)
