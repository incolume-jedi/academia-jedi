"""Module."""

import click


@click.command()
@click.argument('word')
@click.option('--shout/--no-shout', default=False)
def output(word, shout):
    """Out put."""
    # if shout:
    click.secho(word.upper() if shout else word)


if __name__ == '__main__':
    output()
