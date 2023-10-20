
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
# @click.option('-p', '--person', type=dict, help='Index of record.')
@click.argument('name')
@click.argument('date_born')
@click.option('--telephone', '-t', multiple=True)
@click.option('--address', '-a', multiple=True)
@click.option('--email', '-e', multiple=True)
@click.pass_context
def insert(ctx, name, date_born, telephone, address, email):
    """Insert one record into database.

    ex: {
        'name': 'name',
        'date_born': '20/06/1978',
        'email': ['email1', 'email2'], # optional
        'telefone': ['phone1', 'phone2],  # optional
        'address': ['add1', 'add2]   # optional
        }
    """
    click.secho(
        create_person(
            Pessoa(
                nome=name,
                date_born=date_born,
                email=email,
                telefone=telephone,
                address=address,
            ),
            ctx.obj.get('debug'),
        ),
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
@click.argument('index', type=int)
@click.pass_context
def read_one(ctx, index):
    """Show one record into database."""
    click.secho(select_person(index) or None, fg='green')
