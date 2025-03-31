"""Exemplo coloured."""

import click


@click.command()
def coloured():
    """Coloured."""
    click.secho('Hello there', fg='blue', bold=True)


if __name__ == '__main__':
    coloured()
