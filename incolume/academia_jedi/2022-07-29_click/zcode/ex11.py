#!/usr/bin/python

import click
import os
from pathlib import Path

@click.argument('mydir', envvar='MYDIR', type=click.Path(exists=True))
@click.command()
def dolist(mydir):
    # click.echo(os.listdir(mydir))
    click.echo(tuple(x.as_posix() for x in Path(mydir).resolve().iterdir()))


if __name__ == '__main__':
    dolist()
