"""aiohttp + asyncio.

https://youtu.be/nFn4_nA_yk8
https://youtu.be/lUwZ9rS0SeM
"""
import asyncio
import logging

import aiohttp
from bs4 import BeautifulSoup


async def get_page(session, url):
    async with session.get(url, ssl=False) as r:
        return await r.text()


async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    return await asyncio.gather(*tasks)


async def main(urls):
    async with aiohttp.ClientSession() as session:
        return await get_all(session, urls)


def parse(results):
    for html in results:
        soup = BeautifulSoup(html, 'html.parser')
        try:
            print(soup.find('form', {'class': 'form-horizontal'}).text.strip())
        except AttributeError as e:
            logging.exception(e)


if __name__ == '__main__':
    urls = [
        'https://books.toscrape.com/catalogue/page-1.html',
        'https://books.toscrape.com/catalogue/page-2.html',
        'https://books.toscrape.com/catalogue/page-3.html',
    ]
    results = asyncio.run(main(urls))
    print(len(results))
    parse(results)
