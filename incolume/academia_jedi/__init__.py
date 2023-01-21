try:
    from tomli import load
except (ModuleNotFoundError, ImportError):
    from tomllib import load

from pathlib import Path

versionfile = Path(__file__).parent / "version.txt"

with Path(__file__).parents[2].joinpath("pyproject.toml").open("rb") as file:
    versionfile.write_text(f"{load(file)['tool']['poetry']['version']}\n")

__version__ = versionfile.read_text().strip()
