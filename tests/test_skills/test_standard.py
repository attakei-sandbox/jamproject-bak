"""Test case for jamproject.skills.standard module."""
from jamproject.core import TextUnit
from jamproject.skills import standard, WARNING, INFO


def test_count_tokens_succeed():
    unit = TextUnit('明日は、晴れ')
    result = standard.limit_toten(unit)
    assert result.message == ''


def test_count_tokens_failure():
    unit = TextUnit('明日は、とびきり、晴れて、いました')
    result = standard.limit_toten(unit)
    assert '期待数=' in result.message
    assert '検出数=' in result.message


def test_limit_length_succeed():
    unit = TextUnit('、'.join(['明日は晴れ', ] * 13))
    result = standard.limit_length(unit)
    assert result.level == INFO


def test_limit_length_succeed():
    unit = TextUnit('、'.join(['明日は晴れ', ] * 14))
    result = standard.limit_length(unit)
    assert result.level == WARNING
