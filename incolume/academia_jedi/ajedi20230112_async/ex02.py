"""Exemplo assincrono."""

import asyncio
from time import perf_counter

servers = (f'192.168.1.{x}' for x in range(1, 100))


async def simulation_ssh_connection(position, ip):
    await asyncio.sleep(1)
    print(f'{position} - {ip}')


def run():
    start_time = perf_counter()
    loop = asyncio.get_event_loop()
    tasks = [
        simulation_ssh_connection(position, ip)
        for position, ip in enumerate(servers, 1)
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('Tempo de execução: {}s'.format(perf_counter() - start_time))
    loop.close()


if __name__ == '__main__':  # pragma: no cover
    run()
