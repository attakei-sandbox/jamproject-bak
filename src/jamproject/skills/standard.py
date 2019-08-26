"""Standard skill module.

標準利用されるスキルを管理するモジュールです
"""
from jamproject.core import Tokens


def limit_toten(tokens: Tokens):
    """読点の数が指定値以下であることを検査する。"""
    limit_toten = 2

    class Result(object):
        """処理結果オブジェクト"""

        def __init__(self, msg):
            self.msg = msg
    cnt_toten = len([t for t in tokens if t.surface == '、'])
    if cnt_toten > limit_toten:
        return Result(f'読点（、）の数が多いです。 期待数={limit_toten} 検出数={cnt_toten}')
    return Result('')
