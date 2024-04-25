import asyncio

import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url, ssl=False) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])


asyncio.run(main())
