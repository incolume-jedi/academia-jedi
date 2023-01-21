from pathlib import Path
import logging


# PDF files
root = Path.cwd()
pdfdir = root.joinpath("data_files", "pdf")
assert pdfdir.is_dir(), f"Ops: {pdfdir} .."

pdffiles = list(pdfdir.glob("*.pdf"))
logging.debug(pdffiles)
file = pdffiles[0]
