"""Test module."""

from typing import NoReturn
import pytest
from . import Options, finalizar

# ruff: noqa: PLR0913


class TestCase:
    """Testcase."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('0', '', marks=[]),
        ],
    )
    def test_options(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert Options(entrance) is expected

    @pytest.mark.parametrize(
        'op msg deny_op expected'.split(),
        [
            pytest.param('', '', [], False),
            pytest.param('2', '', [], False),
            pytest.param('2', 'ops: ', [], False),
        ],
    )
    def test_finalizar(
        self,
        op,
        msg,
        deny_op,
        expected,
        monkeypatch,
        capsys,
    ) -> NoReturn:
        """Unittest."""
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: op)
            result = finalizar(msg, deny_op)
            output = capsys.readouterr()

            assert result is expected
            assert output.out == ''

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('', ''),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert entrance == expected
