"""Structured documentation models.

These models are intentionally minimal; extend them to represent sections,
entities, and metadata extracted from comments.
"""

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(frozen=True)
class DocSection:
    """A logical documentation section."""

    title: str
    body: str


@dataclass(frozen=True)
class Documentation:
    """Root documentation container."""

    sections: Iterable[DocSection] = field(default_factory=list)
