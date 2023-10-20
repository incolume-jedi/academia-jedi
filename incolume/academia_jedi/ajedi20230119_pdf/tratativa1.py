# importing required modules
import inspect
import logging

import fitz  # pyMuPDF
import PyPDF2
from variaveis import file


def ex01():
    """Exemplo atualizado de https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/."""

    logging.debug(inspect.stack()[0][3].__doc__)

    # creating a pdf file object
    pdfFileObj = open(file, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # printing number of pages in pdf file
    print(len(pdfReader.pages))

    # creating a page object
    pageObj = pdfReader.pages[0]

    # extracting text from page
    print(pageObj.extract_text())

    # closing the pdf file object
    pdfFileObj.close()


def ex02():
    """Exemplo adaptado de https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/."""
    logging.debug(inspect.stack()[0][3].__doc__)

    # creating a pdf file object
    with open(file, 'rb') as pdfFileObj:
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        # printing number of pages in pdf file
        print(len(pdfReader.pages))

        # creating a page object
        pageObj = pdfReader.pages[0]

        # extracting text from page
        print(pageObj.extract_text())


def ex03():
    """Exemplo PyMUPDF oriundo de https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/."""
    logging.debug(inspect.stack()[0][3].__doc__)
    doc = fitz.open(file)
    text = ''
    for page in doc:
        text += page.get_text()
    print(text)


def ex04():
    """Exemplo PyMUPDF baseado de https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/."""
    logging.debug(inspect.stack()[0][3].__doc__)
    with fitz.open(file) as doc:
        print(''.join([page.get_text() for page in doc]))


def run():
    ex01()
    ex02()
    ex03()
    ex04()


if __name__ == '__main__':
    run()
