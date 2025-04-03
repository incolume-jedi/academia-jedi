"""Module."""

import ast

from icecream import ic
from incolume.academia_jedi.ajedi20230113_zipfile import (
    clean_workdir,
    logger,
    realpython01,
    realpython02,
    realpython03,
    realpython04,
    realpython05,
    realpython06,
    realpython07,
    realpython08,
    realpython09,
    realpython10,
    realpython11,
    realpython12,
    realpython13,
    realpython14,
    realpython15,
    realpython16,
    realpython17,
    realpython18,
    realpython19,
    realpython20,
    realpython21,
    realpython22,
    realpython23,
    realpython24,
    realpython25,
    realpython26,
    realpython27,
    realpython28,
    realpython29,
    realpython30,
    realpython31,
    realpython32,
    realpython33,
)

__all__ = [
    'realpython01',
    'realpython02',
    'realpython03',
    'realpython04',
    'realpython05',
    'realpython06',
    'realpython07',
    'realpython08',
    'realpython09',
    'realpython10',
    'realpython11',
    'realpython12',
    'realpython13',
    'realpython14',
    'realpython15',
    'realpython16',
    'realpython17',
    'realpython18',
    'realpython19',
    'realpython20',
    'realpython21',
    'realpython22',
    'realpython23',
    'realpython24',
    'realpython25',
    'realpython26',
    'realpython27',
    'realpython28',
    'realpython29',
    'realpython30',
    'realpython31',
    'realpython32',
    'realpython33',
]


def run():
    """Run it."""
    funcnames = (ic(f'realpython{x:02}.run') for x in range(1, 34))
    functions = [ast.literal_eval(ic(f)) for f in funcnames]
    for func in functions:
        logger.debug(func.__name__)
        try:
            func()
        except (FileNotFoundError, ImportError) as e:
            logger.exception(e.strerror)
    clean_workdir()


if __name__ == '__main__':
    run()
