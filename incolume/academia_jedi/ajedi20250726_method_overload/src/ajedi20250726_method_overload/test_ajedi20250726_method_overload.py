"""Test for ajedi20250726_method_overload module."""

from . import Negator
import pytest
from dataclasses import dataclass, field
from decimal import Decimal
from icecream import ic


@dataclass
class Entrance:
    """Data class for entrance parameters."""

    value: object
    type: str = ''
    exception: dict = field(default_factory=dict)


class TestNegator:
    """Test cases for the Negator class."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                Entrance(5, 'Negation of a un integer'),
                -5,
                id='negate_int',
                marks=[],
            ),
            pytest.param(
                Entrance(-3.14, 'negation of a float'),
                3.14,
                id='negate_float',
                marks=[],
            ),
            pytest.param(
                Entrance(Decimal('-2.5'), 'negation of a Decimal'),
                Decimal('2.5'),
                id='negate_decimal',
                marks=[],
            ),
            pytest.param(
                Entrance(value=True, type='Negation of boolean'),
                False,
                id='negate_true',
                marks=[],
            ),
            pytest.param(
                Entrance(value=False, type='Negation of boolean'),
                True,
                id='negate_false',
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'string',
                    'NotImplementedError is raised for unsupported types',
                    {
                        'expected_exception': NotImplementedError,
                        'match': 'Cannot negate a (str value: string)',
                    },
                ),
                None,
                id='NotImplementedError',
                marks=[],
            ),
        ],
    )
    def test_negate(self, entrance, expected):
        """Test negation of an integer."""
        ic(entrance, expected)

        if entrance.exception:
            with pytest.raises(**entrance.exception):
                Negator.neg(entrance.value)
        else:
            assert Negator.neg(entrance.value) == expected, (
                f'{entrance.msg} failed'
            )

    def test_negate_not_implemented(self):
        """Test that ."""
