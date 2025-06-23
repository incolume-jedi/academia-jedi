"""Test for this module."""

from incolume.academia_jedi.ajedi20250620_py_script import iris


class TestPythonScript:
    """Class TestPythonScript."""

    def test_uci_dataset(self):
        """Unittest."""
        assert iris.UCIDataset.IRIS == 53  # noqa: PLR2004
