"""Extraction strategies for raw comments."""

from pathlib import Path
from typing import Iterable

from sv_doc.models.comment import CommentBlock


class RegexCommentExtractor:
    """Extractor that will scan files for comment blocks."""

    START_COMMENT = "/**"
    END_COMMENT = "*/"

    def extract(self, source_paths: Iterable[Path]) -> Iterable[CommentBlock]:
        blocks = []
        for src_path in source_paths:
            with open(src_path, encoding="utf8") as src_stream:
                blocks.extend(self._search_blocks(src_path, src_stream))
        return blocks

    def _search_blocks(
        self, src_path: Path, stream: Iterable[str]
    ) -> Iterable[CommentBlock]:
        blocks = []
        line_start = None
        content = ""
        for num, line in enumerate(stream, 1):
            if line_start is None:
                if self._search_start(line):
                    line_start = num
                    content += line
            else:
                content += line
                if self._search_end(line):
                    blocks.append(
                        self._create_block(
                            src_path,
                            line_start,
                            num,
                            content,
                        )
                    )
                    content = ""
                    line_start = None
        return blocks

    def _search_start(self, src_string: str) -> bool:
        return self.START_COMMENT == src_string.strip()

    def _search_end(self, src_string: str) -> bool:
        return self.END_COMMENT == src_string.strip()

    def _create_block(
        self,
        source_path: Path,
        line_start: int,
        line_end: int,
        content: str,
        style: str = "",
    ) -> CommentBlock:
        return CommentBlock(source_path, line_start, line_end, content, style)
