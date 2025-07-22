"""Estudos com pacote qrcode."""

from __future__ import annotations

from pathlib import Path

import qrcode
from icecream import ic


def generate_qr_code(
    data: str,
    filename: str | Path,
    **kwargs: object,
) -> Path:
    """Generate a QR code and save it to a file."""
    ic(f'{data=}{filename=}{kwargs=}')
    if kwargs and not any(
        x in kwargs
        for x in [
            'version',
            'box_size',
            'border',
            'fill_color',
            'back_color',
        ]
    ):
        msg = (
            "At least one of  'version', 'box_size', 'border', "
            "'fill_color' or 'back_color' must be specified in kwargs."
        )
        raise ValueError(msg)
    border = kwargs.get('border', 4)
    box_size = kwargs.get('box_size', 10)
    fill_color = kwargs.get('fill_color', 'black')
    back_color = kwargs.get('back_color', 'white')
    version = kwargs.get('version', 1)
    error_correction = kwargs.get(
        'error_correction',
        qrcode.constants.ERROR_CORRECT_L,
    )
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data=data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

    return Path(filename)
