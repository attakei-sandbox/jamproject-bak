"""Included skills package."""
import logging


# Message levels
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR


class SkillResult(object):
    """Skillで処理を行った結果
    """
    @property
    def level(self):
        raise NotImplementedError()

    @property
    def message(self):
        raise NotImplementedError()


class SkillPassed(SkillResult):
    def __init__(self, message=''):
        self._message = message

    @property
    def level(self):
        return INFO

    @property
    def message(self):
        return self._message
