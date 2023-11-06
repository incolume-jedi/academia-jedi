"""Solving question."""
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
