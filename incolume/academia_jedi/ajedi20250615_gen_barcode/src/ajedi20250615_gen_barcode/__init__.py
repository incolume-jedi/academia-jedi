"""Generate barcode in Python."""

from __future__ import annotations

from pathlib import Path

import barcode
import barcode.writer
from icecream import ic


def gen_barcode(
    code: str,
    fileoutput: Path | None = None,
    diroutput: Path | None = None,
    padron: str = 'upc',
) -> bool:
    """Generate barcode."""
    msg = 'UPC must have 11 digits, not more.'
    if padron == 'upc' and len(code) > 13:  # noqa: PLR2004
        raise ValueError(msg)

    diroutput = diroutput or Path()
    fileoutput = fileoutput or diroutput / f'{code}.png'

    ic(fileoutput)
    handler = barcode.get_barcode_class(padron)
    obj = handler(code, writer=barcode.writer.ImageWriter())
    ic(obj.save(fileoutput.with_suffix('')))
    return True


def main() -> str:  # pragma: no cover
    """Generate barcode in Python."""
    gen_barcode('123456789098')
    gen_barcode('314159265358')
    gen_barcode('987412563210')
    return 'Hello from ajedi20250615-gen-barcode!'


if __name__ == '__main__':
    main()
