#!/usr/bin/python

import click


@click.command()
@click.argument('word')
@click.option('--shout/--no-shout', default=False)
def output(word, shout):
    # if shout:
    #     click.echo(word.upper())
    # else:
    #     click.echo(word)
    click.secho(word.upper() if shout else word)

if __name__ == '__main__':
    output()
