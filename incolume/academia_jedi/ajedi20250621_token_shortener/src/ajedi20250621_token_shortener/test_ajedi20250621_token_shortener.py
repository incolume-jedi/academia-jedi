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
