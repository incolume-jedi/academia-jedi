"""Tests for ajedi20250621_token_shortener."""

import pytest
from dataclasses import dataclass, field
import base64
import secrets
from types import ModuleType
from icecream import ic  # type: ignore[import-untyped]


@dataclass
class Entrance:
    """Entrance data class."""

    module: ModuleType = field(default=secrets)
    method: str = field(default='token_urlsafe')
    value: str = field(default=None)

@dataclass
class MockSecrets:
    """Mock secrets module for testing."""

    @classmethod
    def token_urlsafe(cls, *args: str, **kwargs: str) -> str:
        """Mock token_urlsafe method."""
        ic(args, kwargs)
        end = 7 if (args[0] or kwargs.get('nbytes')) else None
        return 'KneJ3JLV7ZnkwAEmdqwAzLKvrMHhuFMIs46WAlHid-E'[:end]

    @classmethod
    def token_hex(cls, *args: str, **kwargs: str) -> str:
        """Mock token_urlsafe method."""
        ic(args, kwargs)
        return '5513c2dd07'

    @classmethod
    def randbelow(cls, *args: str, **kwargs: str) -> int:
        """Mock randbelow method."""
        ic(args, kwargs)
        return 4

    @classmethod
    def randbits(cls, *args: str, **kwargs: str) -> int:
        """Mock randbits method."""
        ic(args, kwargs)
        return 12397

    @classmethod
    def token_bytes(cls, *args: str, **kwargs: str) -> bytes:
        """Mock token_bytes method."""
        ic(args, kwargs)
        return b'\xed\xda9\xac\x9a'


class TestAjedi20250621TokenShortener:
    """Test class for ajedi20250621_token_shortener."""

    @pytest.fixture(scope='class')
    def entrance(self) -> Entrance:
        """Fixture to provide entrance data."""
        import ajedi20250621_token_shortener as module

        return Entrance(
            module=module,
            method='main',
            value='Hello from ajedi20250621-token-shortener!',
        )

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                '',
                '',
                marks=[pytest.mark.xfail(reason='This test is a boilerplate')],
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='b32hexencode',
                    value='Hello from ajedi20250621-token-shortener!',
                ),
                '91IMOR3F41J74RRD41GMKPB4D4P30CHL60R34C9DEHNMMPBE5LPMGRRIEHIMSPBI44======',
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='a85encode',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                'BQS?8F#ks-Ci<flChRa.F>%0=B4Z.+/R`dDBJ2(q1G<llATBGHF(KAH1,CS)BONJM0etD"AThX*',
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='b16encode',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                '68747470733A2F2F6C6F63616C686F73742F6469676573742D617574682F3132332F757365722F757365723132332F7368612D3531322F6E65766572',
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='b32hexencode',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                'D1Q78S3J78NIUR3FCDGMOQ3FEDQ2UP39CTIN6T1DC5QN8Q1F64P36BRLEDIN4BRLEDIN4C9I6CNN6Q315KQJ2CHFDPINCPBI',
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='b64encode',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                'aHR0cHM6Ly9sb2NhbGhvc3QvZGlnZXN0LWF1dGgvMTIzL3VzZXIvdXNlcjEyMy9zaGEtNTEyL25ldmVy',
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='encodebytes',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                'aHR0cHM6Ly9sb2NhbGhvc3QvZGlnZXN0LWF1dGgvMTIzL3VzZXIvdXNlcjEyMy9zaGEtNTEyL25l\ndmVy\n',
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='standard_b64encode',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                'aHR0cHM6Ly9sb2NhbGhvc3QvZGlnZXN0LWF1dGgvMTIzL3VzZXIvdXNlcjEyMy9zaGEtNTEyL25ldmVy',
            ),
            pytest.param(
                Entrance(
                    module=base64,
                    method='z85encode',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                'xMOunB2>%cy&r/(y?N:dBt4fsxjVdaeN-^zxFh7}gCr((wPxCDB7GwDgbyO8xKJFIf!$z1wP?T9',
            ),
        ],
    )
    def test_generate_token_base64(self, entrance, expected):
        """Test the generate_token method."""
        func = getattr(entrance.module, entrance.method)
        assert func(entrance.value.encode()).decode() == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                '',
                '',
                marks=[
                    pytest.mark.xfail(reason='This test is a boilerplate.'),
                ],
            ),
            pytest.param(
                Entrance(
                    module=secrets,
                    method='choice',
                    value='https://localhost/digest-auth/123/user/user123/sha-512/never',
                ),
                99,
                marks=pytest.mark.skip,
            ),
            pytest.param(
                Entrance(module=secrets, method='randbelow', value=5),
                4,
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(module=secrets, method='randbits', value=15),
                12397,
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(module=secrets, method='token_bytes', value=5),
                b'\xed\xda9\xac\x9a',
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(module=secrets, method='token_hex', value=5),
                '5513c2dd07',
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(module=secrets, method='token_urlsafe', value=5),
                'KneJ3JL',
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                Entrance(),
                'KneJ3JLV7ZnkwAEmdqwAzLKvrMHhuFMIs46WAlHid-E',
            ),
        ],
    )
    def test_generate_token_secrets(self, entrance, expected, monkeypatch):
        """Test the generate_token method."""
        monkeypatch.setattr(
            secrets,
            entrance.method,
            getattr(MockSecrets, entrance.method),
        )

        func = getattr(entrance.module, entrance.method)
        assert func(entrance.value) == expected

