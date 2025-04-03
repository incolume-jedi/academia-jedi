"""Module."""

import secrets
import string
from collections.abc import Generator

from incolume.academia_jedi import logger


class BadFormationError(ValueError):
    """BadFormationError class."""


def generate_random_str(length: int = 8) -> str:
    """Generate random str."""
    length = max(length, 8)
    chars: str = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def fuzzer() -> Generator:
    """Fuzzer."""
    while True:
        yield generate_random_str(max(1, secrets.randbelow(100)))


def sample_func(input_str: str) -> int:
    """Sample func."""
    try:
        if '!!!' in input_str:
            msg = 'Bad formation'
            raise BadFormationError(msg)
    except Exception as e:
        logger.exception('%s: %s', e.__class__.__name__, e)
        return 1
    return 0


def main():
    """Main."""
    for i, input_str in enumerate(fuzzer()):
        result: int = sample_func(input_str)

        if result != 0:
            logger.error(f'Ran #{i}: {input_str}')
            break


def run():
    """Run it."""
    logger.debug(generate_random_str())
    main()


if __name__ == '__main__':  # pragma: no cover
    run()
