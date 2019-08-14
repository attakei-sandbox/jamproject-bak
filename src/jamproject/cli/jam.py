"""JAM file endpoint.

This command recieve file or folder path and return result.
"""
import click


@click.command()
@click.version_option(message='JAMProject, version %(version)s')
@click.argument('target', type=click.Path(exists=True))
def cli(target: str):
    """CLI.

    - If version is flagged, print version string.
    """
    pass


def main():
    """Entrypoint."""
    cli()
