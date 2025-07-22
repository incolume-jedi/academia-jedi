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


class TestAjedi20250626GenQRCodeSegno(TestAjedi20250626GenQRCode):
    """Test class for ajedi20250626-gen-qrcode with segno."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)

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
                f.name
                for f in fields(self)
                if f.name == 'light' or getattr(self, f.name) is not None
            )

        def __getitem__(self, item):
            """Return the value of the given attribute name."""
            return getattr(self, item)

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                '',
                marks=[pytest.mark.xfail(reason='Not implemented')],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode0.png',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode1.png',
                    scale=10,
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode2.png',
                    light=None,
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode3.png',
                    dark='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode4.pdf',
                    scale=10,
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode5.svg',
                    scale=10,
                    dark='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode6.svg',
                    scale=10,
                    dark='blue',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode7.svg',
                    scale=10,
                    dark='blue',
                    light='black',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode8.svg',
                    scale=30,
                    dark='black',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode9.svg',
                    scale=30,
                    dark='white',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode10.svg',
                    scale=30,
                    dark='white',
                    light='black',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode11.svg',
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


class TestAjedi20250626GenQRCodeQrcode(TestAjedi20250626GenQRCode):
    """Test class for ajedi20250626-gen-qrcode with qrcode."""

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                '',
                marks=[pytest.mark.xfail(reason='Not implemented')],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode0.png',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode1.png',
                    scale=10,
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode2.png',
                    light=None,
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode3.png',
                    dark='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode4.pdf',
                    scale=10,
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode5.svg',
                    scale=10,
                    dark='darkblue',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode6.svg',
                    scale=10,
                    dark='blue',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode7.svg',
                    scale=10,
                    dark='blue',
                    light='black',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode8.svg',
                    scale=30,
                    dark='black',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode9.svg',
                    scale=30,
                    dark='white',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode10.svg',
                    scale=30,
                    dark='white',
                    light='black',
                ),
                marks=[],
            ),
            pytest.param(
                Entrance(
                    'Tudo é difícil até fácil se tornar.',
                    PATH / 'test_qrcode11.svg',
                    scale=30,
                    dark='white',
                    light='blue',
                ),
                marks=[],
            ),
        ],
    )
    def test_with_qrcode(self, entrance) -> None:
        """Test the main function."""
        result = with_qrcode.generate_qr_code(**entrance)
        assert result.is_file()
