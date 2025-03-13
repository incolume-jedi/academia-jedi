"""Estudo compactação com shutil."""

from pathlib import Path
import tempfile
from inspect import stack
from typing import ClassVar


class TestCompactShutil:
    """Test case."""

    PATH: ClassVar[Path] = Path(tempfile.gettempdir()) / stack()[0][3]

    def test_0(self):
        """Unit test."""
        path = self.PATH / stack()[0][3]
        path.mkdir(parents=True, exist_ok=True)
        [path.joinpath(y) for y in [f'test{x:02}' for x in range(10)]]
        assert self.PATH.as_posix() == ''

    def test_1(self):
        """Unit test."""
        assert self.PATH is None
