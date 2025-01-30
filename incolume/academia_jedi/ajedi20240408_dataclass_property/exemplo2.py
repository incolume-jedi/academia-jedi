"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from dataclasses import dataclass, field
from typing import Union

# ruff: noqa: S101 T201 ERA001 PLR2004


@dataclass
class Vehicle:
    """Vehicle class."""

    wheels: Union[int, str] = 0
    _wheels: int | str = field(default='', init=False, repr=False)

    # Uncomment the field below if you want to make your IDE a bit happier.
    #   _wheels: int = field(repr=False, init=False)

    @property
    def wheels(self) -> int:
        """Property."""
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: Union[int, str]) -> None:
        """Property setter."""
        self._wheels = 0 if isinstance(wheels, property) else int(wheels)


def run():
    """Run it."""
    v = Vehicle(wheels='3')

    print(v)
    # prints:
    #   Vehicle(wheels=3)

    # This works as expected!
    assert v.wheels == 3, 'The constructor should use our setter method'

    # So does this...
    v.wheels = '6'
    assert v.wheels == 6

    # But it ends up failing here, because our `setter` method is passed
    # in a `property` object by the `dataclasses` decorator (as no initial
    # value is explicitly set)
    v = Vehicle()

    # We unfortunately won't get here :(
    print(v)


if __name__ == '__main__':
    run()
