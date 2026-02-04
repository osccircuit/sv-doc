"""Filesystem IO helpers."""

from pathlib import Path

from sv_doc.interfaces import OutputWriter


class FileOutputWriter(OutputWriter):
    """Write rendered output to the filesystem."""

    def write(self, content: str, output_dir: Path) -> None:
        raise NotImplementedError
