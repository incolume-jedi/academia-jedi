import incolume.academia_jedi.ajedi20230928_manipulacao_arquivos.files as pkg
import pytest
from pathlib import Path
from tempfile import NamedTemporaryFile
from functools import partialmethod


class TestCase:
    """Caso de teste."""

    content_fake = (
        'id,nome,telefone\n'
        '1,ciclano,614235-6789\n'
        '2,fulano,617546-4512\n'
        '3,beltrano,621427-7546\n'
        '4,josé da silva,614215-7645\n'
        '5,joão da silva,617777-7777\n'
        '6,sabino cruz das colves,(61) 95555-5555\n'
    )

    @pytest.fixture()
    def nfile(self, ext: str = '') -> Path:
        """Arquivo temp."""
        ext = f'.{ext.strip(".")}' if ext else '.txt'
        return Path(NamedTemporaryFile(prefix='AJEDI-', suffix=ext).name)

    def test_content_origin(self):
        """Teste para conteúdo de origem."""
        assert isinstance(pkg.CONTENT, list)

    @pytest.mark.parametrize(
        'function',
        [getattr(pkg, func) for func in dir(pkg) if func.startswith('exemplo')]
    )
    def test_files_examples_exists(self, nfile, function):
        """Testar se arquivo gerado existe."""
        function(nfile)
        assert nfile.is_file()

    def test_files_exemplo1_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo01(nfile)
        assert nfile.read_text() == 'alguma coisa'

    def test_files_exemplo2_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo02(nfile)
        assert nfile.read_text() == 'alguma coisa\noutra coisa'

    def test_files_exemplo3_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo03(nfile)
        assert nfile.read_text() == 'alguma coisa.'

    def test_files_exemplo4_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo04(nfile)
        assert nfile.read_text() == 'alguma coisa'

    def test_files_exemplo5_txt(self, nfile):
        """Teste para arquivos TXT."""
        pkg.exemplo05(nfile)
        assert nfile.read_text() == 'alguma coisaoutra coisa'

    def test_files_exemplo6_csv(self, nfile) -> None:
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        pkg.exemplo06(nfile)
        assert (
            'first_name,last_name\nBaked,Beans'
            '\nLovely,Spam\nWonderful,Spam\n'
        ) in nfile.read_text()

    def test_files_exemplo7_csv(self, nfile) -> None:
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        pkg.exemplo07(nfile, pkg.CONTENT)
        result = nfile.read_text()
        assert 'id,nome,telefone' in result

    def test_files_exemplo6_csv(self, nfile):
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        nfile.write_text(self.content_fake)
        pkg.exemplo08(nfile)
        out, _ = capsys.readouterr()
        assert out == (
            "['id,nome,telefone']\n"
            "['1,ciclano,614235-6789']\n"
            "['2,fulano,617546-4512']\n"
            "['3,beltrano,621427-7546']\n"
            "['4,josé da silva,614215-7645']\n"
            "['5,joão da silva,617777-7777']\n"
            "['6,sabino cruz das colves,(61) 95555-5555']\n"
        )

    def test_files_exemplo7_csv(self):
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        nfile.write_text(self.content_fake)
        pkg.exemplo09(nfile)
        out, _ = capsys.readouterr()
        assert out == (
            "['id,nome,telefone']\n"
            "['1,ciclano,614235-6789']\n"
            "['2,fulano,617546-4512']\n"
            "['3,beltrano,621427-7546']\n"
            "['4,josé da silva,614215-7645']\n"
            "['5,joão da silva,617777-7777']\n"
            "['6,sabino cruz das colves,(61) 95555-5555']\n"
        )

    def test_files_exemplo8_csv(self):
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        nfile.write_text(self.content_fake.replace(',', ';'))
        pkg.exemplo10(nfile)
        out, _ = capsys.readouterr()
        assert out == (
            "['id', 'nome', 'telefone']\n"
            "[('id', '1'), ('nome', 'ciclano'), "
            "('telefone', '614235-6789')]\n"
            "[('id', '2'), ('nome', 'fulano'), ('telefone', '617546-4512')]\n"
            "[('id', '3'), ('nome', 'beltrano'), "
            "('telefone', '621427-7546')]\n"
            "[('id', '4'), ('nome', 'josé da silva'), "
            "('telefone', '614215-7645')]\n"
            "[('id', '5'), ('nome', 'joão da silva'), "
            "('telefone', '617777-7777')]\n"
            "[('id', '6'), ('nome', 'sabino cruz das colves'), "
            "('telefone', '(61) 95555-5555')]\n"
        )

    def test_files_exemplo9_csv(self):
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        nfile.write_text(self.content_fake.replace(',', ';'))
        pkg.exemplo11(nfile)
        out, _ = capsys.readouterr()
        assert out == (
            "[{'id': '1', 'nome': 'ciclano', 'telefone': '614235-6789'},\n "
            "{'id': '2', 'nome': 'fulano', 'telefone': '617546-4512'},\n "
            "{'id': '3', 'nome': 'beltrano', 'telefone': '621427-7546'},\n "
            "{'id': '4', 'nome': 'josé da silva', "
            "'telefone': '614215-7645'},\n "
            "{'id': '5', 'nome': 'joão da silva', "
            "'telefone': '617777-7777'},\n "
            "{'id': '6', 'nome': 'sabino cruz das colves', "
            "'telefone': '(61) 95555-5555'}]\n"
        )

    def test_files_exemplo10_csv(self):
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        nfile.write_text(self.content_fake.replace(',', ';'))
        pkg.exemplo12(nfile)
        out, _ = capsys.readouterr()
        assert out == (
            "{'id': '1', 'nome': 'ciclano', 'telefone': '614235-6789'}\n"
            "{'id': '2', 'nome': 'fulano', 'telefone': '617546-4512'}\n"
            "{'id': '3', 'nome': 'beltrano', 'telefone': '621427-7546'}\n"
            "{'id': '4', 'nome': 'josé da silva', 'telefone': '614215-7645'}\n"
            "{'id': '5', 'nome': 'joão da silva', 'telefone': '617777-7777'}\n"
            "{'id': '6', 'nome': 'sabino cruz das colves', "
            "'telefone': '(61) 95555-5555'}\n"
        )

    def test_files_exemplo13_csv(self, nfile) -> None:
        """Teste para arquivos CSV."""
        nfile = nfile.with_suffix('.csv')
        nfile.write_text(self.content_fake.replace(',', ';'))
        result = pkg.exemplo13(nfile)
        assert result == [
            {'id': '1', 'nome': 'ciclano', 'telefone': '614235-6789'},
            {'id': '2', 'nome': 'fulano', 'telefone': '617546-4512'},
            {'id': '3', 'nome': 'beltrano', 'telefone': '621427-7546'},
            {'id': '4', 'nome': 'josé da silva', 'telefone': '614215-7645'},
            {'id': '5', 'nome': 'joão da silva', 'telefone': '617777-7777'},
            {
                'id': '6',
                'nome': 'sabino cruz das colves',
                'telefone': '(61) 95555-5555',
            },
        ]

    def test_files_exemplo14_json(self, nfile) -> None:
        """Teste para arquivos JSON."""
        nfile = nfile.with_suffix('.json')
        pkg.exemplo14(nfile, pkg.CONTENT)
        assert nfile.read_text() == (
            '[\n'
            '    {\n'
            '        "id": 1,\n'
            '        "nome": "ciclano",\n'
            '        "telefone": "614235-6789"\n'
            '    },\n'
            '    {\n'
            '        "id": 2,\n'
            '        "nome": "fulano",\n'
            '        "telefone": "617546-4512"\n'
            '    },\n'
            '    {\n'
            '        "id": 3,\n'
            '        "nome": "beltrano",\n'
            '        "telefone": "621427-7546"\n'
            '    },\n    {\n        "id": 4,\n'
            '        "nome": "jos\\u00e9 da silva",\n'
            '        "telefone": "614215-7645"\n    },\n'
            '    {\n        "id": 5,\n'
            '        "nome": "jo\\u00e3o da silva",\n'
            '        "telefone": "617777-7777"\n    },\n'
            '    {\n        "id": 6,\n'
            '        "nome": "sabino cruz das colves",\n'
            '        "telefone": "(61) 95555-5555"\n    }\n]'
        )

    def test_files_exemplo12_json(self):
        """Teste para arquivos JSON."""
        nfile = nfile.with_suffix('.json')
        nfile.write_text(
            '[{\n        "id": 6,\n'
            '        "nome": "sabino cruz das colves",\n'
            '        "telefone": "(61) 95555-5555"\n    }\n]',
        )
        pkg.exemplo15(nfile)
        out, _ = capsys.readouterr()
        assert out == (
            "{'id': 6, 'nome': 'sabino cruz das colves',"
            " 'telefone': '(61) 95555-5555'}\n"
        )

    def test_files_exemplo16_json(self, nfile) -> None:
        """Teste para arquivos JSON."""
        nfile = nfile.with_suffix('.json')
        nfile.write_text(
            '[{\n        "id": 6,\n'
            '        "nome": "sabino cruz das colves",\n'
            '        "telefone": "(61) 95555-5555"\n    }\n]',
        )
        assert pkg.exemplo16(nfile) == [
            {
                'id': 6,
                'nome': 'sabino cruz das colves',
                'telefone': '(61) 95555-5555',
            },
        ]

