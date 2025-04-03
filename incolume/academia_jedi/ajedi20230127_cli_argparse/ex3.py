"""Exemplo."""

from argparse import ArgumentParser, Namespace

# ruff: noqa: T201

parser = ArgumentParser()

parser.add_argument('square', help='squares a given number', type=int)
parser.add_argument(
    '-v',
    '--verbose',
    help='show details',
    action='store_true',
)


def run() -> None:
    """Run it."""
    args: Namespace = parser.parse_args()

    result = args.square**2

    if args.verbose:
        print(f'{args.square} ao quadrado é: {result}')
    else:
        print(result)


if __name__ == '__main__':
    run()
