"""JAM file endpoint.

This command recieve file or folder path and return result.
"""
import click


@click.command()
@click.version_option(message='JAMProject, version %(version)s')
def cli():
    """CLI.

    - If version is flagged, print version string.
    """
    pass


def main():
    """Entrypoint."""
    cli()
