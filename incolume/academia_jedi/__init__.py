"""Module academia_jedi."""

import logging
from pathlib import Path
from platform import system

from config import settings

try:
    from tomli import load
except (ModuleNotFoundError, ImportError):
    from tomllib import load


logging.basicConfig(
    level=logging.INFO,
    format=settings.format_log_win
    if system().casefold().startswith('win')
    else settings.format_log,
)


version_file = Path(__file__).parent / 'version.txt'
project_file = Path(__file__).parents[2] / 'pyproject.toml'
try:
    with project_file.open('rb') as file:
        version_file.write_text(f"{load(file)['tool']['poetry']['version']}\n")
except FileNotFoundError:
    pass

__version__ = version_file.read_text().strip()
