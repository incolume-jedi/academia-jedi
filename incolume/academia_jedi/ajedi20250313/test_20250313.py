"""Estudo compactação com shutil."""

import inspect
from pathlib import Path
import shutil
import tempfile
from inspect import stack
from typing import ClassVar
from icecream import ic
import pytest


class TestCompactShutil:
    """Test case."""

    PATH: ClassVar[Path] = Path(tempfile.gettempdir()) / stack()[0][3]
    quantity: int = 15

    @classmethod
    def setup_class(cls):
        """Setup class."""
        ic(f'starting class {cls.__name__} execution')

    @classmethod
    def teardown_class(cls):
        """Teardown class.

        Teardown da classe. Remove todos os arquivos
         e diretórios gerados ao final.
        """
        ic(f'finished class {cls.__name__} execution')
        shutil.rmtree(cls.PATH)

    def setup_method(self, method):
        """Setup method.

        Cria a estrutura em arvore de diretórios necessários para os testes.
        """
        ic(f'starting execution ({method.__name__}) of {stack()[0][3]}')
        (path := self.PATH.joinpath(method.__name__)).mkdir(
            parents=True,
            exist_ok=True,
        )
        [path.joinpath(f'a{x:02}.txt').touch() for x in range(self.quantity)]

    def teardown_method(self, method):
        """Teardown method.

        Remove a arvore de diretórios criadas após os testes realizados.
        """
        ic(f'finished execution ({method.__name__}) of {stack()[0][3]}')
        path = self.PATH.joinpath(method.__name__)
        shutil.rmtree(path)

    def test_compact_zip(self):
        """Unit test."""
        ext = 'zip'
        output_dir = self.PATH / self.PATH.stem
        path = self.PATH.joinpath(inspect.stack()[0][3])
        result = shutil.make_archive(output_dir, ext, path)
        assert output_dir.with_suffix(f'.{ext}') == Path(result)
        assert Path(result).is_file()

    def test_compact_tar(self):
        """Unit test."""
        ext = 'tar'
        output_dir = self.PATH / self.PATH.stem
        path = self.PATH.joinpath(inspect.stack()[0][3])
        result = shutil.make_archive(output_dir, ext, path)
        assert output_dir.with_suffix(f'.{ext}') == Path(result)
        assert Path(result).is_file()

    @pytest.mark.parametrize(
        ['filename', 'type_format', 'quantia', 'expected'],
        [
            pytest.param(
                PATH / f'{PATH.stem}.zip',
                'zip',
                15,
                [
                    'a00.txt',
                    'a01.txt',
                    'a02.txt',
                    'a03.txt',
                    'a04.txt',
                    'a05.txt',
                    'a06.txt',
                    'a07.txt',
                    'a08.txt',
                    'a09.txt',
                    'a10.txt',
                    'a11.txt',
                    'a12.txt',
                    'a13.txt',
                    'a14.txt',
                ],
                marks=[],
            ),
            pytest.param(
                PATH / f'{PATH.stem}.tar',
                'tar',
                15,
                [
                    'a00.txt',
                    'a01.txt',
                    'a02.txt',
                    'a03.txt',
                    'a04.txt',
                    'a05.txt',
                    'a06.txt',
                    'a07.txt',
                    'a08.txt',
                    'a09.txt',
                    'a10.txt',
                    'a11.txt',
                    'a12.txt',
                    'a13.txt',
                    'a14.txt',
                ],
                marks=[],
            ),
        ],
    )
    def test_extrair(self, filename, type_format, quantia, expected):
        """Unit test."""
        extract_dir = self.PATH / inspect.stack()[0][3]

        assert filename.is_file()

        shutil.unpack_archive(
            filename=filename,
            extract_dir=extract_dir,
            format=type_format,
        )
        result = list(extract_dir.rglob('**/a*.txt'))
        assert all(file.is_file() for file in result)
        assert len(result) == quantia
        assert sorted([file.name for file in result]) == expected
