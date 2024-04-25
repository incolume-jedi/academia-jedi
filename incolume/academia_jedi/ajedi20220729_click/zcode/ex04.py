#!/usr/bin/python

from functools import reduce
from operator import mul

import click


@click.command()
@click.argument('vals', type=int, nargs=-1)
def process(vals):
    print(f'The sum is {sum(vals)}')
    print(f'The product is {reduce(mul, vals, 1)}')


if __name__ == '__main__':
    process()
