"""Testing it."""

from inspect import stack
from pathlib import Path
from tempfile import NamedTemporaryFile

from incolume.academia_jedi.ajedi20231026_raspagem_httpx.raspagem import (
    get_content,
    write_content,
)


def test_get_content_ifcontent() -> None:
    """Testar se tem conteúdo."""
    entrance = (
        'https://www.diariodasleis.com.br/legislacao/'
        'federal/exibe_artigo.php?ifl=203526'
    )
    result = get_content(entrance)
    assert result is not None


def test_get_content_type_list() -> None:
    """Testar se tem conteúdo."""
    entrance = (
        'https://www.diariodasleis.com.br/legislacao/'
        'federal/exibe_artigo.php?ifl=203526'
    )
    result = get_content(entrance)
    assert isinstance(result, list)


def test_write_content() -> None:
    """Testar write_content."""
    url = (
        'https://www.diariodasleis.com.br/legislacao/federal/'
        'exibe_artigo.php?ifl=203526'
    )
    with Path(NamedTemporaryFile(prefix=stack()[0][3]).name) as file:
        write_content(file, get_content(url))
        assert file.is_file()
