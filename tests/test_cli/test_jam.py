"""Test cases for jamproject.clit.jam module."""
from click.testing import CliRunner

from jamproject import __version__
from jamproject.cli import jam


def test_version():
    """Test to print version."""
    runner = CliRunner()
    result = runner.invoke(jam.cli, ['--version'])
    assert result.exit_code == 0
    assert 'JAMProject' in result.output
    assert __version__ in result.output
