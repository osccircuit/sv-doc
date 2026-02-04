"""Plugin registry for discovery of extractors, parsers, and renderers."""

from dataclasses import dataclass, field
from typing import Dict, Type

from sv_doc.interfaces import CommentExtractor, CommentParser, Renderer


@dataclass
class PluginRegistry:
    """Simple in-memory registry for interchangeable components."""

    extractors: Dict[str, Type[CommentExtractor]] = field(default_factory=dict)
    parsers: Dict[str, Type[CommentParser]] = field(default_factory=dict)
    renderers: Dict[str, Type[Renderer]] = field(default_factory=dict)
