"""Module."""

import click


@click.command()
@click.option('--word', '-w', multiple=True)
def words(word):
    """Words."""
    click.echo('\n'.join(word))
    click.echo(f'or {word}')


if __name__ == '__main__':
    words()
