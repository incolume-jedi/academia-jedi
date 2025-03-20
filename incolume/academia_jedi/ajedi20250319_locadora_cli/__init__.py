"""Locadora CLI."""

from collections.abc import Container
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path

import yaml
from icecream import ic
import os


fileconf = Path(__file__).parent / 'locadora.yaml'

config = ic(yaml.safe_load(fileconf.open()))


Montadora: IntEnum = IntEnum(
    'Montadora',
    config['montadoras'],
    module=__name__,
)
Categoria: IntEnum = IntEnum(
    'Categoria',
    config['categorias'],
    module=__name__,
)


@dataclass
class Veiculo:
    """Veiculo dataclass."""

    modelo: str
    ano: int
    montadora: Montadora
    categoria: Categoria


class Locadora:
    """Locadora class."""
    title: str = 'Locadora Incolume'
    barra1: str = '='*80
    barra2: str = '-'*80
    def tela1(self) -> None:
        """Tela1."""
        return f'''
            {self.barra1}
            {f".. {self.title} ..":^80}
            {self.barra1}
            {self.barra2}
            {"(C)Todos os direitos reservados":>80}
            {self.barra2}'''
    @staticmethod
    def clear():
        """Clear screen."""
        os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605

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

    def menu(self, tela: str, options: Container[str]):
        """Menu."""
        while True:
            self.clear()
            print('=' * 30)
            print(f'{"Calculadora CLI":^30}')
            print('-' * 30)
            for idx, item in enumerate(options):
                print(f'   {idx}: {item}')

            op = input('\nEscolha a opção: ')
            if op == '0':
                break

            try:
                print()
            except (ValueError, TypeError):
                msg = 'Opção inválida!'
                print(f'\n\t{msg}\n')

            print('-' * 30)

            if self.finalizar(
                'deseja realizar outra operação (Y/n)? ',
                ['f', 'finalize', 't', 'terminar'],
            ):
                break

    def run(self):
        """Run it."""
        # self.menu([1,2])
        self.clear()
        print(self.tela1())





if __name__ == '__main__':
    """..."""
    ic(list(Categoria))
    ic(v := yaml.safe_load(fileconf.open()))
    Animals0 = IntEnum('Animals', v['categorias'])
    Animals1 = IntEnum(
        'Animals',
        {'CHARTREUSE': 7, 'SEA_GREEN': 11, 'ROSEMARY': 42},
    )
    ic(list(Animals0), list(Animals1))
    Locadora().run()
