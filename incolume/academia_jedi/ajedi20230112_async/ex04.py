"""Exemplo assincrono."""

import asyncio
from itertools import starmap
from time import perf_counter

servers = (f'192.168.1.{x}' for x in range(1, 101))


async def simulation_ssh_connection(position, ip):
    await asyncio.sleep(1)
    print(f'{position} - {ip}')


async def run():
    start_time = perf_counter()
    tasks = list(starmap(simulation_ssh_connection, enumerate(servers, 1)))

    results = await asyncio.gather(*tasks)
    print(f'Tempo de execução: {perf_counter() - start_time}s')
    return results


if __name__ == '__main__':  # pragma: no cover
    asyncio.run(run())
