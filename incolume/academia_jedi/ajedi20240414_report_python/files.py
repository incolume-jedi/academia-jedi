"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import logging
from pathlib import Path
from tempfile import gettempdir

from icecream import ic


def realfilename(
    filebase: str | Path,
    *,
    ext: str = '',
    digits: int = 1,
    count: int = 1,
    separador: bool = True,
) -> Path:
    """Return real file name for filebase.

    :param filebase: str|pathlib.Path: filename or filebase name or full path
    :param ext: str: extension desert, default (txt)
    :param digits: int: digits of sequence, default 2
    :param count: int, default 0
    :param separador: bool: default (True)
    :return: pathlib.Path: real filename tip.
    """
    filebase = Path(filebase)
    suffixes = filebase.suffixes or ['.txt']
    ext = f'.{ext.strip(".")}' if ext else ''.join(suffixes)
    sep = '_' if separador else ''
    basename = filebase.stem.split('.')[0]
    while True:
        dig = f'{count}'.zfill(digits)

        result = filebase.with_name(
            f'{basename}{sep}{dig}',
        ).with_suffix(
            f'{ext}',
        )
        result.parent.mkdir(parents=True, exist_ok=True, mode=0o755)
        if not result.is_file():
            ic(f'Suggested name: {result}')
            logging.info('Suggested name: %s', result)
            return result
        count += 1


if __name__ == '__main__':  # pragma: no cover
    file = Path(gettempdir()) / 'fisco.tar.gz'
    realfilename('pulo').write_text('')
    realfilename('tuto').write_text('')
    realfilename('tox', digits=2).write_text('')
    realfilename('tox', ext='cpp').write_text('')
    realfilename('file.asm', separador=False, digits=2).write_text('')
    realfilename(file, separador=False, count=0, digits=2).write_text('')
