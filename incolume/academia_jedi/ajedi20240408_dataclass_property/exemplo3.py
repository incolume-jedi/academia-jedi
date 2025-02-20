"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

__author__ = '@britodfbr'  # pragma: no cover
from dataclasses import dataclass
from typing import Union

from dataclass_wizard import property_wizard

# ruff: noqa: S101 T201 ERA001 PLR2004


@dataclass
class Vehicle(metaclass=property_wizard):
    """Vehicle class."""

    wheels: Union[int, str] = None
    # Uncomment the field below if you want to make your IDE a bit happier.
    # Remember to set an initial value `x` as needed, via `default=x`.
    #   _wheels: int = field(init=False)

    @property
    def wheels(self) -> int:
        """Property."""
        return self._wheels

    @wheels.setter
    def wheels(self, wheels: Union[int, str]) -> None:
        """Property setter."""
        self._wheels = int(wheels)


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
