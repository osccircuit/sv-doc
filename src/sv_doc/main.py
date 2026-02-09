"""Application service wiring.

This module defines the composition root, leaving concrete implementations
injectable for testing or alternate formats.
"""

from dataclasses import dataclass

from sv_doc.config import ProjectConfig
from sv_doc.pipeline.orchestrator import DocumentationPipeline
from sv_doc.parsers.comment_extractor import RegexCommentExtractor
from sv_doc.parsers.comment_parser import TagBasedCommentParser
from sv_doc.models.document import DocSection
from sv_doc.renderers.html_renderer import HtmlRenderer
from sv_doc.io.filesystem import FileOutputWriter


@dataclass(frozen=True)
class DocumentationApp:
    """High-level application entry point."""

    config: ProjectConfig
    pipeline: DocumentationPipeline

    def generate(self) -> None:
        """Run the pipeline with configuration-provided inputs."""
        self.pipeline.run(".", ".")


if __name__ == "__main__":
    config = ProjectConfig(".", ".", ".", ".", ".", ".")
    pipline = DocumentationPipeline(
        RegexCommentExtractor(),
        TagBasedCommentParser(DocSection),
        HtmlRenderer(),
        FileOutputWriter(),
    )
    app = DocumentationApp(config, pipline)
    app.generate()
