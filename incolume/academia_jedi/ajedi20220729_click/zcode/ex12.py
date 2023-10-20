#!/usr/bin/python

import click


@click.command()
@click.option('--data', required=True, type=(str, int))
def output(data):
    """Python func_name --data abc 123."""
    click.echo(f'name={data[0]} age={data[1]}')


if __name__ == '__main__':
    output()
