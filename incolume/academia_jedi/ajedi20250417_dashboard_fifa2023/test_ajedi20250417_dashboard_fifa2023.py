"""Test Dashboard FIFA2023."""

from typing import NoReturn

import pytest
from incolume.academia_jedi.ajedi20250417_dashboard_fifa2023 import (
    URLS,
    get_dataset,
    io,
    zipfile,
    httpx,
)


class TestDashboard:
    """Case tests."""

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param('ds_fifa2023', marks=[]),
            pytest.param('ds_fifa2023_7z', marks=[]),
            pytest.param('emoji', marks=[]),
            pytest.param('kaggle', marks=[]),
            pytest.param('zip_ds_fifa', marks=[]),
        ],
    )
    def test_urls(self, entrance) -> NoReturn:
        """Unittest."""
        assert entrance in URLS.__annotations__

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA23_official_data.csv',
            ),
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA22_official_data.csv',
            ),
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA21_official_data.csv',
            ),
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA20_official_data.csv',
            ),
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA19_official_data.csv',
            ),
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA18_official_data.csv',
            ),
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA17_official_data.csv',
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        file_zip = io.BytesIO(
            httpx.get(entrance).content,
        )  # carrega bytes com arquivo
        with zipfile.ZipFile(file_zip) as handle:
            assert expected in handle.namelist()

    @pytest.mark.parametrize(
        'entrance target_file expected'.split(),
        [
            pytest.param(
                URLS.zip_ds_fifa,
                'CLEAN_FIFA23_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,'
                    b'Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                    b'Preferred Foot,International Reputation,Weak Foot,Skill'
                    b' Moves,Work Rate,Body Type,Real Face,Position,Joined,'
                    b'Loaned From,Contract Valid Until,Height(cm.),'
                    b'Weight(lbs.),Release Clause(\xc2\xa3),Kit Number,'
                    b'Best Overall Rating,'
                    b'Year_Joined\r\n'
                ),
            ),
        ],
    )
    def test_4(self, entrance, target_file, expected) -> NoReturn:
        """Unittest."""
        assert (
            get_dataset(
                url_zipfile=entrance,
                target_file=target_file,
            ).readline()
            == expected
        )
