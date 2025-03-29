"""Estudos com aiohttp."""

import asyncio
import time

import aiohttp
from icecream import ic

start_time = time.time()


async def get_pokemon(session: aiohttp.ClientSession, url: str) -> str:
    """Get pokemon assincrono."""
    async with session.get(url, ssl=False) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def main():
    """Main."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            ic(pokemon)


if __name__ == '__main__':
    asyncio.run(main())
    ic('--- %s seconds ---' % (time.time() - start_time))
