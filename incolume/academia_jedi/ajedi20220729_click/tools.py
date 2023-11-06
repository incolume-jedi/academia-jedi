import click

CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug/--no-debug', default=False, help='Activate debug mode.')
@click.pass_context
def cli(ctx, **kwargs):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj.update(**kwargs)


@cli.command()
@click.pass_context
def show(ctx):
    click.secho(f'{ctx.obj}')


@cli.command()
@click.pass_context
def sync(ctx):
    click.echo('Debug is %s' % (ctx.obj['debug'] and 'on' or 'off'))


if __name__ == '__main__':
    cli()
