"""Configuration models for sv-doc.

Keep configuration concerns separated from runtime logic.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ProjectConfig:
    """Static configuration for a documentation run."""

    source_roots: Iterable[Path]
    output_dir: Path
    include_patterns: Iterable[str]
    exclude_patterns: Iterable[str]
    comment_style: str
    output_format: str
