"""Test case for jamproject.skills.standard module."""
from jamproject.core import TextUnit
from jamproject.skills import standard


def test_count_tokens_succeed():
    unit = TextUnit('明日は、晴れ')
    result = standard.limit_toten(unit.tokens)
    assert hasattr(result, 'msg')
    assert result.msg == ''

def test_count_tokens_failure():
    unit = TextUnit('明日は、とびきり、晴れて、いました')
    result = standard.limit_toten(unit.tokens)
    assert hasattr(result, 'msg')
    assert '期待数=' in result.msg
    assert '検出数=' in result.msg
