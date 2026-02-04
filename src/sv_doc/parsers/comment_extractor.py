"""Extraction strategies for raw comments."""

from pathlib import Path
from typing import Iterable

from sv_doc.interfaces import CommentExtractor
from sv_doc.models.comment import CommentBlock


class RegexCommentExtractor(CommentExtractor):
    """Placeholder extractor that will scan files for comment blocks."""

    def extract(self, source_paths: Iterable[Path]) -> Iterable[CommentBlock]:
        raise NotImplementedError
