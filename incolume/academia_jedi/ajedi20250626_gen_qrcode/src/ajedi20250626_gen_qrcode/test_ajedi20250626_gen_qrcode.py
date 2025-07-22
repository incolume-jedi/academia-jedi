"""Module testing ajedi20250626-gen-qrcode."""

from __future__ import annotations
from inspect import stack
from pathlib import Path
import shutil
from tempfile import tempdir
from typing import ClassVar

import pytest
from . import with_segno, with_qrcode
from dataclasses import dataclass, fields


@dataclass
class EntranceQRCode:
    """Data class for entrance."""

    data: str
    filename: str = 'test_qrcode.png'
    version: int | None = None
    box_size: int | None = None
    border: int | None = None
    fill_color: str | None = None
    back_color: str | None = None

    def keys(self):
        """Return the names of the fields in the dataclass."""
        return (
            f.name
            for f in fields(self)
            if f.name == 'light' or getattr(self, f.name) is not None
        )

    def __getitem__(self, item):
        """Return the value of the given attribute name."""
        return getattr(self, item)


@dataclass
class EntranceSegno:
    """Data class for entrance."""

    data: str
    filename: str = 'test_segno.png'
    scale: int | None = None
    dark: str | None = None
    light: str | None = None

    def keys(self):
        """Return the names of the fields in the dataclass."""
        return (
            f.name
            for f in fields(self)
            if f.name == 'light' or getattr(self, f.name) is not None
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
        shutil.rmtree(cls.PATH / '', ignore_errors=True)

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                '',
                marks=[pytest.mark.xfail(reason='Not implemented')],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno0.png',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno1.png',
                    scale=10,
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno2.png',
                    light=None,
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno3.png',
                    dark='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno4.pdf',
                    scale=10,
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno5.svg',
                    scale=10,
                    dark='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno6.svg',
                    scale=10,
                    dark='blue',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno7.svg',
                    scale=10,
                    dark='blue',
                    light='black',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno8.svg',
                    scale=30,
                    dark='black',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno9.svg',
                    scale=30,
                    dark='white',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno10.svg',
                    scale=30,
                    dark='white',
                    light='black',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceSegno(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_segno11.svg',
                    scale=30,
                    dark='white',
                    light='blue',
                ),
                marks=[],
            ),
        ],
    )
    def test_with_segno(self, entrance) -> None:
        """Test the main function."""
        result = with_segno.generate_qr_code(**entrance)
        assert result.is_file()

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                '',
                marks=[pytest.mark.xfail(reason='Not implemented')],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode0.png',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode1.png',
                    box_size=10,
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode2.png',
                    back_color=None,
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode3.png',
                    fill_color='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode4.png',
                    box_size=10,
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode5.svg',
                    box_size=10,
                    fill_color='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode6.svg',
                    box_size=10,
                    fill_color='blue',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode7.svg',
                    box_size=10,
                    fill_color='blue',
                    back_color='black',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode8.svg',
                    box_size=30,
                    fill_color='black',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode9.svg',
                    box_size=30,
                    fill_color=(100, 100, 100),  # RGB tuple
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode10.svg',
                    box_size=30,
                    fill_color='white',
                    back_color='black',
                ),
                marks=[],
            ),
            pytest.param(
                EntranceQRCode(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode11.svg',
                    box_size=30,
                    fill_color='white',
                    back_color='blue',
                    border=1,
                ),
                marks=[],
            ),
        ],
    )
    def test_with_qrcode(self, entrance) -> None:
        """Test the main function."""
        result = with_qrcode.generate_qr_code(**entrance)
        assert result.is_file()
