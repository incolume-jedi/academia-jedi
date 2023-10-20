"""Exemplo sincrono."""
from time import perf_counter, sleep

servers = (f'192.168.1.{x}' for x in range(1, 100))


def simulation_ssh_connection(position, ip):
    sleep(1)
    print(f'{position} - {ip}')


def run():
    start_time = perf_counter()
    _ = [
        simulation_ssh_connection(position, ip)
        for position, ip in enumerate(servers, 1)
    ]
    print('Tempo de execução: {}s'.format(perf_counter() - start_time))


if __name__ == '__main__':  # pragma: no cover
    run()
