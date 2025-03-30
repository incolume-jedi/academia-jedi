"""Test module."""

import logging
from pathlib import Path
from typing import NoReturn

import pytest
from incolume.academia_jedi.ajedi20230113_zipfile import (
    filezip_sample,
    filezip_sample_pwd,
    filezip_sample_pwd1,
)
from incolume.academia_jedi.ajedi20230113_zipfile import (
    realpython01,
    realpython02,
    realpython03,
    realpython04,
    realpython05,
)
from tempfile import NamedTemporaryFile, gettempdir


# ruff: noqa: PLR0913
class TestCase:
    """Test case."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(filezip_sample, True),
            pytest.param(filezip_sample_pwd, True),
            pytest.param(filezip_sample_pwd1, True),
        ],
    )
    def test_var(self, entrance, expected):
        """Unittest."""
        assert entrance.is_file() is expected

    def test_estudo1(self, capsys) -> NoReturn:
        """Unititest."""
        realpython01.run()
        capture = capsys.readouterr()
        assert capture.out == (
            'File Name                                             '
            'Modified             Size\n'
            'files/                                         '
            '2023-01-13 08:29:34            0\n'
            'wFEoSLpJSzlkbuU.md                             '
            '2022-12-01 14:36:20          748\n'
            'wMKCNgyLMsBczZs.md                             '
            '2022-12-01 17:21:10         1348\n'
            'wtGzooBjpbSTjsl.md                             '
            '2022-12-01 17:44:40         2603\n'
            'wxwFDrIplXVgLEY.md                             '
            '2022-12-01 16:39:06         1348\n'
            'wzxnlQNFSlVoPJe.md                             '
            '2022-12-01 16:14:56          398\n'
            'files/zbIUSLhPoMNSLke.md                       '
            '2022-12-01 17:20:58         1348\n'
            'files/zbnuNIzsQfvUhCH.md                       '
            '2022-12-01 17:19:12         2603\n'
            'files/znKYZLvdIUbOqpe.md                       '
            '2022-12-01 16:39:06          398\n'
            'files/zZiyJewrMcQhJxV.md                       '
            '2022-12-01 16:14:56         2603\n'
            'files/zihOKPyvnijoMjr.md                       '
            '2022-12-01 17:58:36         1348\n'
            'files/zSECYooiBAaueGk.md                       '
            '2022-12-01 17:21:04          398\n'
            'files/zAbWbqFvgqJfmpl.md                       '
            '2022-12-01 17:58:54          398\n'
            'hello.txt                                      '
            '2023-01-13 09:52:10            5\n'
            'new_hello.txt                                  '
            '1980-01-01 00:00:00           13\n'
            'new_hello.txt                                  '
            '1980-01-01 00:00:00           13\n'
            'new_hello.txt                                  '
            '1980-01-01 00:00:00           13\n'
        )

    @pytest.mark.parametrize(
        'exct entrance expected'.split(),
        [
            pytest.param(
                None,
                filezip_sample_pwd,
                (
                    '===\n'
                    'File Name                                             '
                    'Modified             Size\n'
                    'hello.txt                                      '
                    '2023-01-13 09:52:10            5\n'
                ),
            ),
            pytest.param(
                {
                    'expected_exception': FileNotFoundError,
                    'match': 'No such file or directory',
                },
                '',
                'ERROR   ; root; realpython02; tratativa1;'
                ' No such file or directory',
            ),
            pytest.param(
                {
                    'expected_exception': realpython02.zipfile.BadZipfile,
                    'match': 'File is not a zip file',
                },
                Path(__file__),
                'ERROR   ; root; realpython02; tratativa1;'
                ' Falha no arquivo zip',
            ),
        ],
    )
    def test_estudo2(
        self,
        capsys,
        caplog,
        entrance,
        expected,
        exct,
    ) -> NoReturn:
        """Unititest."""
        caplog.set_level(logging.DEBUG)
        if exct:
            with pytest.raises(**exct):
                realpython02.tratativa1(entrance)
            assert expected in caplog.text
        else:
            realpython02.tratativa1(entrance)
            capture = capsys.readouterr()
            assert capture.out == expected
            assert capture.err == ''

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (realpython03.zipnames[-1], '===\nFile is not a zip file\n'),
            (
                filezip_sample_pwd1,
                '===\n'
                'File Name                                             '
                'Modified             Size\n'
                'new_hello.txt                                  '
                '2023-01-13 09:52:10           12\n',
            ),
        ],
    )
    def test_estudo3(self, entrance, expected, capsys) -> NoReturn:
        """Unittest."""
        realpython03.tratativa2(entrance)
        capture = capsys.readouterr()
        assert capture.out == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (realpython04.hello, realpython04.hello.with_suffix('.zip')),
            (
                (fin := NamedTemporaryFile().name),
                Path(fin).with_suffix('.zip'),
            ),
        ],
    )
    def test_estudo4(self, entrance, expected) -> NoReturn:
        """Unittest."""
        filename = Path(entrance) if isinstance(entrance, str) else entrance
        filename.write_text(filename.as_posix())

        assert realpython04.tratativa(filename=filename) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (realpython05.hello, realpython05.hello.with_suffix('.zip')),
            (
                (fin := NamedTemporaryFile().name),
                Path(fin).with_suffix('.zip'),
            ),
        ],
    )
    def test_estudo5(self, entrance, expected) -> NoReturn:
        """Unittest."""
        filename = Path(entrance) if isinstance(entrance, str) else entrance
        filename.write_text(filename.as_posix())

        with pytest.raises(
            FileNotFoundError,
            match='',
        ):
            assert (
                realpython05.tratativa(
                    filename=filename,
                    filenamezip=Path(gettempdir(), 'xpto', 'output.zip'),
                )
                == expected
            )
