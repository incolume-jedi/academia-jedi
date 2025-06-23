"""Test for this module."""

import pytest
from incolume.academia_jedi.ajedi20250620_py_script import iris
from typing import NoReturn


class TestPythonScript:
    """Class TestPythonScript."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('IRIS', 53),
        ],
    )
    def test_uci_dataset(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert iris.UCIDataset.__getitem__(entrance) == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('petal length', 'petal length'),
            pytest.param('PETAL_LENGTH', 'petal length'),
        ],
    )
    def test_iris_variable(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert iris.UCIDataset.__getitem__(entrance) == expected.value
