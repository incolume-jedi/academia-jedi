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
        'param1 param2 expected'.split(),
        [
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen_content',
                        'content0',
                    ),
                    'path_files_in': path_files,
                },
                {
                    'type_format': 'zip',
                    'file_output': base_dir.joinpath(
                        'test_gen_content',
                        'content0',
                    ),
                },
                [
                    'blbgzv.csv',
                    'bpod.csv',
                    'hxxz.csv',
                    'ismczn.csv',
                    'ldmymido.csv',
                    'nkjcc.csv',
                    'oiguvoc.csv',
                    'vfajycsc.csv',
                    'kxcbqhmt.html',
                    'ubbvz.html',
                    'view_lista.html',
                    'view_lista_atualizada.html',
                    'zvbl.html',
                    'assinantes.json',
                    'assinantes_copia.json',
                    'dvljfa.json',
                    'gymo.json',
                    'mggeox.json',
                    'mhpys.json',
                    'qtvjhleg.json',
                    'slzydn.json',
                    'ufaaokuy.json',
                    'azdx.pdf',
                    'dqarpnv.pdf',
                    'eephtr.pdf',
                    'krssr.pdf',
                    'Lendo e Escrevendo Arquivos'
                    ' - Apostila Asimov Academy.pdf',
                    'lhcdkwji.pdf',
                    'ouzcw.pdf',
                    'rjzfcvly.pdf',
                    'rmmfpgfp.pdf',
                    'vheeu.pdf',
                    'viawbe.pdf',
                    'inst_joao.pickle',
                    'meu_dict.pickle',
                    'minha_lista.pickle',
                    'cayv.txt',
                    'eluch.txt',
                    'fmfet.txt',
                    'mbrr.txt',
                    'mnxq.txt',
                    'ozvdvbjv.txt',
                    'quygdhc.txt',
                    'texto.txt',
                    'vktcz.txt',
                    'zilnvj.txt',
                    'bqeb.xlsx',
                    'clientes.xlsx',
                    'cxvq.xlsx',
                    'hmohnmc.xlsx',
                    'hrbabmu.xlsx',
                    'jytyvst.xlsx',
                    'mejysm.xlsx',
                    'mhmcelq.xlsx',
                    'PR.xlsx',
                    'RS.xlsx',
                    'SC.xlsx',
                    'SP.xlsx',
                    'livros.xml',
                    'livros_copia.xml',
                    'backup.zip',
                ],
                marks=[],
            ),
            pytest.param(
                {
                    'output_base': base_dir.joinpath(
                        'test_gen_content',
                        'content1',
                    ),
                    'path_files_in': path_files,
                },
                {
                    'type_format': 'tar',
                    'file_output': base_dir.joinpath(
                        'test_gen_content',
                        'backup',
                    ),
                },
                [
                    'blbgzv.csv',
                    'bpod.csv',
                    'hxxz.csv',
                    'ismczn.csv',
                    'ldmymido.csv',
                    'nkjcc.csv',
                    'oiguvoc.csv',
                    'vfajycsc.csv',
                    'kxcbqhmt.html',
                    'ubbvz.html',
                    'view_lista.html',
                    'view_lista_atualizada.html',
                    'zvbl.html',
                    'assinantes.json',
                    'assinantes_copia.json',
                    'dvljfa.json',
                    'gymo.json',
                    'mggeox.json',
                    'mhpys.json',
                    'qtvjhleg.json',
                    'slzydn.json',
                    'ufaaokuy.json',
                    'azdx.pdf',
                    'dqarpnv.pdf',
                    'eephtr.pdf',
                    'krssr.pdf',
                    'Lendo e Escrevendo Arquivos'
                    ' - Apostila Asimov Academy.pdf',
                    'lhcdkwji.pdf',
                    'ouzcw.pdf',
                    'rjzfcvly.pdf',
                    'rmmfpgfp.pdf',
                    'vheeu.pdf',
                    'viawbe.pdf',
                    'inst_joao.pickle',
                    'meu_dict.pickle',
                    'minha_lista.pickle',
                    'cayv.txt',
                    'eluch.txt',
                    'fmfet.txt',
                    'mbrr.txt',
                    'mnxq.txt',
                    'ozvdvbjv.txt',
                    'quygdhc.txt',
                    'texto.txt',
                    'vktcz.txt',
                    'zilnvj.txt',
                    'bqeb.xlsx',
                    'clientes.xlsx',
                    'cxvq.xlsx',
                    'hmohnmc.xlsx',
                    'hrbabmu.xlsx',
                    'jytyvst.xlsx',
                    'mejysm.xlsx',
                    'mhmcelq.xlsx',
                    'PR.xlsx',
                    'RS.xlsx',
                    'SC.xlsx',
                    'SP.xlsx',
                    'livros.xml',
                    'livros_copia.xml',
                    'backup.zip',
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
