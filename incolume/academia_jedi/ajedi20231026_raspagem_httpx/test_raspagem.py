from incolume.academia_jedi.ajedi20231026_raspagem_httpx.raspagem import get_content, write_content


def test_get_content():
    """Test this function."""
    entrance = 'https://www.diariodasleis.com.br/legislacao/federal/exibe_artigo.php?ifl=203526'
    expected = ''
    assert get_content(entrance)