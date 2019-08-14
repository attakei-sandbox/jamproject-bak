"""JAM text endpoint.

This command recieve raw text data and return result.
"""
import click


@click.command()
@click.version_option(message='JAMProject, version %(version)s (text mode)')
def cli():
    """CLI.

    - If version is flagged, print version string.
    """
    pass


def main():
    """Entrypoint."""
    cli()
