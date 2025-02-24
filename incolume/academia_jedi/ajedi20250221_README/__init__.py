"""Module."""

import logging
import re
from pathlib import Path

from icecream import ic

paths = Path(__file__).parent

logging.debug(ic(paths))

condition = re.compile(r'ajedi')

subprojects = [
    p.name
    for p in paths.parents[0].iterdir()
    if p.is_dir() and re.match(condition, p.stem)
]


def create_readme(
    directory: Path,
    filename: str = 'README.md',
    model: Path | None = None,
) -> bool:
    """Create README file."""
    model = model or Path(__file__).parent / 'model.md'
    result = False
    directory.mkdir(parents=True, exist_ok=True)
    logging.debug(ic(directory, directory.exists()))
    file = directory / filename
    file.write_bytes(model.read_bytes())
    result = file.is_file()
    logging.debug(ic(result))
    return result
