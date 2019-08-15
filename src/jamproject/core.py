"""JAMProject core module.

This module has minimum classes and functions to execute project.
"""
from typing import List

from janome.tokenizer import Token, Tokenizer

tokenizer = Tokenizer()


class TextUnit(object):
    """Unit component to manage text and analyze."""

    def __init__(self, raw_text: str):
        """In initializing, run tokenize."""
        self._raw_text: str = raw_text
        tokenized = tokenizer.tokenize(self.raw_text)
        self._tokens: List[Token] = [t for t in tokenized]

    @property
    def raw_text(self) -> str:
        """Binded raw text."""
        return self._raw_text

    @property
    def tokens(self) -> List[Token]:
        """Token parts of raw text."""
        return self._tokens

    def splitted_text(self, delimiter: str = ',') -> str:
        """Generate delimiter splitted text from tokens."""
        return delimiter.join([t.surface for t in self.tokens])
