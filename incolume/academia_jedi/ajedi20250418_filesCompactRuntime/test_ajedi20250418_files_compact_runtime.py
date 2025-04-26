"""Estudo sobre compactação em runtime."""
# ruff: noqa: E501

import io
from typing import ClassVar, NoReturn
import zipfile

import pytest
import incolume.academia_jedi.ajedi20250418_filesCompactRuntime as pkg
from pathlib import Path
from tempfile import gettempdir
from icecream import ic
from config import settings
import httpx


ic.disable()
if settings.debug_mode:
    ic.enable()


@pytest.mark.slow()
@pytest.mark.webtest()
class TestCase:
    """TestCase."""

    target_file: str = 'source/dignissimos.txt'
    msg: ClassVar[list] = [
        'Input files may not be found..',
        'I have no idea!!!',
    ]

    @classmethod
    def setup_class(cls):
        """Setup class."""
        cls.localzip = pkg.set_env(count=15, seed=191)

    @classmethod
    def teardown_class(cls):
        """Teardown class."""

    def test_0(self) -> NoReturn:
        """Unittest."""
        assert self.localzip == Path(gettempdir()).joinpath(
            'ajedi20250418_filesCompactRuntime',
            'archives.zip',
        )

    def test_1(self) -> NoReturn:
        """Unittest."""
        expected = (
            'Porque Deus amou o mundo de tal maneira que deu o seu Filho'
            ' unigênito,\n para que todo aquele que nele crê não pereça,'
            ' mas tenha a vida eterna.'
        )
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open(self.target_file) as file,
        ):
            assert expected in io.TextIOWrapper(file, encoding='utf-8').read()

    def test_2(self) -> NoReturn:
        """Unittest."""
        expected = {
            b'\xc2\xb9\xe2\x81\xb6 Porque Deus amou o mundo de'
            b' tal maneira que deu o seu '
            b'Filho unig\xc3\xaanito,\n',
            b' para que todo aquele que nele cr\xc3\xaa n\xc3\xa3o'
            b' pere\xc3\xa7a, mas te'
            b'nha a vida eterna.\n',
        }
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open('source/dignissimos.txt') as file,
        ):
            assert ic(expected).issubset(ic(file.readlines()))

    def test_3(self) -> NoReturn:
        """Unittest."""
        expected = {
            '¹⁶ Porque Deus amou o mundo de tal maneira que deu o'
            ' seu Filho unigênito,\n',
            ' para que todo aquele que nele crê não pereça,'
            ' mas tenha a vida eterna.\n',
        }
        with (
            zipfile.ZipFile(self.localzip) as handle,
            handle.open(self.target_file) as file,
        ):
            result = [line.decode('utf-8') for line in file]
            assert expected.issubset(result)

    @pytest.mark.parametrize(
        'entrance target_file expected'.split(),
        [
            pytest.param(
                pkg.URL.fifa17,
                'CLEAN_FIFA17_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,'
                    b'Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                    b'Preferred Foot,International Reputation,Weak Foot,'
                    b'Skill Moves,Work Rate,Body Type,Real Face,Position,'
                    b'Jersey Number,Joined,Loaned From,Contract Valid Until,'
                    b'Height(cm.),Weight(lbs.),Crossing,Finishing,'
                    b'HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,'
                    b'FKAccuracy,LongPassing,BallControl,Acceleration,'
                    b'SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,'
                    b'Stamina,Strength,LongShots,Aggression,Interceptions,'
                    b'Positioning,Vision,Penalties,Composure,Marking,'
                    b'StandingTackle,SlidingTackle,GKDiving,GKHandling,'
                    b'GKKicking,GKPositioning,GKReflexes,Best Position,'
                    b'Best Overall Rating,Year_Joined\r\n'
                ),
            ),
            pytest.param(
                pkg.URL.fifa18,
                'CLEAN_FIFA18_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential'
                    b',Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                    b'Preferred Foot,International Reputation,Weak Foot,Skill'
                    b' Moves,Work Rate,Body Type,Real Face,Position,Jersey'
                    b' Number,Joined,Loaned From,Contract Valid Until,'
                    b'Height(cm.),Weight(lbs.),Crossing,Finishing,'
                    b'HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,'
                    b'FKAccuracy,LongPassing,BallControl,Acceleration,'
                    b'SprintSpeed,Agility,Reactions,Balance,ShotPower,'
                    b'Jumping,Stamina,Strength,LongShots,Aggression,'
                    b'Interceptions,Positioning,Vision,Penalties,Composure,'
                    b'Marking,StandingTackle,SlidingTackle,GKDiving,'
                    b'GKHandling,GKKicking,GKPositioning,GKReflexes,Best'
                    b' Position,Best Overall Rating,Release'
                    b' Clause(\xc2\xa3),Year_Joined\r\n'
                ),
            ),
            pytest.param(
                pkg.URL.fifa19,
                'CLEAN_FIFA19_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,Preferred Foot,International Reputation,Weak Foot,Skill Moves,Work Rate,Body Type,Real Face,Position,Jersey Number,Joined,Loaned From,Contract Valid Until,Height(cm.),Weight(lbs.),Crossing,Finishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongPassing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,Vision,Penalties,Composure,Marking,StandingTackle,SlidingTackle,GKDiving,GKHandling,GKKicking,GKPositioning,GKReflexes,Best Position,Best Overall Rating,Release Clause(\xc2\xa3),Year_Joined\r\n'
                ),
            ),
            pytest.param(
                pkg.URL.fifa20,
                'CLEAN_FIFA20_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,Club,Club Logo,Val'
                    b'ue(\xc2\xa3),Wage(\xc2\xa3),Special,Preferred Foot,International Reputation,'
                    b'Weak Foot,Skill Moves,Work Rate,Body Type,Real Face,Position,Jersey Number,J'
                    b'oined,Loaned From,Contract Valid Until,Height(cm.),Weight(lbs.),Crossing,Fin'
                    b'ishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongP'
                    b'assing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPo'
                    b'wer,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,'
                    b'Vision,Penalties,Composure,Marking,StandingTackle,SlidingTackle,GKDiving,GKH'
                    b'andling,GKKicking,GKPositioning,GKReflexes,Best Position,Best Overall Rating'
                    b',Release Clause(\xc2\xa3),DefensiveAwareness,Year_Joined\r\n'
                ),
            ),
            pytest.param(
                pkg.URL.fifa21,
                'CLEAN_FIFA21_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,Club,Club Logo,Val'
                    b'ue(\xc2\xa3),Wage(\xc2\xa3),Special,Preferred Foot,International Reputation,'
                    b'Weak Foot,Skill Moves,Work Rate,Body Type,Real Face,Position,Jersey Number,J'
                    b'oined,Loaned From,Contract Valid Until,Height(cm.),Weight(lbs.),Crossing,Fin'
                    b'ishing,HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,FKAccuracy,LongP'
                    b'assing,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPo'
                    b'wer,Jumping,Stamina,Strength,LongShots,Aggression,Interceptions,Positioning,'
                    b'Vision,Penalties,Composure,Marking,StandingTackle,SlidingTackle,GKDiving,GKH'
                    b'andling,GKKicking,GKPositioning,GKReflexes,Best Position,Best Overall Rating'
                    b',Release Clause(\xc2\xa3),DefensiveAwareness,Year_Joined\r\n'
                ),
            ),
            pytest.param(
                pkg.URL.fifa22,
                'CLEAN_FIFA22_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,'
                    b'Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                    b'Preferred Foot,International Reputation,Weak Foot,'
                    b'Skill Moves,Work Rate,Body Type,Real Face,Position,'
                    b'Jersey Number,Joined,Loaned From,Contract Valid Until,'
                    b'Height(cm.),Weight(lbs.),Crossing,Finishing,'
                    b'HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,'
                    b'FKAccuracy,LongPassing,BallControl,Acceleration,'
                    b'SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,'
                    b'Stamina,Strength,LongShots,Aggression,Interceptions,'
                    b'Positioning,Vision,Penalties,Composure,Marking,'
                    b'StandingTackle,SlidingTackle,GKDiving,GKHandling,'
                    b'GKKicking,GKPositioning,GKReflexes,Best Position,'
                    b'Best Overall Rating,Release Clause(\xc2\xa3),'
                    b'DefensiveAwareness,Year_Joined\r\n'
                ),
            ),
            pytest.param(
                pkg.URL.zip,
                'CLEAN_FIFA22_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,'
                    b'Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                    b'Preferred Foot,International Reputation,Weak Foot,'
                    b'Skill Moves,Work Rate,Body Type,Real Face,Position,'
                    b'Jersey Number,Joined,Loaned From,Contract Valid Until,'
                    b'Height(cm.),Weight(lbs.),Crossing,Finishing,'
                    b'HeadingAccuracy,ShortPassing,Volleys,Dribbling,Curve,'
                    b'FKAccuracy,LongPassing,BallControl,Acceleration,'
                    b'SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,'
                    b'Stamina,Strength,LongShots,Aggression,Interceptions,'
                    b'Positioning,Vision,Penalties,Composure,Marking,'
                    b'StandingTackle,SlidingTackle,GKDiving,GKHandling,'
                    b'GKKicking,GKPositioning,GKReflexes,Best Position,'
                    b'Best Overall Rating,Release Clause(\xc2\xa3),'
                    b'DefensiveAwareness,Year_Joined\r\n'
                ),
            ),
            pytest.param(
                pkg.URL.fifa23,
                'CLEAN_FIFA23_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,'
                    b'Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                    b'Preferred Foot,International Reputation,Weak Foot,Skill'
                    b' Moves,Work Rate,Body Type,Real Face,Position,Joined,'
                    b'Loaned From,Contract Valid Until,Height(cm.),Weight(lbs.)'
                    b',Release Clause(\xc2\xa3),Kit Number,Best Overall Rating,'
                    b'Year_Joined\r\n'
                ),
                marks=[
                    pytest.mark.xfail(
                        zipfile.BadZipFile,
                        reason='i have no idea!',
                    ),
                ],
            ),
            pytest.param(
                pkg.URL.zip,
                'CLEAN_FIFA23_official_data.csv',
                (
                    b',ID,Name,Age,Photo,Nationality,Flag,Overall,Potential,'
                    b'Club,Club Logo,Value(\xc2\xa3),Wage(\xc2\xa3),Special,'
                    b'Preferred Foot,International Reputation,Weak Foot,Skill'
                    b' Moves,Work Rate,Body Type,Real Face,Position,Joined,'
                    b'Loaned From,Contract Valid Until,Height(cm.),Weight(lbs.)'
                    b',Release Clause(\xc2\xa3),Kit Number,Best Overall Rating,'
                    b'Year_Joined\r\n'
                ),
            ),
        ],
    )
    def test_4(self, entrance, target_file, expected) -> NoReturn:
        """Unittest."""
        file_zip = io.BytesIO(
            httpx.get(entrance).content,
        )  # carrega bytes com arquivo
        with (
            zipfile.ZipFile(file_zip) as handle,
            handle.open(target_file) as file,
        ):
            assert file.readline() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA17_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA17_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason=msg[0])],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA18_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA18_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason=msg[0])],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA19_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA19_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason=msg[0])],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA20_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA20_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason=msg[0])],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA21_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA21_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason=msg[0])],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA22_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA22_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason=msg[0])],
            ),
            pytest.param(
                Path.home()
                / 'Downloads'
                / 'archive'
                / 'CLEAN_FIFA23_official_data.csv',
                Path(gettempdir()).joinpath(
                    'ajedi20250418_filesCompactRuntime',
                    'CLEAN_FIFA23_official_data.zip',
                ),
                marks=[pytest.mark.xfail(reason=msg[0])],
            ),
        ],
    )
    def test_5(self, entrance, expected) -> NoReturn:
        """Unittest."""
        file_zip = self.localzip.parent / f'{entrance.stem}.zip'
        assert pkg.gen_zip(members=[entrance], zipname=file_zip) == expected

    def test_6(self) -> NoReturn:
        """Unittest."""
        entrance = (
            Path.home()
            .joinpath('Downloads', 'archive')
            .glob('CLEAN_FIFA*_official_data.csv')
        )
        expected = Path(gettempdir()).joinpath(
            'ajedi20250418_filesCompactRuntime',
            'CLEAN_FIFA.zip',
        )
        file_zip = self.localzip.parent / 'CLEAN_FIFA.zip'
        assert (
            pkg.gen_zip(members=ic(list(entrance)), zipname=file_zip)
            == expected
        )
