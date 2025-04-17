"""Module."""

import asyncio

from incolume.academia_jedi.ajedi20230112_async import ex02, ex04

if __name__ == '__main__':  # pragma: no cover
    ex02.run()
    asyncio.run(ex04.run())
