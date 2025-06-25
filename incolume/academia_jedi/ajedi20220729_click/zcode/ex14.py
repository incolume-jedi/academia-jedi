"""Module."""

import click

# ruff: noqa: SIM113


@click.command()
@click.argument('file_name', type=click.File('r'))
@click.argument('lines', default=-1, type=int)
def head(file_name, lines):
    """Head."""
    counter = 0
    for line in file_name:
        print(line.strip())
        counter += 1
        if counter == lines:
            break


@click.command()
@click.argument('file_name', type=click.File('r'))
@click.argument('lines', default=-1, type=int)
def mine_head(file_name, lines):
    """Mine head."""
    for line in file_name.readlines()[: lines if lines > 0 else None]:
        print(line.strip())


if __name__ == '__main__':
    mine_head()
