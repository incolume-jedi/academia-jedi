"""Prospecção do pacote aspose.words."""


import logging
import platform
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Union

import aspose.words as aw

# if platform.python_version() >= '3.12.0':
#     msg = f'This module ({Path.cwd()}) not run on Python 3.12+!'
#     print(msg)
#     logging.info(msg)
#     sys.exit(0)

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

def new_filename(**kwargs: str) -> Path:
    """Name file.

    mode='w+b',
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    delete=True,
    """
    return Path(NamedTemporaryFile(**kwargs).name)


def example1(output_file: Union[Path, str] = 'output.docx') -> bool:
    """Exemple oficial.

    aspose-words em https://pypi.org/project/aspose-words/
    """
    output_file = Path(output_file)

    # Create a blank document.
    doc = aw.Document()

    # Use a document builder to add content to the document.
    builder = aw.DocumentBuilder(doc)
    # Write a new paragraph in the document with the text "Hello World!".
    builder.writeln('Hello, World!')

    # Save the document in DOCX format. Save format is automatically
    # determined from the file extension.
    doc.save(output_file.as_posix())


def example2(filein: Union[Path, str], fileout: Union[Path, str]) -> None:
    """Example2."""
    filein = Path(filein)
    fileout = Path(fileout)
    # Load the document from the disc.
    doc = aw.Document(filein.as_posix())

    # Save the document to HTML format.
    doc.save(fileout.as_posix())


def run() -> None:
    """Run it."""
    example1()

    pdfin = (
        Path(__file__).parents[3] / 'data_files' / 'pdf' / 'Illustrator.pdf'
    )
    example2(filein='output.docx', fileout='output.html')
    example2(filein=pdfin.as_posix(), fileout='output2.html')
    example2(filein=pdfin.as_posix(), fileout='output2.docx')


if __name__ == '__main__':
    run()
