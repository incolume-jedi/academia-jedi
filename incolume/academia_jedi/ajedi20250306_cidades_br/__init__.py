"""Solution for module."""

import logging
from pathlib import Path
from typing import Final

import httpx
import pandas as pd
from bs4 import BeautifulSoup
from icecream import ic

mg: Final[list[str]] = [
    'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Minas_Gerais',
]
sp: Final[list[str]] = [
    'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_S%C3%A3o_Paulo',
    'https://www.al.sp.gov.br/documentacao/municipios-paulistas/',
    'https://www.al.sp.gov.br/arquivos/documentacao/municipios_paulistas/',
]

cidades_file_txt: Final[Path] = (
    Path(__file__).parents[3].joinpath('data_files', 'txt', 'cidades_br.txt')
)


def get_cities_sp(url: str = '') -> list[str]:
    """Get cities.

    By default get cities from Assembléia Legislativa.
    """
    url = url or sp[2]
    cities: list[str] = []
    response = httpx.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')

    cities.extend(
        city.get_text() for city in soup.select('a[class="linkCidade"]')
    )
    return cities


def get_cities(file: Path | None = None) -> pd.DataFrame:
    """Get cities."""
    file = file or cidades_file_txt
    logging.debug(ic(file))
    return pd.read_csv(file, sep=';', names=['cod', 'cidade'])
