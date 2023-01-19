
# importing required modules
import PyPDF2
from pathlib import Path
import logging
import inspect

    
#PDF files
root = Path.cwd()
pdfdir = root.joinpath('data_files', 'pdf')
assert pdfdir.is_dir(), f"Ops: {pdfdir} .."

pdffiles = pdfdir.glob('*.pdf')
file = list(pdffiles)[0]

def ex01():
    """Exemplo atualizado de https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/."""

    logging.debug(ex01.__doc__)

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
    logging.debug(ex01.__doc__)
    
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



def run():
    ex01()
    ex02()


if __name__ == '__main__':
    run()
