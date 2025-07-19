"""Estudos de compactação de arquivos com Python."""

from __future__ import annotations

import gzip
import logging
from pathlib import Path


def compress_file(input_file: str | Path, output_file: str | Path) -> bool:
    """Compress a file using gzip."""
    input_file = (
        Path(input_file) if isinstance(input_file, str) else input_file
    )
    output_file = (
        Path(output_file) if isinstance(output_file, str) else output_file
    )
    try:
        with (
            input_file.open('rb') as f_in,
            gzip.open(output_file, 'wb') as f_out,
        ):
            f_out.write(f_in.read())
    except (FileNotFoundError, Exception) as e:
        msg = f'Error compressing file: {e}'
        logging.exception(msg)
        return False
    return True


def main() -> None:
    """Hello from ajedi20250625-compact-files-py!"""


if __name__ == '__main__':
    main()
