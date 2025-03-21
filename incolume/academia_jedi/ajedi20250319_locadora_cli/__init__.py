"""Locadora CLI."""

# ruff:noqa: T201
import os
from collections.abc import Container
from dataclasses import asdict, dataclass
from enum import IntEnum
from pathlib import Path

import yaml
from icecream import ic

fileconf = Path(__file__).parent / 'locadora.yaml'

config = ic(yaml.safe_load(fileconf.open()))


def clear():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605


@classmethod
def _missing_(cls, value):
    """Method missing.

    Método chamado quando um valor não é encontrado no enumerador.
    Tenta encontrar o membro correspondente com base no nome ou valor.
    """
    if isinstance(value, str) and value.isdigit():
        value = int(value)
    else:
        value = value.capitalize()

    for member in cls:
        if value in (member.name, member.value):
            return member

    return None


Montadora: IntEnum = IntEnum(
    'Montadora',
    {key.capitalize(): value for key, value in config['montadoras'].items()},
    module=__name__,
)
Categoria: IntEnum = IntEnum(
    'Categoria',
    {key.capitalize(): value for key, value in config['categorias'].items()},
    module=__name__,
)

Categoria._missing_, Montadora._missing_ = _missing_, _missing_  # noqa: SLF001


@dataclass
class Veiculo:
    """Veiculo dataclass."""

    modelo: str
    ano: int
    montadora: Montadora
    categoria: Categoria
    diaria: float
    chassi: str

    def __post_init__(self):
        """Post init."""
        self.montadora = Montadora(str(self.montadora))
        self.categoria = Categoria(str(self.categoria))

    def to_dict(self):
        """To dict."""
        result = asdict(self)
        result['montadora'] = self.montadora.value
        result['categoria'] = self.categoria.value
        return result


veiculos: list[Veiculo] = [Veiculo(**x) for x in config['veiculos']]


class Locadora:
    """Locadora class."""

    title: str = 'Locadora Incolume'
    barra1: str = '=' * 80
    barra2: str = '-' * 80

    @staticmethod
    def finalizar(
        msg: str = '',
        deny_options: None | Container[str] = None,
    ) -> bool:
        """Finalizar menu em loop."""
        deny: list[str] = ['não', 'no', 'n', 'q', 'quit', 'sair', 's']
        if deny_options:
            deny.extend(item.casefold() for item in deny_options)
        msg = msg or 'deseja realizar outra operação (Y/n)? '
        op = input(msg)
        return op.casefold() in deny

    def locar_veiculo(self):
        """Locar veículo."""
        print('locar')

    def devolver_veiculo(self):
        """Devolver veículo."""
        print('devolver')

    def options(self, array: Container) -> None:
        """Options."""
        clear()
        print(f"""
            {self.barra1}
            {f'.. {self.title} ..':^80}
            {self.barra1}""")
        for idx, item in enumerate(array):
            print(f'\t\t\t\t[ {idx} ] {item}')
        print(f"""
            {self.barra2}
            {'(C)Todos os direitos reservados':>80}
            {self.barra2}""")

    def mostrar_lista_carros(self, ls_carros: list[Veiculo], place_holder: str = '') -> None:
        """Show cars."""
        place_holder = place_holder or '[{}] {} ({}) - R$ {} /dia.'
        result = ''
        for idx, car in enumerate(ls_carros):
            result += f'{
                place_holder.format(
                    idx,
                    car.modelo,
                    car.montadora.name,
                    car.diaria,
                )
            }\n'
        print(result)

    def menu(self) -> None:
        """Menu."""
        while True:
            self.options([
                'Sair',
                'Veiculos disponível',
                'Alugar veículo',
                'devolver veículo',
            ])

            op = input('\nEscolha a opção desejada: ')

            match op:
                case '0':
                    break
                case '1':
                    self.options(veiculos)
                case '2':
                    self.locar_veiculo()
                case '3':
                    self.devolver_veiculo()
                case _:
                    msg = 'Opção inválida!'
                    print(f'\n\t{msg}\n')

            if self.finalizar(
                'deseja realizar outra operação (Y/n)? ',
                ['f', 'finalize', 't', 'terminar'],
            ):
                break

    def run(self):
        """Run it."""
        self.clear()


def others_exec() -> None:
    """Outras execuções."""
    ic(list(Categoria))
    ic(v := yaml.safe_load(fileconf.open()))
    animals0 = IntEnum('Animals', v['categorias'])
    animals1 = IntEnum(
        'Animals',
        {'CHARTREUSE': 7, 'SEA_GREEN': 11, 'ROSEMARY': 42},
    )
    ic(list(animals0), list(animals1))
    ic(
        Categoria('carga'),
        Categoria('CARGA'),
        Categoria(1),
        Categoria('Carga'),
    )


if __name__ == '__main__':
    """..."""
    # Locadora().menu()
    Locadora().mostrar_lista_carros(veiculos)
