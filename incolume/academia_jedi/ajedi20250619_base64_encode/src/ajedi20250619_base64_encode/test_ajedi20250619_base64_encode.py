"""Test module for ajedi20250619_base64_encode."""

from __future__ import annotations
from dataclasses import dataclass
from typing import NoReturn

import pytest
import ajedi20250619_base64_encode as pkg


@dataclass
class Entrance:
    """Entrance class for testes."""

    method: str
    value: str


class TestAjedi20250619Base64Encode:
    """Test class for ajedi20250619_base64_encode."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('', ''),
            pytest.param(
                'Tudo é difícil até fácil se tornar.',
                '5475646F20C3A920646966C3AD63696C206174C3A92066C3A163696C20736520746F726E61722E',
            ),
            pytest.param('Jesus te ama!', '4A6573757320746520616D6121'),
        ],
    )
    def test_base16(self, entrance, expected) -> None:
        """Test the main function."""
        assert pkg.base64.b16encode(entrance.encode()).decode() == expected, (
            f'Expected {expected} but got '
            f'{pkg.base64.b16encode(entrance.encode()).decode()}'
        )

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('', ''),
            pytest.param(
                'Tudo é difícil até fácil se tornar.',
                'VHVkbyDDqSBkaWbDrWNpbCBhdMOpIGbDoWNpbCBzZSB0b3JuYXIu',
            ),
            pytest.param('Jesus te ama!', 'SmVzdXMgdGUgYW1hIQ=='),
        ],
    )
    def test_base64_standard(self, entrance, expected) -> None:
        """Test the base64 encoding."""
        assert (
            pkg.base64.standard_b64encode(entrance.encode()).decode()
            == expected
        )

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                'https://github.com/incolume-jedi/academia-jedi/issues/287',
                'afasf',
            ),
            pytest.param(
                'Tudo é difícil até fácil se tornar.',
                'VHVkbyDDqSBkaWbDrWNpbCBhdMOpIGbDoWNpbCBzZSB0b3JuYXIu',
            ),
            pytest.param('Jesus te ama!', 'SmVzdXMgdGUgYW1hIQ=='),
        ],
    )
    def test_base64_urlsafe(self, entrance, expected) -> None:
        """Test the base64 encoding."""
        pkg.base64.urlsafe_b64encode(entrance.encode()).decode() == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                Entrance(
                    'urlsafe_b64encode',
                    'https://pypi.org/search/?q=base62&o=',
                ),
                'aHR0cHM6Ly9weXBpLm9yZy9zZWFyY2gvP3E9YmFzZTYyJm89',
            ),
            pytest.param(
                Entrance(
                    'standard_b64encode',
                    'Tudo é difícil até fácil se tornar.',
                ),
                'VHVkbyDDqSBkaWbDrWNpbCBhdMOpIGbDoWNpbCBzZSB0b3JuYXIu',
            ),
            pytest.param(
                Entrance('standard_b64encode', 'Jesus te ama!'),
                'SmVzdXMgdGUgYW1hIQ==',
            ),
            pytest.param(
                Entrance('b16encode', 'Tudo é difícil até fácil se tornar.'),
                '5475646F20C3A920646966C3AD63696C206174C3A92066C3A163696C20736520746F726E61722E',
            ),
            pytest.param(
                Entrance('b32encode', 'Tudo é difícil até fácil se tornar.'),
                'KR2WI3ZAYOUSAZDJM3B22Y3JNQQGC5GDVEQGNQ5BMNUWYIDTMUQHI33SNZQXELQ=',
            ),
            pytest.param(
                Entrance('a85encode', 'Tudo é difícil até fácil se tornar.'),
                "<-;_i+N(0$A8,YnX^c']+CTB0W?>fjTjqeQ+EM*:FDl2;@<*t",
            ),
            pytest.param(
                Entrance(
                    'b32hexencode',
                    'Tudo é difícil até fácil se tornar.',
                ),
                'AHQM8RP0OEKI0P39CR1QQOR9DGG62T63L4G6DGT1CDKMO83JCKG78RRIDPGN4BG=',
            ),
            pytest.param(
                Entrance('b64encode', 'Tudo é difícil até fácil se tornar.'),
                'VHVkbyDDqSBkaWbDrWNpbCBhdMOpIGbDoWNpbCBzZSB0b3JuYXIu',
            ),
            pytest.param(
                Entrance('encode', 'Tudo é difícil até fácil se tornar.'),
                'VHVkbyDDqSBkaWbDrWNpbCBhdMOpIGbDoWNpbCBzZSB0b3JuYXIu',
                marks=[
                    pytest.mark.skip(reason='Not ran. This is a placeholder.'),
                ],
            ),
            pytest.param(
                Entrance('encodebytes', 'Tudo é difícil até fácil se tornar.'),
                'VHVkbyDDqSBkaWbDrWNpbCBhdMOpIGbDoWNpbCBzZSB0b3JuYXIu\n',
            ),
            pytest.param(
                Entrance('z85encode', 'Tudo é difícil até fácil se tornar.'),
                'rcq.&aJ7f3wnbU[TZ=6YayPxfSut/<P<}!MaAI9pBz(hqvr9$',
            ),
        ],
    )
    def test_others(self, entrance, expected) -> NoReturn:
        """Test the others function."""
        func = getattr(pkg.base64, entrance.method)
        assert func(entrance.value.encode()).decode() == expected
