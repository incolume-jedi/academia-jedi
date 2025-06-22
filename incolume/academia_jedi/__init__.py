"""Module academia_jedi."""

import logging
import os
from logging.config import dictConfig
from pathlib import Path

import yaml
from icecream import ic

try:
    from tomli import load
except (ModuleNotFoundError, ImportError):
    from tomllib import load

file_config_log = Path(__file__).parents[2].joinpath('settings/logging.yml')

with file_config_log.open('rt') as f:
    config = yaml.safe_load(f.read())

dictConfig(config)

logger = logging.getLogger(ic(os.getenv('INCOLUME_MODE') or 'testing'))


version_file = Path(__file__).parent / 'version.txt'
project_file = Path(__file__).parents[2] / 'pyproject.toml'
try:
    with project_file.open('rb') as file:
        version_file.write_text(f'{load(file)["tool"]["poetry"]["version"]}\n')
except FileNotFoundError:
    pass

__version__ = version_file.read_text().strip()
logger.info('Load __version__: %s', __version__)
