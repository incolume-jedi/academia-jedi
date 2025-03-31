"""https://zetcode.com/python/click/."""

import click


@click.command()
def hello():
    """Hello."""
    click.echo('Hello there')


if __name__ == '__main__':
    hello()
