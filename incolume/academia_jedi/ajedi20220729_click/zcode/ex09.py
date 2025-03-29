"""Module."""

import click


@click.command()
@click.option('--blue', is_flag=True, help='message in blue color')
def hello(blue):
    """Estudo com flag de cor."""
    click.secho('Hello there', fg='blue' if blue else None)


if __name__ == '__main__':
    hello()
    hello(blue=True)
