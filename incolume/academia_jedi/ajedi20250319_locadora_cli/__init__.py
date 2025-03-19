"""Locadora CLI."""

from dataclasses import dataclass
from enum import IntEnum, auto
from pathlib import Path

import yaml
from icecream import ic

fileconf = Path(__file__).parent / 'locadora.yaml'

config = ic(yaml.safe_load(fileconf.open()))


Montadora: IntEnum = IntEnum('Montadora', config['montadora'], module=__name__)
Categoria: IntEnum = IntEnum('Categoria', config['categoria'], module=__name__)


@dataclass
class Veiculo:
    """Veiculo dataclass."""

    modelo: str
    montadora: Montadora
    categoria: Categoria


if __name__ == '__main__':
    """..."""
    ic(list(Categoria))
    ic(v := yaml.safe_load(fileconf.open()))
    Animals0 = IntEnum('Animals', v['categoria'])
    Animals1 = IntEnum(
        'Animals',
        {'CHARTREUSE': 7, 'SEA_GREEN': 11, 'ROSEMARY': 42},
    )
    ic(list(Animals1))
