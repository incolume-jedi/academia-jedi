"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from dataclasses import dataclass, field
from typing import Union


@dataclass
class Vehicle:
    wheels: Union[int, str] = field(default=0)

    # Uncomment the field below if you want to make your IDE a bit happier.
    # Remember to set an initial value `x` as needed, via `default=x`.
    _wheels: int = field(init=False, repr=False)

    @property
    def wheels(self) -> int:
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: Union[int, str]):
        # self._wheels = int(wheels)
        self._wheels = (
            0 if isinstance(wheels, property) else max(int(wheels), 1)
        )

    def __post_init__(self):
        """Post init."""


if __name__ == '__main__':
    v = Vehicle(wheels='3')

    print(v)
    # prints:
    #   Vehicle(wheels=3)

    # This works as expected!
    assert v.wheels == 3, 'The constructor should use our setter method'

    # So does this...
    v.wheels = '6'
    assert v.wheels == 6

    # Our `setter` method is still passed in a `property` object, but the
    # updated `setter` method (added by the metaclass) is now able to
    # automatically check for this value, and update `_wheels` with the
    # default value for the annotated type.
    v = Vehicle()

    # We've successfully managed to handle the edge case above!
    print(v)
