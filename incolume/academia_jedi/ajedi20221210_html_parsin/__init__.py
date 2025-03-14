"""Module initialyzer."""

from pathlib import Path

config: Path = Path(__file__).parent / 'conf.toml'
timeout: float = 1.5
