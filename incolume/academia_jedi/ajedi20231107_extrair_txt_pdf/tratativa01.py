"""Extrair texto com opencv e tesseract."""

import logging
from typing import Any

import cv2
import pytesseract
from pathlib import Path
from os import getenv, environ


__author__ = "@britodfbr"  # pragma: no cover

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
           '%(module)s;%(funcName)s;%(message)s',
)


def exemplo01(img_file: Path = None) -> Any:
    """Extrair texto ascii da imagem."""
    logging.debug(img_file)
    img = cv2.imread(img_file.as_posix())
    resultado = pytesseract.image_to_string(img).strip()
    logging.debug(resultado.strip())

    return resultado


def exemplo2(img_file: Path = None) -> Any:
    """Extrair texto utf8 da imagem.

    A base para portugues deve ser disponibilizada em
    /usr/share/tesseract-ocr/4.00/tessdata/por.traineddata.
    """
    tessdata = Path(__file__).parents[0].joinpath('./tessdata').resolve()
    environ['TESSDATA_PREFIX'] = tessdata.as_posix()
    logging.debug(tessdata.is_dir())
    logging.debug(img_file)
    img = cv2.imread(img_file.as_posix())

    resultado = pytesseract.image_to_string(img, lang='por').strip()
    return resultado


def exemplo3(img_file: Path = None) -> Any:
    """Extrair texto utf8 da imagem.

    A base para portugues deve ser disponibilizada em
    /usr/share/tesseract-ocr/4.00/tessdata/por.traineddata."""

    logging.debug(img_file)
    img = cv2.imread(img_file.as_posix())

    resultado = pytesseract.image_to_string(img, lang='por')
    print(resultado.strip())
    return resultado
