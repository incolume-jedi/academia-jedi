"""Estudo com aiohttp.

https://docs.aiohttp.org/en/stable/

"""

# ruff: noqa: D103, SIM117

import asyncio

import aiohttp
from icecream import ic


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            ic('Status:', response.status)
            ic('Content-type:', response.headers['content-type'])

            html = await response.text()
            ic(f'Body: {html[:15]} ...')


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
