"""Test cases for jamproject.clit.jamt module."""
from click.testing import CliRunner

from jamproject import __version__
from jamproject.cli import jamt


def test_version():
    """Test to print version."""
    runner = CliRunner()
    result = runner.invoke(jamt.cli, ['--version'])
    assert result.exit_code == 0
    assert 'JAMProject' in result.output
    assert __version__ in result.output


def test_verbose_behavior():
    """Test -v/--verbose behavior.

    - First, print version
    """
    runner = CliRunner()
    result = runner.invoke(jamt.cli, ['-v', 'sample'])  # Example text
    assert result.exit_code == 0
    assert 'JAMProject' in result.output
    assert __version__ in result.output
    assert 'Target text' in result.output
    assert 'sample' in result.output


def test_verbose_tokenizable_source():
    """Test -v/--verbose behavior.

    - First, print version
    """
    runner = CliRunner()
    result = runner.invoke(jamt.cli, ['-v', '本日は晴天なり'])  # Example text
    assert result.exit_code == 0
    assert '本日,は,晴天,なり' in result.output
