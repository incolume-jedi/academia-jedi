"""Exemplo."""

import logging

# ruff: noqa: T201 PLR2004
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument(
    'square',
    help='squares a given number',
    type=int,
    default=0,
    nargs='?',
)
parser.add_argument('-v', '--verbose', help='show details', action='count')


def run() -> None:
    """Run it."""
    args: Namespace = parser.parse_args()

    result = args.square**2

    logging.debug(args.verbose)

    if not args.verbose:
        print(result)
    elif args.verbose == 1:
        print(f'{args.square} ** 2 = {result}')
    elif args.verbose >= 2:
        print(f'{args.square} ao quadrado é: {result}')


if __name__ == '__main__':
    run()
