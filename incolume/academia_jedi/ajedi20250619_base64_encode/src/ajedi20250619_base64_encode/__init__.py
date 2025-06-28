"""Estudos sobre base64."""

from __future__ import annotations

import base64

from icecream import ic


def main() -> None:  # pragma: no cover
    """Estudos sobre base64."""
    ic(base64.b16encode(b'Hello from ajedi20250619-base64-encode!'))


if __name__ == '__main__':
    main()
