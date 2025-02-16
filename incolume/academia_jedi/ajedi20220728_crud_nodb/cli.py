"""Solving question."""

import logging
from typing import Any, NoReturn

import click
from icecream import ic
from incolume.academia_jedi.ajedi20220728_crud_nodb.basedados import (
    create_person,
    select_all_person,
    select_person,
)
from incolume.academia_jedi.ajedi20220728_crud_nodb.model import Pessoa

CONTEXT_SETTINGS: dict[str, Any] = {'help_option_names': ['-h', '--help']}


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.option('--debug/--no-debug', default=False, help='Activate debug mode.')
@click.pass_context
def run(ctx: dict, **kwargs: str) -> NoReturn:
    """Run.

    ensure that ctx.obj exists and is a dict (in case `cli()` is called
    by means other than the `if` block below)
    """
    logging.debug(ic(ctx))
    ctx.ensure_object(dict)
    ctx.obj.update(**kwargs)
    if ctx.invoked_subcommand is None:
        click.secho(run.get_help(ctx), fg='red')


@run.command()
@click.pass_context
def show(ctx: dict) -> NoReturn:
    """Show context content."""
    logging.debug(ic(ctx))
    click.secho(f'{ctx.obj}')


@run.command()
@click.option('-p', '--person', type=dict, help='Index of record.')
@click.pass_context
def insert(ctx: dict, person: dict) -> NoReturn:
    """Insert one record into database.

    ex: {
        'name': 'name',
        'date_born': '20/06/1978',
        'email': ['email1', 'email2'], # optional
        'telefone': ['phone1', 'phone2],  # optional
        'address': ['add1', 'add2]}   # optional
    """
    logging.debug(ic(ctx))
    click.secho(
        create_person(Pessoa(**person), ctx.obj.get('debug')),
        fg='green',
    )


@run.command()
@click.pass_context
def sync(ctx: dict) -> NoReturn:
    """Show debug state."""
    logging.debug(ic(ctx))
    click.echo('Debug is %s' % (ctx.obj['debug'] and 'on' or 'off'))


@run.command()
@click.pass_context
def read_all(ctx: dict) -> NoReturn:
    """Show all records into database."""
    logging.debug(ic(ctx))
    click.secho(select_all_person(), fg='green')


@run.command()
@click.option('-i', '--index', type=int, help='Index of record.')
@click.pass_context
def read_one(ctx: dict, index: int) -> NoReturn:
    """Show one record into database."""
    logging.debug(ic(ctx))
    click.secho(select_person(index), fg='green')
