"""Pipeline orchestration for documentation generation."""

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from sv_doc.interfaces import CommentExtractor, CommentParser, OutputWriter, Renderer


@dataclass(frozen=True)
class DocumentationPipeline:
    """Compose extraction, parsing, rendering, and writing steps."""

    extractor: CommentExtractor
    parser: CommentParser
    renderer: Renderer
    writer: OutputWriter

    def run(self, source_paths: Iterable[Path], output_dir: Path) -> None:
        """Execute the end-to-end documentation pipeline."""
        src_paths = [Path("../test.sv")]
        print(src_paths)
        comment_blocks = self.extractor.extract(src_paths)
        documentation = self.parser.parse(comment_blocks)
        render_doc = self.renderer.render(documentation)
        self.writer.write(render_doc, Path("../test.html"))
