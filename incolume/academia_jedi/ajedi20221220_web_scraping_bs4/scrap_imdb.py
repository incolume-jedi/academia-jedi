"""Baseado em [Web Scraping in Python using Beautiful Soup |

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
Writing a Python program to Scrape IMDB website]
(https://www.youtube.com/watch?v=LCVSmkyB4v8).
"""

import logging

import openpyxl
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

excel = openpyxl.Workbook()
logging.debug(excel.sheetnames)
sheet = excel.active
sheet.title = 'Top rate movies'
logging.debug(excel.sheetnames)
sheet.append(
    ['Movie Rank', 'Movie name', 'Year of release', 'IMDB Ranking', 'Poster'],
)

url = 'https://www.imdb.com/chart/top'
try:
    req = requests.get(url)
    req.raise_for_status()

    soup = BeautifulSoup(req.content, 'html.parser')
    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    logging.debug('%s; %s', len(movies), movies)
    for movie in movies:
        name = movie.find('td', class_='titleColumn').a.text
        rank = (
            movie.find('td', class_='titleColumn')
            .get_text(strip=True)
            .split('.')[0]
        )
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        poster = movie.find('td', class_='posterColumn').img['src']
        logging.debug(
            '{ rank: %s, name: %s,year: %s, rating: %s, poster: %s}',
            rank,
            name,
            year,
            rating,
            poster,
        )
        sheet.append([rank, name, year, rating, poster])
except requests.exceptions.HTTPError as e:
    logging.exception(e)

excel.save('IMDB_Movies_Ratings.xlsx')
