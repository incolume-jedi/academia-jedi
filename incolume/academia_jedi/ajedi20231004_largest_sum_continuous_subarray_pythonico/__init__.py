# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import sys
from sys import maxsize


def maxSubArraySum(a, size):
    """
    Function to find the maximum contiguous subarray
    and print its starting and end index
    """

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print('Maximum contiguous sum is %d' % (max_so_far))
    print('Starting Index %d' % (start))
    print('Ending Index %d' % (end))


def maxSubArraySum1(arr):
    # Base case: when there is only one element in the array
    if len(arr) == 1:
        return arr[0]

    # Recursive case: divide the problem into smaller sub-problems
    m = len(arr) // 2

    # Find the maximum subarray sum in the left half
    left_max = maxSubArraySum1(arr[:m])

    # Find the maximum subarray sum in the right half
    right_max = maxSubArraySum1(arr[m:])

    # Find the maximum subarray sum that crosses the middle element
    left_sum = -sys.maxsize - 1
    right_sum = -sys.maxsize - 1
    sum = 0

    # Traverse the array from the middle to the right
    for i in range(m, len(arr)):
        sum += arr[i]
        right_sum = max(right_sum, sum)

    sum = 0

    # Traverse the array from the middle to the left
    for i in range(m - 1, -1, -1):
        sum += arr[i]
        left_sum = max(left_sum, sum)

    cross_max = left_sum + right_sum

    # Return the maximum of the three subarray sums
    return max(cross_max, max(left_max, right_max))


if __name__ == '__main__':  # pragma: no cover
    # Driver program to test maxSubArraySum
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    maxSubArraySum(a, len(a))

    # Example usage
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_sum = maxSubArraySum1(arr)
    print('Maximum contiguous sum is', max_sum)
