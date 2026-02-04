"""Core interfaces (protocols) for extensibility.

Define abstractions that enable SOLID-friendly composition.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Protocol, runtime_checkable

from sv_doc.models.comment import CommentBlock
from sv_doc.models.document import Documentation


@runtime_checkable
class CommentExtractor(Protocol):
    """Extract raw comment blocks from source files."""

    def extract(self, source_paths: Iterable[Path]) -> Iterable[CommentBlock]:
        raise NotImplementedError


@runtime_checkable
class CommentParser(Protocol):
    """Parse raw comment blocks into structured documentation nodes."""

    def parse(self, blocks: Iterable[CommentBlock]) -> Documentation:
        raise NotImplementedError


@runtime_checkable
class Renderer(Protocol):
    """Render documentation into a target output format."""

    def render(self, documentation: Documentation) -> str:
        raise NotImplementedError


@runtime_checkable
class OutputWriter(Protocol):
    """Persist rendered output to a destination."""

    def write(self, content: str, output_dir: Path) -> None:
        raise NotImplementedError
