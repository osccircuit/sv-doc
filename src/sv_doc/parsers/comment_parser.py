"""Parsing strategies for structured documentation."""

from typing import Iterable
from dataclasses import dataclass
import re

from sv_doc.models.comment import CommentBlock
from sv_doc.models.document import Documentation, BuilderSection


@dataclass
class Tag:
    name: str
    pattern: str


class TagBasedCommentParser:
    """Parser for tag-based comment formats."""

    TAGS = [
        Tag("name", r"\* @name:(.+)"),
        Tag("description", r"\* @description:(.+)"),
    ]

    def __init__(self, type_section):
        self.type_section = type_section

    def parse(self, blocks: Iterable[CommentBlock]) -> Documentation:
        sections: list[type] = []
        for block in blocks:
            builder = BuilderSection(self.type_section)
            for tag in self.TAGS:
                parsed = self.try_parse(tag.pattern, block.content)
                builder.add(tag.name, parsed)
            section = builder.build()
            if section is not None:
                section.append(section)
        return Documentation(sections)

    def try_parse(self, pattern, string):
        match = re.search(pattern, string)
        if match is None:
            return None
        return match.group(1)
