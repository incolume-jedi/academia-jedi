"""Test Reload runtime."""

from pathlib import Path
from typing import NoReturn
import pytest
from importlib import reload


class TestReloadRuntime:
    """ReloadRuntime class."""

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.file = Path(__file__).parent.joinpath('other.py')
        with cls.file.open('w') as f:
            f.write(r'"""Fake module."""')

        import incolume.academia_jedi.ajedi20250416_reload_runtime.other as pkg

        cls.pkg = pkg

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('__doc__', 'Fake module.'),
            (
                '__version__',
                {
                    'expected_exception': AttributeError,
                    'match': "has no attribute '__version__'",
                },
            ),
        ],
    )
    def test_reaload_runtime(self, entrance, expected) -> NoReturn:
        """Unittest."""
        try:
            assert getattr(self.pkg, entrance) == expected
        except AttributeError:
            with pytest.raises(**expected):
                getattr(self.pkg, entrance)

    def test_runtime(self) -> NoReturn:
        """Unittest."""
        with self.file.open('a') as f:
            f.write('')
            f.write(r'__version__="0.0.1"')
        reload(self.pkg)
