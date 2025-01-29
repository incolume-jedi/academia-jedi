from collections.abc import Sequence
from typing import overload

__author__ = '@britodfbr'  # pragma: no cover


@overload
def process(response: None) -> None: ...


@overload
def process(response: int) -> tuple[int, str]: ...


@overload
def process(response: bytes) -> str: ...


@overload
def process(response: float) -> float: ...


def process(response):
    """Process."""
    return f'{type(response)}'


@overload
def double(input_: int) -> int: ...


@overload
def double(input_: Sequence[int]) -> list[int]: ...


def double(input_: int | Sequence[int]) -> int | list[int]:
    if isinstance(input_, Sequence):
        return [i * 2 for i in input_]
    return input_ * 2
