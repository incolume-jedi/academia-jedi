"""Test Reload runtime."""

from pathlib import Path
from typing import NoReturn
import pytest
from importlib import reload
from icecream import ic


class TestReloadRuntime:
    """ReloadRuntime class."""

    @classmethod
    def setup_class(cls):
        """Setup class."""
        ic('criação do modulo fake.')
        cls.file = Path(__file__).parent.joinpath('other.py')
        with cls.file.open('w') as f:
            f.write('"""Fake module."""')

        import incolume.academia_jedi.ajedi20250416_reload_runtime.other as pkg

        cls.pkg = pkg

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        ic('Descarte do modulo fake.')
        cls.file.unlink(missing_ok=True)

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
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
        """Unittest para nomes existentes no módulo."""
        try:
            assert getattr(self.pkg, entrance) == expected
        except AttributeError:
            with pytest.raises(**expected):
                getattr(self.pkg, entrance)

    def test_runtime(self) -> NoReturn:
        """Criação e carregamento de __version__ em runtime."""
        expected = '0.0.1'
        with self.file.open('a') as f:
            f.write(f"\n\n__version__ = '{expected}'")
        reload(self.pkg)
        assert self.pkg.__version__ == expected
