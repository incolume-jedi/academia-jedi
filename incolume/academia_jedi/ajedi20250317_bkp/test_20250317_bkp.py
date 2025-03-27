"""Test module."""

from pathlib import Path
import shutil

import pytest
from . import gen_bkp, organizer_dir, path_files
from tempfile import gettempdir
from inspect import stack
from faker import Faker
from icecream import ic
from config import settings


ic.disable()
if settings.debug_mode:
    ic.enable()

Faker.seed(13)
fake = Faker('pt_Br')


def massa_teste(dout: Path) -> Path:
    """Gera arquivos."""
    dout.mkdir(parents=True, exist_ok=True)
    extensions = [
        'htm',
        'html',
        'docx',
        'xlsx',
        'pdf',
        'xml',
        'json',
        'pickle',
        'txt',
        'csv',
    ]
    file_names = []
    if not ic(len(list(dout.iterdir()))):
        file_names.extend(fake.file_name(category='audio') for _ in range(20))
        file_names.extend(
            fake.file_name(extension=ext)
            for _ in range(5)
            for ext in extensions
        )
        [dout.joinpath(file).touch() for file in file_names]
    ic(list(dout.iterdir()))
    return dout


class TestOrganizer:
    """Test case."""

    base_dir: Path = Path(gettempdir(), stack()[0][3])
    path_test: Path = base_dir.joinpath('files', 'desafio')

    @classmethod
    def setup(cls):
        """Setup class."""
        cls.base_dir.mkdir(exist_ok=True)
        massa_teste(cls.path_test)

    @classmethod
    def teardown_class(cls):
        """Setup class."""
        shutil.rmtree(cls.base_dir)

    def teardown_method(self, method):
        """Setup method."""
        directory = self.base_dir.joinpath(method.__name__)
        if directory.exists():
            shutil.rmtree(directory)

    def test_setup_class_created(self):
        """Unittest."""
        assert self.base_dir.is_dir()

    def test_organizer_0(self):
        """Unittest."""
        output = self.base_dir / stack()[0][3]
        assert not output.is_dir()
        assert output == organizer_dir(self.path_test, output)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {
                    'output_base': base_dir.joinpath(
                        'test_organizer',
                    ),
                    'path_files_out': None,
                    'path_files_in': path_test,
                },
                'TestOrganizer test_organizer'.split(),
            ),
        ],
    )
    def test_organizer_1(self, entrance, expected):
        """Unittest."""
        assert set(expected).issubset(organizer_dir(**entrance).parts)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_organizer',
                    ),
                    'path_files_out': None,
                    'path_files_in': path_test,
                },
                ['csv', 'html', 'json', 'pdf', 'pickle', 'txt', 'xlsx', 'xml'],
            ),
        ],
    )
    def test_organizer_2(self, entrance, expected):
        """Unittest."""
        assert set(expected).issubset(
            x.name for x in organizer_dir(**entrance).iterdir() if x.is_dir()
        )

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('exists', True),
            pytest.param('is_dir', False),
            pytest.param('is_file', True),
        ],
    )
    def test_path_files(self, entrance, expected):
        """Unittest."""
        result = gen_bkp(path_files)
        assert getattr(result, entrance)() is expected

    @pytest.mark.parametrize(
        'entrance type_format expected'.split(),
        [
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen',
                    ),
                    'path_files_out': None,
                    'path_files_in': path_test,
                },
                'zip',
                base_dir / 'test_gen/backup/backup.zip',
            ),
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen',
                    ),
                    'path_files_out': base_dir,
                    'path_files_in': path_test,
                },
                'zip',
                base_dir / 'backup.zip',
            ),
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_organizer',
                    ),
                    'path_files_out': None,
                    'path_files_in': path_test,
                },
                'tar',
                base_dir / 'test_organizer/backup/backup.tar',
            ),
        ],
    )
    def test_gen_pkg(self, entrance, type_format, expected):
        """Unittest."""
        path_test = organizer_dir(**entrance)
        result = gen_bkp(path_test, type_format=type_format)
        assert result == expected

    @pytest.mark.parametrize(
        'param1 param2 expected'.split(),
        [
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen_content',
                        'content0',
                    ),
                    'path_files_in': path_test,
                },
                {
                    'type_format': 'zip',
                    'file_output': base_dir.joinpath(
                        'test_gen_content',
                        'content0',
                    ),
                },
                [
                    'similique.docx',
                    'aut.docx',
                    'repellat.docx',
                    'ipsam.docx',
                    'quasi.docx',
                    'minima.xml',
                    'suscipit.xml',
                    'laborum.xml',
                    'veritatis.xml',
                    'ex.xml',
                    'facere.flac',
                    'aut.flac',
                    'fuga.flac',
                    'et.flac',
                    'non.flac',
                    'vel.flac',
                    'vitae.flac',
                    'totam.flac',
                    'error.wav',
                    'maiores.wav',
                    'nobis.wav',
                    'impedit.wav',
                    'ea.wav',
                    'vitae.wav',
                    'accusantium.wav',
                    'quidem.pickle',
                    'tempora.pickle',
                    'fuga.pickle',
                    'molestias.pickle',
                    'ex.pickle',
                    'deleniti.xlsx',
                    'magnam.xlsx',
                    'non.xlsx',
                    'porro.xlsx',
                    'ullam.xlsx',
                    'nam.htm',
                    'non.htm',
                    'eligendi.htm',
                    'occaecati.htm',
                    'maiores.htm',
                    'quod.html',
                    'delectus.html',
                    'tempore.html',
                    'dolorum.html',
                    'dolorum.txt',
                    'sequi.txt',
                    'fuga.txt',
                    'a.txt',
                    'earum.txt',
                    'voluptas.csv',
                    'impedit.csv',
                    'hic.csv',
                    'voluptates.csv',
                    'nisi.csv',
                    'illum.mp3',
                    'nostrum.mp3',
                    'eveniet.mp3',
                    'quo.mp3',
                    'dignissimos.mp3',
                    'saepe.json',
                    'officia.json',
                    'officiis.json',
                    'numquam.json',
                    'recusandae.json',
                    'nulla.pdf',
                    'cumque.pdf',
                    'totam.pdf',
                    'explicabo.pdf',
                    'quo.pdf',
                ],
                marks=[],
            ),
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen_content',
                        'content1',
                    ),
                    'path_files_in': path_test,
                },
                {
                    'type_format': 'tar',
                    'file_output': base_dir.joinpath(
                        'test_gen_content',
                        'backup',
                    ),
                },
                [
                    'similique.docx',
                    'aut.docx',
                    'repellat.docx',
                    'ipsam.docx',
                    'quasi.docx',
                    'minima.xml',
                    'suscipit.xml',
                    'laborum.xml',
                    'veritatis.xml',
                    'ex.xml',
                    'facere.flac',
                    'aut.flac',
                    'fuga.flac',
                    'et.flac',
                    'non.flac',
                    'vel.flac',
                    'vitae.flac',
                    'totam.flac',
                    'error.wav',
                    'maiores.wav',
                    'nobis.wav',
                    'impedit.wav',
                    'ea.wav',
                    'vitae.wav',
                    'accusantium.wav',
                    'quidem.pickle',
                    'tempora.pickle',
                    'fuga.pickle',
                    'molestias.pickle',
                    'ex.pickle',
                    'deleniti.xlsx',
                    'magnam.xlsx',
                    'non.xlsx',
                    'porro.xlsx',
                    'ullam.xlsx',
                    'nam.htm',
                    'non.htm',
                    'eligendi.htm',
                    'occaecati.htm',
                    'maiores.htm',
                    'quod.html',
                    'delectus.html',
                    'tempore.html',
                    'dolorum.html',
                    'dolorum.txt',
                    'sequi.txt',
                    'fuga.txt',
                    'a.txt',
                    'earum.txt',
                    'voluptas.csv',
                    'impedit.csv',
                    'hic.csv',
                    'voluptates.csv',
                    'nisi.csv',
                    'illum.mp3',
                    'nostrum.mp3',
                    'eveniet.mp3',
                    'quo.mp3',
                    'dignissimos.mp3',
                    'saepe.json',
                    'officia.json',
                    'officiis.json',
                    'numquam.json',
                    'recusandae.json',
                    'nulla.pdf',
                    'cumque.pdf',
                    'totam.pdf',
                    'explicabo.pdf',
                    'quo.pdf',
                ],
            ),
        ],
    )
    def test_gen_content(self, param1, param2, expected):
        """Unittest."""
        path_test = organizer_dir(**param1)
        assert path_test.name == 'backup'
        filecompress = gen_bkp(path_test, **param2)
        assert filecompress == param2['file_output'].with_suffix(
            f'.{param2["type_format"]}',
        )
        dirout = self.base_dir.joinpath(stack()[0][3], 'restore')
        shutil.unpack_archive(
            filename=filecompress,
            extract_dir=dirout,
            format=param2['type_format'],
        )
        result = list(dirout.rglob('**/*.*'))
        assert [x.name for x in result] == expected
