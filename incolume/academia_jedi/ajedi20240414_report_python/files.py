"""Module."""

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
