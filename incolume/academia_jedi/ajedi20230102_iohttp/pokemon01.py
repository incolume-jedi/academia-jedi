"""Estudos com aiohttp."""

import asyncio

import aiohttp
from icecream import ic


async def main():
    """Main."""
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url, ssl=False) as resp:
            pokemon = await resp.json()
            ic(pokemon['name'])


if __name__ == '__main__':
    asyncio.run(main())
