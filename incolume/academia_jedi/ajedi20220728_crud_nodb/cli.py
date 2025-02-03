"""Solving question."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import click
from basedados import create_person, select_all_person, select_person
from model import Pessoa

# @click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
# @click.option('--debug/--no-debug', default=False, help='Activate debug mode.')
# @click.pass_context
# def cli(ctx, **kwargs):
#     # ensure that ctx.obj exists and is a dict (in case `cli()` is called
#     # by means other than the `if` block below)
#     if ctx.invoked_subcommand is None:


# @cli.command()
# @click.pass_context
# def show(ctx):
#     """Show context content."""


# @cli.command()
# @click.pass_context
# def sync(ctx):
#     """Show debug state."""


CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.option('--debug/--no-debug', default=False, help='Activate debug mode.')
@click.pass_context
def run(ctx, **kwargs):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj.update(**kwargs)
    if ctx.invoked_subcommand is None:
        click.secho(run.get_help(ctx), fg='red')


@run.command()
@click.pass_context
def show(ctx):
    """Show context content."""
    click.secho(f'{ctx.obj}')


@run.command()
@click.option('-p', '--person', type=dict, help='Index of record.')
@click.pass_context
def insert(ctx, person):
    """Insert one record into database.

    ex: {
        'name': 'name',
        'date_born': '20/06/1978',
        'email': ['email1', 'email2'], # optional
        'telefone': ['phone1', 'phone2],  # optional
        'address': ['add1', 'add2]}   # optional
    """
    click.secho(
        create_person(Pessoa(**person), ctx.obj.get('debug')),
        fg='green',
    )


@run.command()
@click.pass_context
def sync(ctx):
    """Show debug state."""
    click.echo('Debug is %s' % (ctx.obj['debug'] and 'on' or 'off'))


@run.command()
@click.pass_context
def read_all(ctx):
    """Show all records into database."""
    click.secho(select_all_person(), fg='green')


@run.command()
@click.option('-i', '--index', type=int, help='Index of record.')
@click.pass_context
def read_one(ctx, index):
    """Show one record into database."""
    click.secho(select_person(index), fg='green')
