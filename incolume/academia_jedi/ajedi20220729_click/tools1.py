import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.option('--debug/--no-debug', default=False, help='Activate debug mode.')
@click.pass_context
def cli(ctx, **kwargs):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj.update(**kwargs)
    if ctx.invoked_subcommand is None:
        click.secho(cli.get_help(ctx), fg='red')


@cli.command()
@click.pass_context
def show(ctx):
    """Show context content."""
    click.secho(f'{ctx.obj}')


@cli.command()
@click.pass_context
def sync(ctx):
    """Show debug state."""
    click.echo('Debug is %s' % (ctx.obj['debug'] and 'on' or 'off'))


if __name__ == '__main__':
    cli()