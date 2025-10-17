"""utils for submodule."""

import tempfile
from functools import wraps
from pathlib import Path
from typing import Any

import httpx
from icecream import ic

dout = Path(tempfile.gettempdir()) / Path(__file__).parent.stem


def nonexequi(*, suppress: bool = True) -> Any:
    """Decorator nonexequi."""

    def wrapper(func: callable) -> None:
        """Wrapper function."""

        @wraps(func)
        def inner(*args: str, **kwargs: str) -> None:
            """Action."""
            if suppress:
                ic(f'Supressed: {func.__name__}({args}, {kwargs})')
                return None
            return func(*args, **kwargs)

        return inner

    return wrapper


def config(content_index: str = '', dout: Path = dout) -> Path:
    """Config it."""
    dsite: Path = dout / 'site-fake'
    dsite.mkdir(parents=True, exist_ok=True)
    site = dsite / 'index.html'
    dsite.joinpath('favicon.ico').write_bytes(
        Path(__file__)
        .parents[2]
        .joinpath('data_files', 'ico', 'favicon2.ico')
        .read_bytes(),
    )
    site.write_text(content_index, encoding='utf-8')
    return site


def filename(**kwargs: [str, Any]) -> Path:
    """Filename.

    Args:
        kwargs:
          contains:
            mode: OpenBinaryMode = "w+b",
            buffering: int = -1,
            encoding: str | None = None,
            newline: str | None = None,
            suffix: AnyStr@NamedTemporaryFile = .png,
            prefix: AnyStr@NamedTemporaryFile = print-screen-,
            dir: GenericPath[AnyStr@NamedTemporaryFile] = $OSTEMPFILEDIR,
            delete: bool = True,
            errors: str | None = None

    """
    args: dict[str, Any] = {
        'mode': kwargs.get('mode', 'w+b'),
        'buffering': kwargs.get('buffering', -1),
        'encoding': kwargs.get('encoding'),
        'suffix': kwargs.get('suffix', '.png'),
        'prefix': kwargs.get('prefix', 'print-screen-'),
        'dir': kwargs.get('dir', dout),
        'delete': kwargs.get('delete', True),
        'errors': kwargs.get('errors'),
    }
    with tempfile.NamedTemporaryFile(**args) as fl:
        return fl.name


def check_web_resource(url: str = 'http://localhost:8000') -> bool:
    """Check if web resource activate."""
    try:
        response = httpx.get(url)
        ic(response.status_code)
        response.raise_for_status()
    except httpx.HTTPStatusError:
        return False
    return True
