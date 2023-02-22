"""

Faz-se necessário instalar o binário no OS:
sudo apt install tesseract-ocr
"""
import cv2
import pytesseract
from pathlib import Path
import logging


def exemplo1()-> None:
    """"""
    img_file = Path(__file__).parent.joinpath('images', 'img2.png')
    logging.debug(img_file)

    img = cv2.imread(img_file.as_posix())

    resultado = pytesseract.image_to_string(img)
    print(resultado.strip())


def exemplo2()->None:
    """
    
    A base para portugues deve ser disponibilizada em /usr/share/tesseract-ocr/4.00/tessdata/por.traineddata
    """
    img_file = Path(__file__).parent.joinpath('images', 'img3.png')
    logging.debug(img_file)

    img = cv2.imread(img_file.as_posix())

    resultado = pytesseract.image_to_string(img, lang='por')
    print(resultado.strip())


def run():
    exemplo1()
    exemplo2()

if __name__ == '__main__':
    run()
