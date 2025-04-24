"""Chat streamlit."""

from pathlib import Path
from typing import ClassVar
import pytest
import incolume.academia_jedi.ajedi20250423_chat_streamlit as pkg
import datetime as dt
from config import settings
from pytz import timezone
from icecream import ic


class TestCase:
    """TestCase."""

    trash: ClassVar[list[Path]] = []

    @classmethod
    def teardown_class(cls):
        """Teardown class."""
        [path.unlink(missing_ok=True) for path in cls.trash]
        ic(f'finished class {cls.__name__} execution')

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                ('user one', 'user two'),
                {
                    'mensagens',
                    f'user_one-user_two-{dt.datetime.now(tz=timezone(settings.tz)):%Y%m%d}.pkl',
                },
            ),
        ],
    )
    def test_filename_chat(self, entrance, expected):
        """Unittest."""
        assert expected.issubset(pkg.filename_chat(*entrance).parts)

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
    def test_write_msg(self, entrance, expected):
        """Unittest."""
        result = pkg.write_msg(*entrance)
        self.trash.append(result)
        assert expected.issubset(result.parts)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(('user one', 'user two'), {'as': 'as'}),
            pytest.param(('user two', 'user one'), {'as': 'as'}),
            pytest.param(('user twice', 'user one'), []),
            pytest.param(('user twice', 'user two'), []),
        ],
    )
    def test_read_msg(self, entrance, expected):
        """Unittest."""
        if 'expected_exception' in expected:
            with pytest.raises(**expected):
                pkg.read_msg(*entrance)
        else:
            assert pkg.read_msg(*entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('user one', {'users', 'user_one.pkl'}),
            pytest.param('user two', {'users', 'user_two.pkl'}),
            pytest.param('user three', {'users', 'user_three.pkl'}),
            pytest.param('user four', {'users', 'user_four.pkl'}),
        ],
    )
    def test_filename_user(self, entrance, expected):
        """Unittest."""
        result = pkg.filename_user(entrance)
        self.trash.append(result)
        ic(self.trash)
        assert expected.issubset(result.parts)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(('user one', '123abc'), True),
            pytest.param(('user one', '123abc'), False),
            pytest.param(('user two', '123abc'), True),
            pytest.param(('user three', '123abc'), True),
            pytest.param(('user four', '123abc'), True),
        ],
    )
    def test_create_new_user(self, entrance, expected):
        """Unittest."""
        assert ic(pkg.create_new_user(*entrance)) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(('user one', '123abc'), True),
            pytest.param(('user two', '123abc'), True),
            pytest.param(('user three', '123abc'), True),
            pytest.param(('user four', '123abc'), True),
            pytest.param(('user five', '123abc'), False),
        ],
    )
    def test_check_senha(self, entrance, expected):
        """Unittest."""
        assert pkg.check_senha(*entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('user_one', True),
            pytest.param('user_two', True),
            pytest.param('user_three', True),
            pytest.param('user_four', True),
            pytest.param('user_five', False),
        ],
    )
    def test_all_users(self, entrance, expected):
        """Unittest."""
        result = pkg.users_all()
        assert isinstance(result, list)
        assert (entrance in result) == expected
