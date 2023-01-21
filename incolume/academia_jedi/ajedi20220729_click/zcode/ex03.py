#!/usr/bin/python

import click


@click.command()
@click.argument("name", default="guest")
@click.argument("age", type=int)
def hello(name, age):
    click.echo(f"{name} is {age} years old")


if __name__ == "__main__":
    hello()
