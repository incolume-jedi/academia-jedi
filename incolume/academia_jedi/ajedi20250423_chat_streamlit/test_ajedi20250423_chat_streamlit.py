"""Chat streamlit."""

import pytest
import incolume.academia_jedi.ajedi20250423_chat_streamlit as pkg
import datetime as dt
from config import settings
from pytz import timezone


class TestCase:
    """TestCase."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                ('user one', 'user two', {'as': 'as'}),
                {
                    'mensagens',
                    f'user_one-user_two-{dt.datetime.now(tz=timezone(settings.tz)):%Y%m%d}.pkl',
                },
            ),
        ],
    )
    def test_0(self, entrance, expected):
        """Unittest."""
        assert expected.issubset(pkg.write_msg(*entrance).parts)
