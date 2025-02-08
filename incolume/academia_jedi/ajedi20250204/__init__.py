"""20250204 module."""

from collections.abc import Generator
from pathlib import Path

directories = Path(__file__).parent


def list_dir(directory: Path | None = None) -> Generator:
    """List directories."""
    directory = directory or directories
    return directory.iterdir()
