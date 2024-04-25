from dataclasses import dataclass, field


class Pencil:
    def __init__(self, count):
        self.__counter = count

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, count):
        self.__counter = count

    @counter.getter
    def counter(self):
        return self.__counter


@dataclass
class Pen:
    """Pen class."""

    def __post_init__(self):
        """Post init."""
