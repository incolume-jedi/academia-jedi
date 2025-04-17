"""Module."""

import click


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    """CLI."""
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()  # @cli, not @click!
def sync():
    """Sync."""
    click.echo('Syncing')


if __name__ == '__main__':
    cli()

# run: python exemplo01.py --debug sync
