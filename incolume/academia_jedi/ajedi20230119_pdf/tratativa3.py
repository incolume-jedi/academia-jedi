"""Converter PDF para Imagem.

https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/.

sudo apt install poppler-utils
"""
# ruff: noqa: T201

from pathlib import Path
from typing import Final

from incolume.academia_jedi import logger
from incolume.academia_jedi.ajedi20230119_pdf.variaveis import pdffiles
from pdf2image import convert_from_path

print(pdffiles)
PDFFILE: Final[Path] = pdffiles[0]
print(PDFFILE)


def tratativa1(pdffile: (Path | str) = '') -> None:
    """Tratativa."""
    pdffile = pdffile or PDFFILE
    logger.debug(pdffile)
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdffile)

    for i in range(len(images)):
        print('Save pages as images in the pdf')
        images[i].save('page' + str(i) + '.jpg', 'JPEG')


def tratativa2():
    """Tratativa."""
    from pdf2image import convert_from_path

    print(PDFFILE)
    pages = convert_from_path(PDFFILE)
    directory = Path(__file__).parent / 'images'
    print(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(pages, 1):
        page.save(directory / f'out{i:02}.jpg', 'JPEG')


def tratativa3():
    """Tratativa."""
    from pdf2image import convert_from_path

    print(PDFFILE)
    pages = convert_from_path(PDFFILE)
    directory = Path(__file__).parent / 'images'
    print(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(pages, 1):
        page.save(directory / f'out{i:02}.png', 'PNG')


def run():
    """Run it."""
    tratativa3()


if __name__ == '__main__':
    run()
