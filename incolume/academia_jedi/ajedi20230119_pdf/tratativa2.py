import inspect

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import logging

import pdfplumber
import PyPDF2
from variaveis import file


def ex01():
    """Exemplo pypdf2 oriundo de https://towardsdatascience.com/how-to-extract-text-from-pdf-245482a96de7."""
    logging.debug(inspect.stack()[0][3].__doc__)
    fhandle = open(file, 'rb')
    pdfReader = PyPDF2.PdfReader(fhandle)
    pagehandle = pdfReader.pages[0]
    print(pagehandle.extract_text())


def ex02():
    """Exemplo pdfplumber oriundo de https://towardsdatascience.com/how-to-extract-text-from-pdf-245482a96de7."""
    logging.debug(inspect.stack()[0][3].__doc__)
    with pdfplumber.open(file) as pdf:
        first_page = pdf.pages[0]
        print(first_page.extract_text())


def ex03():
    """Exemplo pdfMiner3 oriundo de https://towardsdatascience.com/how-to-extract-text-from-pdf-245482a96de7."""
    logging.debug(inspect.stack()[0][3].__doc__)

    import io

    from pdfminer3.converter import TextConverter
    from pdfminer3.layout import LAParams
    from pdfminer3.pdfinterp import PDFPageInterpreter, PDFResourceManager
    from pdfminer3.pdfpage import PDFPage

    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(
        resource_manager,
        fake_file_handle,
        laparams=LAParams(),
    )
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(
            fh,
            caching=True,
            check_extractable=True,
        ):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    print(text)


def run():
    ex01()
    ex02()
    ex03()


if __name__ == '__main__':
    run()
