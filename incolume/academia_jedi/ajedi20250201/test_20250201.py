"""Test module."""

import pytest
import incolume.academia_jedi.ajedi20250201 as pkg


class TestContrants:
    """Test case."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('A001', True, marks=[]),
            pytest.param('A002', True, marks=[]),
            pytest.param('ANN001', True, marks=[]),
            pytest.param('ANN002', True, marks=[]),
            pytest.param('ANN003', True, marks=[]),
            pytest.param('ANN201', True, marks=[]),
            pytest.param('ANN202', True, marks=[]),
            pytest.param('ANN204', True, marks=[]),
            pytest.param('ANN401', True, marks=[]),
            pytest.param('ARG001', True, marks=[]),
            pytest.param('ARG002', True, marks=[]),
            pytest.param('ASYNC101', True, marks=[]),
            pytest.param('B007', True, marks=[]),
            pytest.param('B008', True, marks=[]),
            pytest.param('B009', True, marks=[]),
            pytest.param('B011', True, marks=[]),
            pytest.param('B015', True, marks=[]),
            pytest.param('B904', True, marks=[]),
            pytest.param('B905', True, marks=[]),
            pytest.param('BLE001', True, marks=[]),
            pytest.param('C408', True, marks=[]),
            pytest.param('C419', True, marks=[]),
            pytest.param('C901', True, marks=[]),
            pytest.param('D100', True, marks=[]),
            pytest.param('D101', True, marks=[]),
            pytest.param('D102', True, marks=[]),
            pytest.param('D103', True, marks=[]),
            pytest.param('D104', True, marks=[]),
            pytest.param('D105', True, marks=[]),
            pytest.param('D107', True, marks=[]),
            pytest.param('D205', True, marks=[]),
            pytest.param('D402', True, marks=[]),
            pytest.param('D415', True, marks=[]),
            pytest.param('D419', True, marks=[]),
            pytest.param('DTZ001', True, marks=[]),
            pytest.param('DTZ003', True, marks=[]),
            pytest.param('DTZ005', True, marks=[]),
            pytest.param('DTZ007', True, marks=[]),
            pytest.param('E501', True, marks=[]),
            pytest.param('E741', True, marks=[]),
            pytest.param('EM101', True, marks=[]),
            pytest.param('EM102', True, marks=[]),
            pytest.param('ERA001', True, marks=[]),
            pytest.param('EXE005', True, marks=[]),
            pytest.param('F402', True, marks=[]),
            pytest.param('F403', True, marks=[]),
            pytest.param('F405', True, marks=[]),
            pytest.param('F601', True, marks=[]),
            pytest.param('F811', True, marks=[]),
            pytest.param('F821', True, marks=[]),
            pytest.param('F841', True, marks=[]),
            pytest.param('FBT001', True, marks=[]),
            pytest.param('FBT002', True, marks=[]),
            pytest.param('FBT003', True, marks=[]),
            pytest.param('FIX002', True, marks=[]),
            pytest.param('G001', True, marks=[]),
            pytest.param('G002', True, marks=[]),
            pytest.param('G004', True, marks=[]),
            pytest.param('N801', True, marks=[]),
            pytest.param('N802', True, marks=[]),
            pytest.param('N805', True, marks=[]),
            pytest.param('N806', True, marks=[]),
            pytest.param('N816', True, marks=[]),
            pytest.param('N999', True, marks=[]),
            pytest.param('NPY002', True, marks=[]),
            pytest.param('PD901', True, marks=[]),
            pytest.param('PERF203', True, marks=[]),
            pytest.param('PERF401', True, marks=[]),
            pytest.param('PERF402', True, marks=[]),
            pytest.param('PIE796', True, marks=[]),
            pytest.param('PLE1205', True, marks=[]),
            pytest.param('PLR0913', True, marks=[]),
            pytest.param('PLR1714', True, marks=[]),
            pytest.param('PLR2004', True, marks=[]),
            pytest.param('PLW0602', True, marks=[]),
            pytest.param('PLW0603', True, marks=[]),
            pytest.param('PLW2901', True, marks=[]),
            pytest.param('PT004', True, marks=[]),
            pytest.param('PT006', True, marks=[]),
            pytest.param('PT012', True, marks=[]),
            pytest.param('PT015', True, marks=[]),
            pytest.param('PTH118', True, marks=[]),
            pytest.param('PTH123', True, marks=[]),
            pytest.param('PYI024', True, marks=[]),
            pytest.param('PYI041', True, marks=[]),
            pytest.param('RET503', True, marks=[]),
            pytest.param('RET504', True, marks=[]),
            pytest.param('RUF001', True, marks=[]),
            pytest.param('RUF012', True, marks=[]),
            pytest.param('RUF013', True, marks=[]),
            pytest.param('S101', True, marks=[]),
            pytest.param('S113', True, marks=[]),
            pytest.param('S201', True, marks=[]),
            pytest.param('S301', True, marks=[]),
            pytest.param('S307', True, marks=[]),
            pytest.param('S310', True, marks=[]),
            pytest.param('S311', True, marks=[]),
            pytest.param('S602', True, marks=[]),
            pytest.param('S603', True, marks=[]),
            pytest.param('S605', True, marks=[]),
            pytest.param('S607', True, marks=[]),
            pytest.param('S608', True, marks=[]),
            pytest.param('SIM103', True, marks=[]),
            pytest.param('SIM109', True, marks=[]),
            pytest.param('SIM113', True, marks=[]),
            pytest.param('SIM115', True, marks=[]),
            pytest.param('SIM117', True, marks=[]),
            pytest.param('SLF001', True, marks=[]),
            pytest.param('SLOT000', True, marks=[]),
            pytest.param('T201', True, marks=[]),
            pytest.param('T203', True, marks=[]),
            pytest.param('TCH003', True, marks=[]),
            pytest.param('TD002', True, marks=[]),
            pytest.param('TD003', True, marks=[]),
            pytest.param('TD004', True, marks=[]),
            pytest.param('TRY002', True, marks=[]),
            pytest.param('TRY003', True, marks=[]),
            pytest.param('TRY300', True, marks=[]),
            pytest.param('TRY301', True, marks=[]),
            pytest.param('TRY401', True, marks=[]),
            pytest.param('W293', True, marks=[]),
        ],
    )
    def test_rules(self, entrance, expected):
        """Unit test."""
        assert (entrance in pkg.RULES) == expected

    def test_path(self):
        """Unittest."""
        assert set(pkg.project_path.parts).issuperset(
            'incolume academia_jedi'.split(),
        )

    def test_files(self):
        """Unittest."""
        assert next(pkg.python_files).exists()

    def test_noqa0(self):
        """Unittest."""
        file = next(pkg.python_files)
        assert pkg.edit_noqa_for_python_0(file)

    def test_noqa(self):
        """Unittest."""
        file = next(pkg.python_files)
        assert pkg.edit_noqa_for_python(file)
