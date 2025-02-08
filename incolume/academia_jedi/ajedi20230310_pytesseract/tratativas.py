import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
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
