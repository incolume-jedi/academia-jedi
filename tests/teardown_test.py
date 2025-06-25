"""Test examples."""

from inspect import stack
from icecream import ic
import pytest


class TestClass:
    """TestClass.

    Exemplo utilizando classe para configuração de setup e teardown.
    """

    @classmethod
    def setup_class(cls):
        """Setup class."""
        ic()
        ic(f'starting class {cls.__name__} execution')

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        ic()
        ic(f'finishing class {cls.__name__} execution')

    def setup_method(self, method):
        """Setup method."""
        ic()
        ic(f'starting execution ({method}) of {stack()[0][3]}')

    def teardown_method(self, method):
        """Teardown method."""
        ic()
        ic(f'finishing execution ({method}) of {stack()[0][3]}')

    def test_tc1(self, capsys):
        """Test case."""
        output = capsys.readouterr()
        assert output.out == ''

    def test_tc2(self):
        """Test case."""
        assert True


@pytest.fixture
def resource():
    """TestClass.

    Exemplo sem classe para configuração de setup e teardown.
    """
    ic('setup')
    yield 'resource'
    ic('teardown')


class TestResource:
    """Test class."""

    def test_that_depends_on_resource(self, resource):
        """Unittest."""
        ic(f'testing {resource}')
