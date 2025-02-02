import asyncio

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import inspect
import logging
from collections.abc import Iterable
from random import randint
from time import sleep

import aiohttp
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


async def get_page(session, url):
    logging.debug(url)
    try:
        sleep(randint(5, 20))
        async with session.get(url, ssl=False) as r:
            return await r.text()
    except aiohttp.client_exceptions.ClientConnectorError as e:
        logging.exception(e)


async def get_pages(session, urls):
    logging.debug(inspect.stack()[0][3])
    tasks = [asyncio.create_task(get_page(session, url)) for url in urls]
    return await asyncio.gather(*tasks)


async def main(urls, headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        return await get_pages(session, urls)


def parse(results: Iterable):
    leis = []
    for html in results:
        BeautifulSoup(html, 'html.parser')
    return leis


def run():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/108.0.0.0 Safari/537.36',
    }
    urlbase = (
        'https://www.lexml.gov.br/busca/search?'
        'f1-tipoDocumento=Legisla%C3%A7%C3%A3o;tipoDocumento=lei;'
        'tipoDocumento-exclude=decreto;f2-autoridade=Federal;'
        'year=1800;year-max=2022;smode=advanced;startDoc={}'
    )
    total_query = int(
        BeautifulSoup(requests.get(urlbase.format(1)).content, 'html.parser')
        .select_one('#itemCount')
        .text,
    )
    urls = [urlbase.format(page) for page in range(1, total_query, 20)]

    results = asyncio.run(main(urls, headers=headers))
    print(len(results))
    parse(results)


if __name__ == '__main__':
    run()
