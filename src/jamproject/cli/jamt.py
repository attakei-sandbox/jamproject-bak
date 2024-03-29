"""JAM text endpoint.

This command recieve raw text data and return result.
"""
import click

from .. import __version__
from ..core import TextUnit


@click.command()
@click.version_option(message='JAMProject, version %(version)s (text mode)')
@click.option('--verbose', '-v', is_flag=True)
@click.argument('text')
def cli(text, verbose):
    """CLI.

    - If version is flagged, print version string.
    """
    if verbose:
        click.echo(f'JAMProject {__version__}')
        click.echo(f'Target text: {text}')
    unit = TextUnit(text)
    if verbose:
        click.echo(f'Tokens: {unit.splitted_text()}')


def main():
    """Entrypoint."""
    cli()
