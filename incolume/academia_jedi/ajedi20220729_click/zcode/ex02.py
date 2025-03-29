"""Module."""

import click


@click.command()
@click.argument('name', default='guest')
def hello(name):
    """Exemplo com valores default."""
    click.echo(f'Hello {name}')


if __name__ == '__main__':
    hello()
