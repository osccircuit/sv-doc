"""Structured documentation models.

These models are intentionally minimal; extend them to represent sections,
entities, and metadata extracted from comments.
"""

from dataclasses import dataclass, field
from typing import Iterable


class BuilderSection:
    def __init__(self, type_section):
        self.type_section = type_section
        self.attrs = self.type_section.__annotations__
        self.values = {}

    def get_required(self):
        return set(self.attrs.keys())

    def get_values(self):
        return self.values

    def add(self, name, value):
        if value is not None and name in self.attrs:
            self.values[name] = value

    def build(self):
        if not self._validate():
            return None
        section = self.type_section(**self.values)
        return section

    def _validate(self):
        if self.get_required().issubset(self.values):
            return True
        return False


@dataclass(frozen=True)
class DocSection:
    """A logical documentation section."""

    name: str
    description: str


@dataclass(frozen=True)
class Documentation:
    """Root documentation container."""

    sections: Iterable[DocSection] = field(default_factory=list)
