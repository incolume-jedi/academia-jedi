"""Dashboard FIFA2023.

- https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data
- dataset FIFA2023: https://pastebin.com/raw/cYJfDddu
- emoji markdown: https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia
"""

import io
import zipfile
from dataclasses import dataclass, field
from typing import Final
from functools import lru_cache
import httpx


@dataclass
class URLS:
    """URL for project."""

    zip_ds_fifa: Final[str] = 'https://pastebin.com/raw/Zt9BHEF4'

    kaggle: str = field(
        default='https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data',
        init=False,
        kw_only=True,
    )
    emoji: str = field(
        default='https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia',
        init=False,
        kw_only=True,
    )
    ds_fifa2023: str = field(
        default='',
        init=False,
        kw_only=True,
    )
    ds_fifa2023_7z: str = field(
        default='https://pastebin.com/raw/KGmnsB0j',
        init=False,
        kw_only=True,
    )

@lru_cache
def get_dataset(url_zipfile: str = '', target_file: str = '') -> io.BytesIO:
    """Get dataset."""
    url_zipfile = url_zipfile or URLS.zip_ds_fifa
    target_file = target_file or 'CLEAN_FIFA23_official_data.csv'

    file_zip = io.BytesIO(
        httpx.get(url_zipfile).content,
    )  # carrega bytes com arquivo
    with (
        zipfile.ZipFile(file_zip) as handle,
        handle.open(target_file) as file,
    ):
        return io.BytesIO(file.read())
