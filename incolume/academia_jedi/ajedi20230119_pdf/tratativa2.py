import inspect
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
