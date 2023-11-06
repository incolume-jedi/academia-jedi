"""Exemplo sincrono."""
from itertools import starmap
from time import perf_counter, sleep

servers = (f'192.168.1.{x}' for x in range(1, 100))


def simulation_ssh_connection(position, ip):
    sleep(1)
    print(f'{position} - {ip}')


def run():
    start_time = perf_counter()
    _ = list(starmap(simulation_ssh_connection, enumerate(servers, 1)))
    print(f'Tempo de execução: {perf_counter() - start_time}s')


if __name__ == '__main__':  # pragma: no cover
    run()
