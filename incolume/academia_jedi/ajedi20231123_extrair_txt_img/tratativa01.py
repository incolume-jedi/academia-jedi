"""Extrair texto com opencv e tesseract."""

import logging
from os import environ
from pathlib import Path

import cv2
import pytesseract

__author__ = '@britodfbr'  # pragma: no cover

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def exemplo01(img_file: Path | None = None) -> str:
    """Extrair texto ascii da imagem."""
    logging.debug(img_file)
    img = cv2.imread(img_file.as_posix())
    resultado = pytesseract.image_to_string(img).strip()
    logging.debug(resultado.strip())

    return resultado


def exemplo02(img_file: Path | None = None) -> str:
    """Extrair texto utf8 da imagem.

    A base para portugues deve ser disponibilizada em
    /usr/share/tesseract-ocr/4.00/tessdata/por.traineddata.
    """
    tessdata = Path(__file__).parents[0].joinpath('./tessdata').resolve()
    environ['TESSDATA_PREFIX'] = tessdata.as_posix()
    logging.debug(tessdata.is_dir())
    logging.debug(img_file)
    img = cv2.imread(img_file.as_posix())

    return pytesseract.image_to_string(img, lang='por').strip()


def exemplo03(img_file: Path | None = None) -> str:
    """Extrair texto utf8 da imagem.

    A base para portugues deve ser disponibilizada em
    /usr/share/tesseract-ocr/4.00/tessdata/por.traineddata.
    """
    logging.debug(img_file)
    img = cv2.imread(img_file.as_posix())

    resultado = pytesseract.image_to_string(img, lang='por')
    logging.debug(resultado.strip())
    return resultado
