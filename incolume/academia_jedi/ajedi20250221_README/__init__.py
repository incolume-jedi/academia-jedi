"""Module."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING

from icecream import ic

if TYPE_CHECKING:
    from collections.abc import Callable

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
    filename: str = '',
    model: Path | None = None,
) -> bool:
    """Create README file."""
    filename = filename or 'README.md'
    model = model or Path(__file__).parent / 'model.md'
    result = False
    directory.mkdir(parents=True, exist_ok=True)
    logging.debug(ic(directory, directory.exists()))
    file = directory / filename
    file.write_bytes(model.read_bytes())
    result = file.is_file()
    logging.debug(ic(result))
    return result


def apply_issue(
    func: Callable,
    list_dir: list[Path],
    filename: str = '',
    model: Path | None = None,
) -> None:
    """Apply this issue."""
    for path_dir in list_dir:
        func(directory=path_dir, filename=filename, model=model)


if __name__ == '__main__':
    apply_issue(func=create_readme, list_dir=[Path(p) for p in subprojects])
