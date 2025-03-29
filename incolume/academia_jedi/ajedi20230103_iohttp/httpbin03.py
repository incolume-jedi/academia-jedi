"""Estudo com consumo de API assincrono."""

import asyncio
import time

import aiohttp
from icecream import ic

start_time = time.time()


async def get_uuid(session: aiohttp.ClientSession, url: str) -> str:
    """Get uuid.

    Args:
        session (aiohttp.ClientSession): _description_
        url (str): _description_

    Returns:
        str: _description_
    """
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    """Main."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 151):
            url = f'https://rickandmortyapi.com/api/episode/{number}'
            tasks.append(asyncio.ensure_future(get_uuid(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            ic(pokemon)


if __name__ == '__main__':
    asyncio.run(main())
    ic('--- %s seconds ---' % (time.time() - start_time))
