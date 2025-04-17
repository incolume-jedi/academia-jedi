"""Example."""

import click


@click.group()
def messages():
    """Messages."""


@click.command()
def generic():
    """Generic."""
    click.echo('Hello there')


@click.command()
def welcome():
    """Welcome."""
    click.echo('Welcome')


messages.add_command(generic)
messages.add_command(welcome)


if __name__ == '__main__':
    messages()
