"""Module."""

# ruff: noqa: T201 PLR2004

from collections.abc import Container

array = [14, 6, 5, 20, 2]


def qsort(array: Container[int]) -> list[int]:
    """Algoritmo quick sort."""
    if len(array) < 2:
        return array

    pivot = array[0]

    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]
    return [*qsort(left), pivot, *qsort(right)]


if __name__ == '__main__':
    print(f'original array: {array}')  # out: [14,6,5,20,2]
    print(f'ordered array: {qsort(array)}')  # out: [2,5,6,14,20]
