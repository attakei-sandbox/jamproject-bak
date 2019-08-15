"""Test case for jamproject.core.Unit class."""
from jamproject.core import TextUnit


def test_init_core():
    """"Test for basic behavior of class."""
    unit = TextUnit('Sample')
    assert unit.raw_text == 'Sample'
    assert len(unit.tokens) == 1


def test_init_simple_ja_text():
    """"Test for basic behavior of class."""
    unit = TextUnit('本日は晴天なり')
    assert len(unit.tokens) == 4
