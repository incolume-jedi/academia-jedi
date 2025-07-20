"""Estudos com pacote segno."""

from __future__ import annotations

import segno


def generate_qr_code(data: str, filename: str, **kwargs: object) -> str:
    """Generate a QR code and save it to a file."""
    if kwargs and not any(x in kwargs for x in ['scale', 'dark', 'light']):
        raise ValueError(
            "At least one of 'scale', 'dark', or 'light' must be specified in kwargs.",
        )

    qr = segno.make(data)
    qr.save(filename, **kwargs)
    return f'QR code saved as {filename}'
