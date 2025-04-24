"""Chat streamlit."""

import pytest
import incolume.academia_jedi.ajedi20250423_chat_streamlit as pkg


class TestCase:
    """TestCase."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                ('user one', 'user two', {'as': 'as'}),
                {'mensagens', 'user_one-user_two-20250423.pkl'},
            ),
        ],
    )
    def test_0(self, entrance, expected):
        """Unittest."""
        assert expected.issubset(pkg.write_msg(*entrance).parts)
