"""JAMProject core module.

This module has minimum classes and functions to execute project.
"""
from janome.tokenizer import Tokenizer


tokenizer = Tokenizer()


class TextUnit(object):
    """Unit component to manage text and analyze."""
    def __init__(self, raw_text: str):
        self._raw_text: str = raw_text
        tokenized = tokenizer.tokenize(self.raw_text)
        self._tokens: list = [t for t in tokenized]

    @property
    def raw_text(self) -> str:
        """Binded raw text."""
        return self._raw_text

    @property
    def tokens(self) -> list:
        """Token parts of raw text."""
        return self._tokens
