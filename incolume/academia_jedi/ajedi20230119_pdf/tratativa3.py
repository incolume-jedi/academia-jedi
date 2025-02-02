"""Converter PDF para Imagem

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/.

sudo apt install poppler-utils
"""

import logging
from pathlib import Path
from typing import Final

from pdf2image import convert_from_path
from variaveis import pdffiles

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


print(pdffiles)
PDFFILE: Final[Path] = pdffiles[0]
print(PDFFILE)


def tratativa1(pdffile: (Path | str) = ''):
    pdffile = pdffile or PDFFILE
    logging.debug(pdffile)
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdffile)

    for i in range(len(images)):
        print('Save pages as images in the pdf')
        images[i].save('page' + str(i) + '.jpg', 'JPEG')


def tratativa2():
    from pdf2image import convert_from_path

    print(PDFFILE)
    pages = convert_from_path(PDFFILE)
    directory = Path(__file__).parent / 'images'
    print(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(pages, 1):
        page.save(directory / f'out{i:02}.jpg', 'JPEG')


def tratativa3():
    from pdf2image import convert_from_path

    print(PDFFILE)
    pages = convert_from_path(PDFFILE)
    directory = Path(__file__).parent / 'images'
    print(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(pages, 1):
        page.save(directory / f'out{i:02}.png', 'PNG')


def run():
    tratativa3()


if __name__ == '__main__':
    run()
