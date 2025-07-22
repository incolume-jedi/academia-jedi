"""Estudos com pacote segno."""

from __future__ import annotations

from pathlib import Path

import segno


def generate_qr_code(data: str, filename: str, **kwargs: object) -> Path:
    """Generate a QR code and save it to a file."""
    if kwargs and not any(x in kwargs for x in ['scale', 'dark', 'light']):
        msg = (
            "At least one of 'scale', 'dark',"
            " or 'light' must be specified in kwargs."
        )
        raise ValueError(msg)

    qr = segno.make(data)
    qr.save(filename, **kwargs)
    return Path(filename)
