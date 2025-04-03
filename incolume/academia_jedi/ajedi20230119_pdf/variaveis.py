"""Module."""

from pathlib import Path

from icecream import ic
from incolume.academia_jedi import logger

pdfdir = Path(__file__).parents[3].joinpath('data_files', 'pdf')
ic(pdfdir)

pdffiles = sorted(pdfdir.glob('*.pdf'))
logger.debug(pdffiles)
file = pdffiles[0]

if __name__ == '__main__':
    # PDF files
    assert pdfdir.is_dir(), f'Ops: {pdfdir} ..'  # noqa: S101
