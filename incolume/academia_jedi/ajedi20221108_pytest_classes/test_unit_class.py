"""test_class_parametrization.py"""
import inspect

import pytest


@pytest.mark.parametrize(
    'param1,param2',
    [
        ('a', 'b'),
        ('c', 'd'),
    ],
)
class TestGroup:
    """A class with common parameters, `param1` and `param2`."""

    @pytest.fixture
    def fixt(self):
        """This fixture will only be available within the scope of TestGroup"""
        return 123

    def test_one(self, param1, param2, fixt):
        print(f'\n{inspect.stack()[0][3]} {param1} {param2} {fixt}')

    def test_two(self, param1, param2):
        print(f'\n{inspect.stack()[0][3]} {param1} {param2}')
