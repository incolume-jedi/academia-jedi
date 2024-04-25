import asyncio
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
