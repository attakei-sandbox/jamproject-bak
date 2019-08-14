"""Test cases for jamproject.clit.jam module."""
import tempfile

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


def test_not_path():
    """If passed none-file path (not exists), return 2."""
    with tempfile.TemporaryDirectory() as tmpdir:
        runner = CliRunner()
        result = runner.invoke(jam.cli, [tmpdir + '/not-found'])
        assert result.exit_code == 2


def test_path():
    """If passed none-file path (not exists), return 0."""
    with tempfile.TemporaryDirectory() as tmpdir:
        runner = CliRunner()
        result = runner.invoke(jam.cli, [tmpdir])
        assert result.exit_code == 0
