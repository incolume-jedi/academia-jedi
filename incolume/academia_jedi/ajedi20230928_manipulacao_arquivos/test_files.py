import incolume.academia_jedi.ajedi20230928_manipulacao_arquivos.files as pkg
import pytest
from pathlib import Path
from tempfile import NamedTemporaryFile
from functools import partialmethod


class TestCase:
    """Caso de teste."""
    @pytest.fixture
    def nfile(self, ext: str = '') -> Path:
        """Arquivo temp."""
        ext = f'.{ext.strip(".")}' if ext else '.txt'
        return Path(NamedTemporaryFile(prefix='AJEDI-', suffix=ext).name)

    def test_content_origin(self):
        """Teste para conteúdo de origem."""
        assert isinstance(pkg.CONTENT, list)

    @pytest.mark.parametrize(
        'function',
        [getattr(pkg, func) for func in dir(pkg) if func.startswith('exemplo')]
    )
    def test_files_examples_exists(self, nfile, function):
        """Testar se arquivo gerado existe."""
        function(nfile)
        assert nfile.is_file()

    def test_files_exemplo1_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo01(nfile)
        assert nfile.read_bytes()

    def test_files_exemplo2_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo02(nfile)
        assert nfile.read_text()

    def test_files_exemplo3_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo03(nfile)
        assert nfile.read_text()

    def test_files_exemplo4_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo04(nfile)
        assert nfile.is_file()

    def test_files_exemplo5_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo05(nfile)
        assert nfile.is_file()

    def test_files_exemplo6_csv(self, nfile):
        """Teste para arquivos CSV."""

    def test_files_exemplo7_csv(self):
        """Teste para arquivos CSV."""

    def test_files_exemplo8_csv(self):
        """Teste para arquivos CSV."""

    def test_files_exemplo9_csv(self):
        """Teste para arquivos CSV."""

    def test_files_exemplo10_csv(self):
        """Teste para arquivos CSV."""

    def test_files_exemplo11_json(self):
        """Teste para arquivos JSON."""

    def test_files_exemplo12_json(self):
        """Teste para arquivos JSON."""

    def test_files_exemplo13_xlsx(self):
        """Teste para arquivos XLSX."""

