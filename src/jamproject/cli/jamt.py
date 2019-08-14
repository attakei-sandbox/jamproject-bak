"""JAM text endpoint.

This command recieve raw text data and return result.
"""
import click

from .. import __version__


@click.command()
@click.option('--version', '-V', is_flag=True)
def cli(version: bool):
    """CLI.

    - If version is flagged, print version string.
    """
    if version:
        click.echo(f'JAM Project v{__version__}')
        return


def main():
    """Entrypoint."""
    cli()
