"""Exemplo assincrono."""

import asyncio
from itertools import starmap
from time import perf_counter

servers = (f'192.168.1.{x}' for x in range(1, 100))


async def simulation_ssh_connection(position, ip):
    await asyncio.sleep(1)
    print(f'{position} - {ip}')


def run():
    start_time = perf_counter()
    loop = asyncio.get_event_loop()
    tasks = list(starmap(simulation_ssh_connection, enumerate(servers, 1)))
    loop.run_until_complete(asyncio.wait(tasks))
    print(f'Tempo de execução: {perf_counter() - start_time}s')
    loop.close()


if __name__ == '__main__':  # pragma: no cover
    run()
