"""Solution for module."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Final

import httpx
import pandas as pd
import yaml
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


def _get_cities_dataframe(file: Path | None = None) -> pd.DataFrame:
    """Get cities."""
    file = file or cidades_file_txt
    logging.debug(ic(file))
    dataframe = pd.read_csv(file, sep=';', names=['cod', 'cidade'])
    dataframe[['municipio', 'uf']] = (
        dataframe.cidade.str.replace(')', '')
        .str.replace(' (', ', ')
        .str.split(', ')
        .tolist()
    )
    return dataframe


def pandas2yaml(dataframe: pd.DataFrame, filename: Path | None = None) -> Path:
    """Pandas to YAML file."""
    filename = filename or Path('output.yaml')
    filename = filename.with_suffix('.yaml')
    data = yaml.dump(dataframe.to_dict(orient='records', sort_keys=False))
    logging.debug(ic(data))
    with filename.open('w') as f:
        yaml.dump(data, f, default_flow_style=False)


def get_cities(file: Path | None = None) -> list[str]:
    """Get cities."""
    dataframe = _get_cities_dataframe(file)
    logging.debug(ic(dataframe))
    return dataframe.municipio.tolist()
