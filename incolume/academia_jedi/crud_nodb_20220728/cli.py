import click
from basedados import select_all

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# Example from https://stackoverflow.com/a/50442496/5132101
#
# @click.command(context_settings=CONTEXT_SETTINGS)
# @click.option('--toduhornot', is_flag=True, help='prints "duh..."')
# def duh(toduhornot):
#     if toduhornot:
#         click.echo('duh...')
#     else:
#         with click.Context(duh) as ctx:
#             click.echo(ctx.get_help())


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-a', '--read_all', is_flag=True, help='Read all records')
def run(read_all):
    if not read_all:
        with click.Context(run) as ctx:
            click.secho(ctx.get_help(), fg='red')
    click.echo(select_all())
