"""Test examples."""

from inspect import stack
from icecream import ic
import pytest

# ruff: noqa: T201


class TestClass:
    """TestClass.

    Exemplo utilizando classe para configuração de setup e teardown.
    """

    @classmethod
    def setup_class(cls):
        """Setup class."""
        ic()
        print(f'starting class {cls.__name__} execution')

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        ic()
        print(f'finishing class {cls.__name__} execution')

    def setup_method(self, method):
        """Setup method."""
        ic()
        print(f'starting execution ({method}) of {stack()[0][3]}')

    def teardown_method(self, method):
        """Teardown method."""
        ic()
        print(f'finishing execution ({method}) of {stack()[0][3]}')

    def test_tc1(self, capsys):
        """Test case."""
        output = capsys.readouterr()
        assert output.out == ''

    def test_tc2(self):
        """Test case."""
        assert True


@pytest.fixture()
def resource():
    """TestClass.

    Exemplo sem classe para configuração de setup e teardown.
    """
    print('setup')
    yield 'resource'
    print('teardown')


class TestResource:
    """Test class."""

    def test_that_depends_on_resource(self, resource):
        """Unittest."""
        print(f'testing {resource}')
