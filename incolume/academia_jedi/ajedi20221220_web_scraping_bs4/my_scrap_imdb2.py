import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import openpyxl
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


@dataclass
class Movie:
    rank: int
    name: str
    year: int
    rating: str
    poster: str


@dataclass
class ScrapingIMDB:
    def __init__(
        self,
        url: str = '',
        excel_output: (str | Path) = '',
        sheet_title: str = '',
        columns_name: Optional[list] = None,
    ) -> None:
        self.url = url or 'https://www.imdb.com/chart/top'
        self.excel_output = Path(excel_output or 'my_IMDB_Movies_Ratings.xlsx')
        self.sheet_title = sheet_title or 'Top rate movies'
        self.columns_name = columns_name or [
            'Movie Rank',
            'Movie name',
            'Year of release',
            'IMDB Ranking',
            'Poster',
        ]
        self.req = None
        self.soup = None
        self.movies = []

    def connect(self, url: str = ''):
        url = url or self.url
        try:
            self.req = requests.get(url)
            self.req.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.exception(e)
        return self

    def get_soup(self):
        self.soup = BeautifulSoup(self.req.content, 'html.parser')
        return self

    def get_movies(self):
        movies = self.soup.find('tbody', class_='lister-list').find_all('tr')

        for movie in movies:
            obj = Movie(
                rank=movie.find('td', class_='titleColumn')
                .get_text(strip=True)
                .split('.')[0],
                name=movie.find('td', class_='titleColumn').a.text,
                year=movie.find('td', class_='titleColumn').span.text.strip(
                    '()',
                ),
                rating=movie.find(
                    'td',
                    class_='ratingColumn imdbRating',
                ).strong.text,
                poster=movie.find('td', class_='posterColumn').img['src'],
            )
            logging.debug(
                '{ rank: %s, name: %s,year: %s, rating: %s, poster: %s}',
                *obj.__dict__.values(),
            )
            self.movies.append(obj)
        logging.debug('Quantidade encontrada: %s', len(self.movies))
        return self

    def save_excel(
        self,
        *,
        excel_output: (str | Path) = '',
        columns_name: Optional[list] = None,
        **kwargs,
    ):
        if columns_name is None:
            columns_name = []
        excel_output = Path(excel_output or self.excel_output)
        excel = openpyxl.Workbook()
        logging.debug(excel.sheetnames)

        sheet = excel.active
        sheet.title = kwargs.get('sheet_title') or self.sheet_title
        logging.debug(excel.sheetnames)

        sheet.append(columns_name or self.columns_name)
        [sheet.append(list(movie.__dict__.values())) for movie in self.movies]
        excel.save(excel_output.as_posix())
        return True

    def scraping(self, **kwargs):
        url = kwargs.get('url') or self.url
        excel_output = Path(kwargs.get('excel_output') or self.excel_output)
        sheet_title = kwargs.get('sheet_title') or self.sheet_title
        columns_name = kwargs.get('columns_name') or self.columns_name
        return (
            self.connect(url)
            .get_soup()
            .get_movies()
            .save_excel(
                excel_output=excel_output,
                columns_name=columns_name,
                sheet_title=sheet_title,
            )
        )
