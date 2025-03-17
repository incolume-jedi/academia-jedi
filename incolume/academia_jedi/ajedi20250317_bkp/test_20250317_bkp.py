"""Test module."""

from pathlib import Path
import shutil

import pytest
from . import gen_bkp, path_files, organizer_dir
from tempfile import gettempdir
from inspect import stack


class TestOrganizer:
    """Test case."""

    base_dir: Path = Path(gettempdir()) / stack()[0][3]

    @classmethod
    def setup(cls):
        """Setup class."""
        cls.base_dir.mkdir(exist_ok=True)

    @classmethod
    def teardown_class(cls):
        """Setup class."""
        # shutil.rmtree(cls.base_dir)

    def test_setup_class_created(self):
        """Unittest."""
        assert self.base_dir.is_dir()

    def test_organizer_0(self):
        """Unittest."""
        output = self.base_dir / stack()[0][3]
        assert not output.is_dir()
        assert output == organizer_dir(path_files, output)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {
                    'output_base': base_dir.joinpath(
                        'test_organizer',
                    ),
                    'path_files_out': None,
                    'path_files_in': path_files,
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
            (
                {
                    'output_base': base_dir.joinpath(
                        'test_organizer',
                    ),
                    'path_files_out': None,
                    'path_files_in': path_files,
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
                    'path_files_in': path_files,
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
                    'path_files_in': path_files,
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
                    'path_files_in': path_files,
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
        'entrance type_format expected'.split(),
        [
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen',
                    ),
                    'path_files_out': None,
                    'path_files_in': path_files,
                },
                'zip',
                [],
            ),
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen',
                    ),
                    'path_files_out': base_dir,
                    'path_files_in': path_files,
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
                    'path_files_in': path_files,
                },
                'tar',
                base_dir / 'test_organizer/backup/backup.tar',
            ),
        ],
    )
    def test_gen_content(self, entrance, type_format, expected):
        """Unittest."""
        path_test = organizer_dir(**entrance)
        result = gen_bkp(path_test, type_format=type_format)
        dirout = self.base_dir / stack()[0][3]
        shutil.unpack_archive(result, dirout)
        assert list(dirout.iterdir()) == expected
