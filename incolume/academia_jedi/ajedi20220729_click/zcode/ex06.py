"""Module."""

import click


@click.command()
@click.option('-s', '--string')
def output(string):
    """Options abrevidas."""
    click.echo(string)


if __name__ == '__main__':
    output()
