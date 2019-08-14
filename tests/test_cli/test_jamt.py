"""Test cases for jamproject.clit.jamt module."""
from click.testing import CliRunner

from jamproject import __version__
from jamproject.cli import jamt


def test_version():
    """Test to print version."""
    runner = CliRunner()
    result = runner.invoke(jamt.cli, ['--version'])
    assert result.exit_code == 0
    assert 'JAM Project' in result.output
    assert __version__ in result.output
