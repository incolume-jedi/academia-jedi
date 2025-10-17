"""Module."""

from __future__ import annotations

import asyncio
import contextlib
import sys
from pathlib import Path

if sys.version_info < (3, 11):
    with contextlib.suppress(SystemExit):
        sys.exit('This application need Python 3.11+')


class AnotherError(Exception):
    """Another one Exception."""


async def read_file(filename: str | Path) -> str:
    """Async read file."""
    with Path(filename).open() as f:
        data: str = f.read()
    return data


async def fetch_data(data: int) -> dict:
    """Async fetch data."""
    if data == 0:
        msg = 'No data found.'
        raise AnotherError(msg)
    return {'data': data}


async def main() -> None:
    """Main async."""
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(read_file('anime.png'))
            tg.create_task(read_file('icon.png'))
            tg.create_task(read_file('python.png'))
            tg.create_task(read_file('file.png'))
            tg.create_task(fetch_data(0))
        print('Completed.')
    except* FileNotFoundError as eg:
        for error in eg.exceptions:
            print(error)
    except* AnotherError as e:
        print(e.exceptions)


if __name__ == '__main__':  # pragma: no cover
    asyncio.run(main())
