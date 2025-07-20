"""Module testing ajedi20250626-gen-qrcode."""

from __future__ import annotations
from inspect import stack
from pathlib import Path
import shutil
from tempfile import tempdir
from typing import ClassVar

import pytest
from . import with_segno
from dataclasses import dataclass, fields


@dataclass
class Entrance:
    """Data class for entrance."""

    data: str
    filename: str = 'test_qrcode.png'
    scale: int | None = None
    dark: str | None = None
    light: str | None = None

    def keys(self):
        """Return the names of the fields in the dataclass."""
        return (
            f.name for f in fields(self) if getattr(self, f.name) is not None
        )

    def __getitem__(self, item):
        """Return the value of the given attribute name."""
        return getattr(self, item)


class TestAjedi20250626GenQRCode:
    """Test class for ajedi20250626-gen-qrcode."""

    PATH: ClassVar = Path(tempdir, stack()[0][3])

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.PATH.joinpath(stack()[0][3]).mkdir(
            parents=True,
            exist_ok=True,
        )

    @classmethod
    def teardown_class(cls):
        """Teardown class.

        Teardown da classe. Remove todos os arquivos
         e diretórios gerados ao final.
        """
        shutil.rmtree(cls.PATH, ignore_errors=True)

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                '',
                '',
                marks=[pytest.mark.xfail(reason='Not implemented')],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode.png',
                ),
                'QR code saved as test_qrcode.png',
                marks=[],
            ),
        ],
    )
    def test_with_segno(self, entrance, expected) -> None:
        """Test the main function."""
        assert with_segno.generate_qr_code(**entrance) == expected
