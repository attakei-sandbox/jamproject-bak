"""JAM text endpoint.

This command recieve raw text data and return result.
"""
import click

from .. import __version__


@click.command()
@click.version_option(message='JAMProject, version %(version)s (text mode)')
@click.option('--verbose', '-v', is_flag=True)
@click.argument('src')
def cli(src, verbose):
    """CLI.

    - If version is flagged, print version string.
    """
    if verbose:
        click.echo(f'JAMProject {__version__}')
        click.echo(f'Target text: {src}')


def main():
    """Entrypoint."""
    cli()
