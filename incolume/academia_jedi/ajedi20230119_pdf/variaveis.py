import logging
from pathlib import Path

# PDF files
root = Path.cwd()
pdfdir = root.resolve().parents[2].joinpath('data_files', 'pdf')
assert pdfdir.is_dir(), f'Ops: {pdfdir} ..'

pdffiles = sorted(pdfdir.glob('*.pdf'))
logging.debug(pdffiles)
file = pdffiles[0]
