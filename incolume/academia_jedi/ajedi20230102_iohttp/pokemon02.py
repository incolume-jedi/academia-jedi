"""Estudos com aiohttp."""

import asyncio
import time

import aiohttp
from icecream import ic

start_time = time.time()


async def main():
    """Main."""
    async with aiohttp.ClientSession() as session:
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url, ssl=False) as resp:
                pokemon = await resp.json()
                ic(pokemon['name'])


if __name__ == '__main__':
    asyncio.run(main())
    ic('--- %s seconds ---' % (time.time() - start_time))
