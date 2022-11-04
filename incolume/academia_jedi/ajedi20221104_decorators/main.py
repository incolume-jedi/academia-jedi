from functools import wraps
from time import perf_counter_ns, sleep
import logging
from inspect import stack


__author__ = "@britodfbr"  # pragma: no cover
logging.basicConfig(level=logging.DEBUG)


def performance_meter(func):
    """Calculate performace."""
    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug(f'{func.__name__}@{stack()[0][3]}')
        logging.info(f'{args=}, {kwargs=}')
        start_time = perf_counter_ns()
        func(*args, **kwargs)
        total_time = round(perf_counter_ns() - start_time, 2)
        logging.info(f'{total_time} ns')
    return inner


@performance_meter
def gretting(name: str = None) -> str:
    """Show gretting with name."""
    sleep(1)
    frase = f'Olá {name}.'
    print(frase)
    return frase


def run():
    gretting('Mundo')


if __name__ == '__main__':    # pragma: no cover
    run()
