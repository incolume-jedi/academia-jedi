"""
tarefas comcorrentes
"""

import aiohttp
import asyncio
import logging
from inspect import stack

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
    results = await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':  # pragma: no cover
    asyncio.run(main())
