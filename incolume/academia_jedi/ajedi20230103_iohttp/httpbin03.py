import aiohttp
import asyncio
import time

start_time = time.time()


async def get_uuid(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://rickandmortyapi.com/api/episode/{number}'
            tasks.append(asyncio.ensure_future(get_uuid(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


asyncio.run(main())
print('--- %s seconds ---' % (time.time() - start_time))
