"""Estudo sobre compactação em runtime."""

import incolume.academia_jedi.ajedi20250418_filesCompactRuntime as pkg
from pathlib import Path
from tempfile import gettempdir


class TestCase:
    """TestCase."""

    def test_0(self):
        """Unittest."""
        assert pkg.set_env() == Path(gettempdir()).joinpath(
            'ajedi20250418_filesCompactRuntime', 'archives.zip',
        )
