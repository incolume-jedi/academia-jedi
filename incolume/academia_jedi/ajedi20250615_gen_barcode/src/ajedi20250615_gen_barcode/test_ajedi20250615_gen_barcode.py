"""Module test."""

from faker import Faker
from . import gen_barcode, barcode
import pytest
from tempfile import gettempdir
from pathlib import Path
from icecream import ic


Faker.seed(149)
fake = Faker('pt-br')


class Testclass:
    """Suite test."""

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.dout = Path(gettempdir(), cls.__name__)
        cls.dout.mkdir(
            parents=True,
            exist_ok=True,
        )

    @classmethod
    def teardown_class(cls):
        """Teardown class.

        Teardown da classe. Remove todos os arquivos
         e diretórios gerados ao final.
        """
        shutil.rmtree(cls.dout)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('123456789098', True),
            pytest.param('314159265358', True),
            pytest.param('987412563210', True),
            pytest.param(fake.numerify(text='############'), True),
            pytest.param(
                fake.numerify(text='#####'),
                {
                    'expected_exception': barcode.errors.NumberOfDigitsError,
                    'match': 'UPC must have 11 digits, not 5.',
                },
            ),
            pytest.param(
                fake.numerify(text='###-###-####'),
                {
                    'expected_exception': barcode.errors.IllegalCharacterError,
                    'match': 'UPC code can only contain numbers.',
                },
            ),
            pytest.param(
                '1234567890cc',
                {
                    'expected_exception': barcode.errors.IllegalCharacterError,
                    'match': 'UPC code can only contain numbers.',
                },
            ),
            pytest.param(
                fake.numerify(text='##############'),
                {
                    'expected_exception': ValueError,
                    'match': 'UPC must have 11 digits, not more',
                },
            ),
            pytest.param(
                fake.numerify(text='##########'),
                {
                    'expected_exception': barcode.errors.NumberOfDigitsError,
                    'match': 'UPC must have 11 digits, not',
                },
            ),
        ],
    )
    def test_type_upc(self, entrance, expected):
        """Verify upc."""
        if isinstance(expected, dict) and 'expected_exception' in expected:
            with pytest.raises(**expected):
                gen_barcode(entrance, diroutput=self.dout)
        else:
            assert ic(gen_barcode(entrance, diroutput=self.dout)) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'padron': 'isbn13',
                    'code': fake.numerify(text='9791#########'),
                },
                {},
            ),
            pytest.param(
                {
                    'padron': 'isbn13',
                    'code': fake.numerify(text='978##########'),
                },
                {},
            ),
        ],
    )
    def test_type_isbn(self, entrance, expected):
        """Verify isbn."""
        if 'expected_exception' in expected:
            with pytest.raises(**expected):
                gen_barcode(entrance, diroutput=self.dout)
        assert gen_barcode(**ic(entrance), diroutput=self.dout)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'padron': 'ean13',
                    'code': fake.numerify(text='############'),
                },
                {},
            ),
            pytest.param(
                {
                    'padron': 'ean13',
                    'code': fake.numerify(text='978##########'),
                },
                {},
            ),
        ],
    )
    def test_type_ean(self, entrance, expected):
        """Verify isbn."""
        if 'expected_exception' in expected:
            with pytest.raises(**expected):
                gen_barcode(entrance, diroutput=self.dout)
        assert gen_barcode(**ic(entrance), diroutput=self.dout)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'padron': 'code39',
                    'code': fake.numerify(text='############'),
                },
                {},
            ),
            pytest.param(
                {
                    'padron': 'code128',
                    'code': fake.numerify(text='978##########'),
                },
                {},
            ),
        ],
    )
    def test_type_code(self, entrance, expected):
        """Verify isbn."""
        if 'expected_exception' in expected:
            with pytest.raises(**expected):
                gen_barcode(entrance, diroutput=self.dout)
        assert gen_barcode(**ic(entrance), diroutput=self.dout)
