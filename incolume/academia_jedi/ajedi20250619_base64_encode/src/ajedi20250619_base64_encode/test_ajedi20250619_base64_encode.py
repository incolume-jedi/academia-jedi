"""Test module for ajedi20250619_base64_encode."""

from __future__ import annotations

import pytest
import ajedi20250619_base64_encode as pkg


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
