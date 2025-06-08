"""Test module."""

from typing import NoReturn
import pytest
import incolume.academia_jedi.ajedi20250304_jogo_da_forca.jogo_da_forca as pkg


class CheckAlura:
    """Testcase."""

    obj = pkg.Alura()

    def test_msg_abertura(self, capsys) -> NoReturn:
        """Unittest."""
        self.obj.imprime_mensagem_abertura()
        out, err = capsys.readouterr()
        assert (
            out == '*********************************\n'
            '***Bem vindo ao jogo da Forca!***\n'
            '*********************************\n'
        )
        assert err == ''

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(0, 'CAJUEIRO'),
            pytest.param(1, 'BICICLETA'),
            pytest.param(2, 'PARALELEPIPEDO'),
        ],
    )
    def test_load_secret_word(self, entrance, expected, monkeypatch):
        """Unittest."""

        def mock_return(*_):
            return entrance

        monkeypatch.setattr('secrets.randbelow', mock_return)
        assert self.obj.carrega_palavra_secreta() == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(0, 'CAJUEIRO'),
            pytest.param(1, 'BICICLETA'),
            pytest.param(2, 'PARALELEPIPEDO'),
        ],
    )
    def test_inicializa_letras_acertadas(
        self,
        entrance,
        expected,
        monkeypatch,
    ):
        """Unittest."""
        with monkeypatch.context() as m:
            m.setattr(pkg.secrets, 'randbelow', lambda _: entrance)
            assert pkg.secrets.randbelow(42) == entrance
        monkeypatch.setattr('secrets.randbelow', lambda _: entrance)
        word = self.obj.carrega_palavra_secreta()
        assert self.obj.inicializa_letras_acertadas(word) == [
            '_' for _ in expected
        ]

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('j', 'J', marks=[]),
            pytest.param('e', 'E', marks=[]),
            pytest.param('s', 'S', marks=[]),
            pytest.param('u', 'U', marks=[]),
        ],
    )
    def test_pede_chute(self, entrance, expected, monkeypatch):
        """Unitest."""
        monkeypatch.setattr('builtins.input', lambda _: entrance)
        assert self.obj.pede_chute() == expected

    def test_marca_chute_correto(self, monkeypatch) -> NoReturn:
        """Unittest."""

        def mock_return(*_):
            return 3

        monkeypatch.setattr('secrets.randbelow', mock_return)

        word = self.obj.carrega_palavra_secreta()
        kicks = 'A'
        letters = self.obj.inicializa_letras_acertadas(word)

        self.obj.marca_chute_correto(kicks, letters, word)
        assert letters == ['A', '_', 'A', '_', 'A', '_', '_']

    def test_msg_vencedor(self, capsys) -> NoReturn:
        """Unittest."""
        self.obj.imprime_mensagem_vencedor()
        out, err = capsys.readouterr()
        assert out == (
            'Parabéns, você ganhou!\n'
            '       ___________      \n'
            "      '._==_==_=_.'     \n"
            '      .-\\\\:      /-.    \n'
            '     | (|:.     |) |    \n'
            "      '-|:.     |-'     \n"
            '        \\\\::.    /      \n'
            "         '::. .'        \n"
            '           ) (          \n'
            "         _.' '._        \n"
            "        '-------'       \n"
        )
        assert err == ''

    def test_msg_perdedor(self, capsys, monkeypatch) -> NoReturn:
        """Unittest."""

        def mock_return(*_):
            return 3

        monkeypatch.setattr('secrets.randbelow', mock_return)
        word = self.obj.carrega_palavra_secreta()
        self.obj.imprime_mensagem_perdedor(word)
        out, _ = capsys.readouterr()
        assert out == (
            'Puxa, você foi enforcado!\n'
            'A palavra era ABACAXI\n'
            '    _______________         \n'
            '   /               \\       \n'
            '  /                 \\      \n'
            '//                   \\/\\  \n'
            '\\|   XXXX     XXXX   | /   \n'
            ' |   XXXX     XXXX   |/     \n'
            ' |   XXX       XXX   |      \n'
            ' |                   |      \n'
            ' \\__      XXX      __/     \n'
            '   |\\     XXX     /|       \n'
            '   | |           | |        \n'
            '   | I I I I I I I |        \n'
            '   |  I I I I I I  |        \n'
            '   \\_             _/       \n'
            '     \\_         _/         \n'
            '       \\_______/           \n'
        )

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                0,
                (
                    '\n  _______     \n'
                    ' |/      |    \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    '_|___         \n\n'
                ),
                marks=[],
            ),
            pytest.param(
                1,
                (
                    '\n  _______     \n'
                    ' |/      |    \n'
                    ' |      (_)   \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    '_|___         \n\n'
                ),
                marks=[],
            ),
            pytest.param(
                2,
                (
                    '\n  _______     \n'
                    ' |/      |    \n'
                    ' |      (_)   \n'
                    ' |      \\     \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    '_|___         \n\n'
                ),
                marks=[],
            ),
            pytest.param(
                3,
                (
                    '\n'
                    '  _______     \n'
                    ' |/      |    \n'
                    ' |      (_)   \n'
                    ' |      \\|    \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    '_|___         \n\n'
                ),
                marks=[],
            ),
            pytest.param(
                4,
                (
                    '\n'
                    '  _______     \n'
                    ' |/      |    \n'
                    ' |      (_)   \n'
                    ' |      \\|/   \n'
                    ' |            \n'
                    ' |            \n'
                    ' |            \n'
                    '_|___         \n\n'
                ),
                marks=[],
            ),
            pytest.param(
                7,
                (
                    '\n'
                    '  _______     \n'
                    ' |/      |    \n'
                    ' |      (_)   \n'
                    ' |      \\|/   \n'
                    ' |       |    \n'
                    ' |      / \\   \n'
                    ' |            \n'
                    '_|___         \n\n'
                ),
                marks=[],
            ),
        ],
    )
    def test_desenha_forca(self, capsys, entrance, expected) -> NoReturn:
        """Unittest."""
        self.obj.desenha_forca(entrance)
        out, _ = capsys.readouterr()
        assert out == expected


class TestCase:
    """Testcase."""

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('', '', marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Test 0."""
        assert entrance == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                'cep',
                '* frutas\n* carros\n* cep\n* cores\n',
                marks=[],
            ),
        ],
    )
    def test_op_arq_toml(
        self,
        entrance,
        expected,
        monkeypatch,
        capsys,
    ) -> NoReturn:
        """Unittest."""
        with monkeypatch.context() as m:
            m.setattr('builtins.input', lambda _: entrance)
            pkg.op_arq_toml(pkg.palavras_db)
            out, _ = capsys.readouterr()
            assert out == expected
