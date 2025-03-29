"""Estudos com aiohttp."""

import asyncio
from collections.abc import Coroutine

from aiohttp import ClientSession
from icecream import ic


async def fetch(url: str, session: ClientSession) -> Coroutine:
    """Fetch session.

    Args:
        url (str): _description_
        session (ClientSession): _description_

    Returns:
        Coroutine: _description_
    """
    async with session.get(url) as response:
        return await response.read()


async def run(r: int) -> None:
    """Run it.

    Args:
        r (int): limit of range;
    """
    url = 'http://httpbin.org/delay/{}'
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        ic(responses)


def print_responses(result: str) -> None:
    """Print responses.

    Args:
        result (str): _description_
    """
    ic(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(4))
    loop.run_until_complete(future)
