"""tarefas comcorrentes."""

import asyncio
import logging
from inspect import stack

import aiohttp

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


async def get_page(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.text()


async def tarefa(number: int, url):
    logging.debug('inicio: %s%s', stack()[0][3], number)
    async with aiohttp.ClientSession() as session:
        logging.debug('fim: %s%s', stack()[0][3], number)
        return await get_page(session, url)


async def main():
    urls = [
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
    ]
    tasks = [
        asyncio.create_task(tarefa(seq, url))
        for seq, url in enumerate(urls, start=1)
    ]
    return await asyncio.gather(*tasks)


def run():
    print(asyncio.run(main()))


if __name__ == '__main__':  # pragma: no cover
    run()
