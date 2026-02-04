"""Domain models for comment extraction."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CommentBlock:
    """Raw comment block extracted from a file."""

    source_path: Path
    line_start: int
    line_end: int
    content: str
    style: str
