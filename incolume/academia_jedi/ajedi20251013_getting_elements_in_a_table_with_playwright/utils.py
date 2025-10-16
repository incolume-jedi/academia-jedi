"""utils for submodule."""

import tempfile
from pathlib import Path
from typing import Any

dout = Path(tempfile.gettempdir()) / Path(__file__).parent.stem


def config(content_index: str = '') -> Path:
    """Config it."""
    dsite: Path = dout / 'site-fake'
    dsite.mkdir(parents=True, exist_ok=True)
    site = dsite / 'index.html'
    dsite.joinpath('favicon.ico').write_bytes(
        Path(__file__)
        .parents[3]
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
