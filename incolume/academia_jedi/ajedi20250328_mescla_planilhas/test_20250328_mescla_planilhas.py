"""Test module."""

import inspect
from pathlib import Path
import shutil
from tempfile import gettempdir
from typing import NoReturn
import incolume.academia_jedi.ajedi20250328_mescla_planilhas as pkg


class TestMergeSheet:
    """Test case."""

    dout = Path(gettempdir(), inspect.stack()[0][3])

    def setup_method(self, method):
        """Setup method."""
        self.fout = self.dout.joinpath(method.__name__, 'merged.csv')
        self.fout.parent.mkdir(parents=True, exist_ok=True)

    def teardown_method(self):
        """Teardown."""
        shutil.rmtree(self.fout.parent, ignore_errors=True)

    def test_correct_path(self) -> NoReturn:
        """Test unit."""
        assert pkg.path.is_dir()

    def test_show_files(self, capsys) -> NoReturn:
        """Unittest."""
        pkg.show_files_dir(pkg.path)
        capture = capsys.readouterr()
        assert capture.out

    def test_0(self) -> NoReturn:
        """Unittest."""
        assert pkg.merge_planilhas(pkg.path, fout=self.fout).is_file()
