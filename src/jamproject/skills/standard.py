"""Standard skill module.

標準利用されるスキルを管理するモジュールです
"""
from ..core import TextUnit
from . import SkillResult, WARNING


def limit_toten(unit: TextUnit) -> SkillResult:
    """読点の数が指定値以下であることを検査する。"""
    limit_toten = 2

    cnt_toten = len([t for t in unit.tokens if t.surface == '、'])
    if cnt_toten > limit_toten:
        msg = f'読点（、）の数が多いです。 期待数={limit_toten} 検出数={cnt_toten}'
        return SkillResult.warning(msg)
    return SkillResult.passed()
