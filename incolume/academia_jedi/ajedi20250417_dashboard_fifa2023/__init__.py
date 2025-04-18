"""Dashboard FIFA2023.

- https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data
- dataset FIFA2023: https://pastebin.com/raw/cYJfDddu
- emoji markdown: https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia
"""

from dataclasses import dataclass, field


@dataclass
class URLS:
    """URL for project."""

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
