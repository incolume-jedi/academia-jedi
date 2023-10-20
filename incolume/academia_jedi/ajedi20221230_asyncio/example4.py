"""
tarefas comcorrentes
"""

import asyncio
import logging
from inspect import stack

import aiohttp

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


async def tarefa(number: int, url):
    logging.debug('inicio: %s%s', stack()[0][3], number)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            print((await response.text()))
    logging.debug('fim: %s%s', stack()[0][3], number)


async def main():
    urls = [
        'http://httpbin.org/links/1/1',
        'http://httpbin.org/links/2/2',
        'http://httpbin.org/links/3/3',
        'http://httpbin.org/links/4',
    ]
    tasks = [
        asyncio.create_task(tarefa(seq, url)) for seq, url in enumerate(urls)
    ]
    results = await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':  # pragma: no cover
    asyncio.run(main())
