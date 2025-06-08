"""Testing it."""

from inspect import stack
from pathlib import Path
from tempfile import NamedTemporaryFile

from incolume.academia_jedi.ajedi20231026_raspagem_httpx.raspagem import (
    get_content,
    write_content,
)

# ruff: noqa: SIM115


# ruff: noqa: SIM115
class TestRapagem:
    """Testcase."""

    url = 'https://www.diariodasleis.com.br/legislacao/federal/exibe_artigo.php?ifl=203526'

    def test_get_content_ifcontent(self) -> None:
        """Testar se tem conteúdo."""
        result = get_content(self.url)
        assert result is not None

    def test_get_content_type_list(self) -> None:
        """Testar se tem conteúdo."""
        result = get_content(self.url)
        assert isinstance(result, list)
        assert all(isinstance(x, str) for x in result)

    def test_write_content(self) -> None:
        """Testar write_content."""
        filename: Path = Path(NamedTemporaryFile(prefix=stack()[0][3]).name)
        write_content(filename, get_content(self.url))
        assert filename.is_file()
