"""
tarefas comcorrentes
"""


import asyncio
import logging
from inspect import stack

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


async def t1():
    logging.debug('inicio: %s', stack()[0][3])
    await asyncio.sleep(1.8)
    logging.debug('fim: %s', stack()[0][3])


async def t2():
    logging.debug('inicio: %s', stack()[0][3])
    await asyncio.sleep(0.6)
    logging.debug('fim: %s', stack()[0][3])


async def main():
    task1 = asyncio.create_task(t1())
    task2 = asyncio.create_task(t2())
    await task1
    await task2


if __name__ == '__main__':  # pragma: no cover
    asyncio.run(main())
