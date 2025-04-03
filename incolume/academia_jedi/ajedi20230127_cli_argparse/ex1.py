"""Exemplo."""

from argparse import ArgumentParser, Namespace

# ruff: noqa: T201

parser = ArgumentParser()

parser.add_argument('echo', help='echo the given string ')

if __name__ == '__main__':
    args: Namespace = parser.parse_args()
    print(args.echo)
