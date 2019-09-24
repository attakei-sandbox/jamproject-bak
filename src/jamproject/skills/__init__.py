"""Included skills package."""
import logging

# Message levels
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR


class SkillResult(object):
    """Skillで処理を行った結果を保持するクラス。

    Skillは必ずこのオブジェクト、もしくはこれと同等のインターフェースを持つオブジェクトを返すこと。
    """

    def __init__(self, level: int, message: str):
        """メッセージレベルと、メッセージが必要。

        ただし、基本的は ``passed()``,' ``warning()`` などの仕様を推奨
        """
        self._level = level
        self._message = message

    @classmethod
    def passed(cls, message: str = ''):
        """検査OK時のSkillResultオブジェクトを返す。

        :rtype: SkillResult
        """
        return cls(INFO, message)

    @classmethod
    def warning(cls, message: str):
        """検査NG時のSkillResultオブジェクトを返す。

        :rtype: SkillResult
        """
        return cls(WARNING, message)

    @property
    def level(self) -> int:
        """結果の判定レベル。（loggingのログレベルと同値）"""
        return self._level

    @property
    def message(self) -> str:
        """Skillからのメッセージ"""
        return self._message
