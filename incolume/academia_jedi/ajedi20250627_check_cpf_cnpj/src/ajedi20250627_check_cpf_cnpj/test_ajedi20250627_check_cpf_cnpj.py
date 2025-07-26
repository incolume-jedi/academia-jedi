"""Test for ajedi20250627_check_cpf_cnpj package."""

from __future__ import annotations
from typing import ClassVar, NoReturn
import pytest
from validate_docbr import CPF, CNPJ


class TestAjedi20250627CheckCpfCnpj:
    """Test class for ajedi20250627_check_cpf_cnpj package."""

    cpf: ClassVar = CPF()
    cnpj: ClassVar = CNPJ()

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('12345678900', False, marks=[]),
            pytest.param('00000000191', True, marks=[]),
            pytest.param('00000000272', True, marks=[]),
            pytest.param(cpf.generate(), True, marks=[]),
        ],
    )
    def test_check_cpf(self, entrance, expected) -> NoReturn:
        """Test the main function."""
        assert self.cpf.validate(entrance) == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param('12345678900', False, marks=[]),
            pytest.param('00000000191', False, marks=[]),
            pytest.param('00000000272', False, marks=[]),
            pytest.param('87777426622054', True, marks=[]),
            pytest.param('62898915347733', True, marks=[]),
            pytest.param(cnpj.generate(), True, marks=[]),
        ],
    )
    def test_check_cnpj(self, entrance, expected) -> NoReturn:
        """Test the main function."""
        assert self.cnpj.validate(entrance) == expected
