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

