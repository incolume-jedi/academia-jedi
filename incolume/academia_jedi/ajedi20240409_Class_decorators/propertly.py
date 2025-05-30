"""Class decorators."""

from dataclasses import dataclass


class Pencil:
    """Pencil class."""

    def __init__(self, count):
        """Initializer."""
        self.__counter = count

    @property
    def counter(self):
        """Counter property."""
        return self.__counter

    @counter.setter
    def counter(self, count):
        """Counter property setter."""
        self.__counter += count

    @counter.getter
    def counter(self):
        """Counter property getter."""
        return self.__counter


@dataclass
class Pen:
    """Pen class."""

    def __post_init__(self):
        """Post init."""
