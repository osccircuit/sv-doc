"""Application service wiring.

This module defines the composition root, leaving concrete implementations
injectable for testing or alternate formats.
"""

from dataclasses import dataclass

from sv_doc.config import ProjectConfig
from sv_doc.pipeline.orchestrator import DocumentationPipeline


@dataclass(frozen=True)
class DocumentationApp:
    """High-level application entry point."""

    config: ProjectConfig
    pipeline: DocumentationPipeline

    def generate(self) -> None:
        """Run the pipeline with configuration-provided inputs."""

        raise NotImplementedError
