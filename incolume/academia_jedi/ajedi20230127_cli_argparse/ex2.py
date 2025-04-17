"""Exemplo."""

from argparse import ArgumentParser, Namespace

# ruff: noqa: T201

parser = ArgumentParser()

parser.add_argument('square', help='squares a given number', type=int)

if __name__ == '__main__':
    args: Namespace = parser.parse_args()

    print(args.square**2)
