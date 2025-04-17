"""Example."""

import click


@click.group()
def cli():
    """Comand Line Interface."""


@cli.command(name='gen')
def generic():
    """Generic."""
    click.echo('Hello there')


@cli.command(name='wel')
def welcome():
    """Welcome."""
    click.echo('Welcome')


if __name__ == '__main__':
    cli()
