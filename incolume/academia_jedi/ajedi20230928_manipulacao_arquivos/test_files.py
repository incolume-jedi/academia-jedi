import incolume.academia_jedi.ajedi20230928_manipulacao_arquivos.files as pkg
import pytest
from pathlib import Path
from tempfile import NamedTemporaryFile


class TestCase:
    """Caso de teste."""
    def test_content_origin(self):
        """Teste para conteúdo de origem."""
        assert isinstance(pkg.CONTENT, list)

    @pytest.fixture
    def nfile(self, ext: str = '') -> Path:
        """Arquivo temp."""
        ext = f'.{ext.strip(".")}' if ext else '.txt' 
        return Path(NamedTemporaryFile(prefix='AJEDI-', suffix=ext).name)

    def test_files_exemplo1_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo1(nfile)
        assert nfile.read_text()
    
    def test_files_exemplo2_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo2(nfile)
        assert nfile.is_file()

    def test_files_exemplo3_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo3(nfile)
        assert nfile.is_file()
    
    def test_files_exemplo4_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo4(nfile)
        assert nfile.is_file()
    
    def test_files_exemplo5_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo5(nfile)
        assert nfile.is_file()

    def test_files_exemplo6_csv(self):
        """Teste para arquivos CSV."""

    def test_files_exemplo1_json(self):
        """Teste para arquivos JSON."""