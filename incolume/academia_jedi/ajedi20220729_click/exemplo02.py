"""Module."""

import click


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """CLI."""
    if ctx.invoked_subcommand is None:
        click.echo('I was invoked without subcommand')
    else:
        click.echo(f'I am about to invoke {ctx.invoked_subcommand}')


@cli.command()
def sync():
    """Sync."""
    click.echo('The subcommand')


if __name__ == '__main__':
    cli()
