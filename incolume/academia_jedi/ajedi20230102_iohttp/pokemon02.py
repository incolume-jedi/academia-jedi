import asyncio
import time

import aiohttp

start_time = time.time()


async def main():

    async with aiohttp.ClientSession() as session:

        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url, ssl=False) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


asyncio.run(main())
print('--- %s seconds ---' % (time.time() - start_time))
