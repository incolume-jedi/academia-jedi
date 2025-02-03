"""Extrair texto de imagem.


cv2 + pytesseract

Faz-se necessário instalar o binário no OS:
sudo apt install tesseract-ocr.

"""

import logging
from pathlib import Path

import cv2
import pytesseract

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293


def exemplo1() -> None:
    """"""
    img_file = Path(__file__).parent.joinpath('images', 'img2.png')
    logging.debug(img_file)

    img = cv2.imread(img_file.as_posix())

    resultado = pytesseract.image_to_string(img)
    print(resultado.strip())


def exemplo2() -> None:
    """A base para portugues deve ser disponibilizada em /usr/share/tesseract-ocr/4.00/tessdata/por.traineddata."""
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
