"""Filesystem IO helpers."""

from pathlib import Path


class FileOutputWriter:
    """Write rendered output to the filesystem."""

    def write(self, content: str, output_dir: Path) -> None:
        with open(output_dir, "w", encoding="utf8") as file_out:
            file_out.write(content)
