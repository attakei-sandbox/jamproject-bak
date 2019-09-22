"""Included skills package."""
import logging


# Message levels
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR


class SkillResult(object):
    """Skillで処理を行った結果
    """
    def __init__(self, level: int, message: str):
        self._level = level
        self._message = message

    @classmethod
    def passed(cls, message: str=''):
        return cls(INFO, message)

    @classmethod
    def warning(cls, message: str):
        return cls(WARNING, message)

    @property
    def level(self) -> int:
        """Message level of result
        """
        return self._level

    @property
    def message(self) -> str:
        """Message from skill
        """
        return self._message
