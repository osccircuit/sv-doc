"""Parsing strategies for structured documentation."""

from typing import Iterable

from sv_doc.interfaces import CommentParser
from sv_doc.models.comment import CommentBlock
from sv_doc.models.document import Documentation


class TagBasedCommentParser(CommentParser):
    """Placeholder parser for tag-based comment formats."""

    def parse(self, blocks: Iterable[CommentBlock]) -> Documentation:
        raise NotImplementedError
