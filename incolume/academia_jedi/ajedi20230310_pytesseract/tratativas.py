import logging
import typing
from pathlib import Path

from pdf2image import convert_from_path
from pytesseract import image_to_string

PDFDIR: typing.Final = Path(__file__).parents[3] / 'data_files' / 'pdf'
PDFFILES: list[Path] = list(PDFDIR.glob('*.pdf'))


def convert_pdf_to_image(pdf_file):
    """"""
    img = convert_from_path(pdf_file)
    logging.debug(img)
    return img


def convert_image_to_text(file):
    """"""
    text = image_to_string(file)
    logging.debug(text)
    return text


def get_txt_from_any_pdf(pdf_file):
    """"""
    images = convert_pdf_to_image(pdf_file)
    final_text = ''
    for img in images:
        final_text += convert_image_to_text(img)
    return final_text


def tratativa1():
    """Estrutura arquivos PDF."""
    logging.debug(PDFDIR)
    logging.debug(PDFDIR.exists())
    logging.debug([str(x) for x in PDFFILES])


def tratativa2():
    """Listar arquivos PDF."""
    for file in PDFFILES:
        print(file)


def tratativa3():
    """PDF2TXT."""
    for file in PDFFILES[:1]:
        logging.debug(f'{type(file)} {file}')
        get_txt_from_any_pdf(file.as_posix())


def run():
    """Running it."""
    functions: list[typing.Callable] = [
        value
        for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        print(f'    >>> {func.__doc__}')
        try:
            if result := func():
                print(result)
        except (TypeError, ValueError) as e:
            logging.exception(f'{e.__class__.__name__}: {e}')
        finally:
            logging.debug(f'{func.__name__} finalizada.')
        print('------\n')


if __name__ == '__main__':
    run()
