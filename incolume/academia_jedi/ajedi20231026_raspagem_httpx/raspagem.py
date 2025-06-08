"""Modulo para raspagem web com httpx."""

# ruff: noqa: BLE001

import logging
from pathlib import Path
from tempfile import gettempdir

import httpx
from bs4 import BeautifulSoup
from icecream import ic


def get_content(url: str) -> list:
    """Donwload content web."""
    result = ['']
    try:
        req = httpx.get(url)
        content: str = req.text
        soup = BeautifulSoup(content, 'html5lib')
        result = soup.select_one(
            'div.corpo_texto_noticia',
        ).contents  # type: ignore[union-attr]
        return [
            line.strip() for line in result if line and isinstance(line, str)
        ]
    except Exception:
        return result


def write_content(fout: Path, content: list) -> bool:
    """Escrita de conteúdo raspado."""
    logging.debug(ic(fout, content))
    soup = BeautifulSoup('', 'html5lib')
    for line in content:
        logging.debug(ic(line))
        if line:
            p = soup.new_tag('p')
            p.string = line
            soup.html.body.append(p)  # type: ignore[union-attr]
    fout.write_bytes(soup.prettify(encoding='utf-8'))
    return True


def run() -> None:
    """Run it."""
    url = (
        'https://www.diariodasleis.com.br/legislacao/'
        'federal/exibe_artigo.php?ifl=203526'
    )
    file = Path(gettempdir()) / 'dim18320616-001.html'

    content = get_content(url)
    write_content(file, content)


if __name__ == '__main__':  # pragma: no cover
    run()
