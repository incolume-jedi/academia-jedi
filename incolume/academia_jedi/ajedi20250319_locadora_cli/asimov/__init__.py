"""Exemplo Asimov adaptado."""

from dataclasses import dataclass

from icecream import ic
from incolume.academia_jedi.ajedi20250319_locadora_cli import clear


@dataclass
class Carro:
    """Carro class."""

    montadora: str
    modelo: str
    ano: int
    diaria: float


carros: list[Carro] = [
    Carro('Chevrolet', 'Tracker', 2024, 120),
    Carro('Chevrolet', 'Onix', 2024, 90),
    Carro('Chevrolet', 'Spin', 2024, 150),
    Carro('Hyundai', 'HB20', 2024, 85),
    Carro('Hyundai', 'HB20S', 2024, 110),
    Carro('Hyundai', 'Tucson', 2024, 120),
    Carro('Fiat', 'Uno', 2024, 60),
    Carro('Fiat', 'Mobi', 2024, 70),
    Carro('Fiat', 'Pulse', 2025, 130),
]
alugados: list[Carro] = []

place_holder_carros: str = '[{}] {} ({}) - R$ {} /dia. \n'


def mostrar_lista_carros(ls_carros: list[Carro]) -> None:
    """Show cars."""
    result = ''
    for idx, car in enumerate(ls_carros):
        result += place_holder_carros.format(
            idx,
            car.modelo,
            car.montadora,
            car.diaria,
        )
    print(result)


def alugar_carro(ls_carros: list[Carro], ls_alugados: list[Carro]) -> None:
    """Alugar carro."""
    mostrar_lista_carros(ls_carros)
    print('==========')
    while (cod_car := int(input('Escolha o código do carro: '))) not in range(
        len(ls_carros),
    ):
        pass
    dias = int(input('Quantas diarias? '))
    carro = ls_carros[cod_car]
    valor = carro.diaria * dias
    print(
        f'Você escolheu {carro.montadora}/{carro.modelo} por {dias} dias.',
        f'Valor total da reserva R$ {valor:.02f}',
        sep='\n',
        end='\n\n',
    )
    if input('Deseja alugar (*s|n)? ').casefold() in ['n', 'no', 'não']:
        print('Reserva cancelada!')
        return
    print(
        'Parabéns você alugou o'
        f' {carro.montadora}/{carro.modelo}({carro.ano})'
        f' por {dias} dias, no valor de R$ {valor:.02f}.',
    )
    ls_alugados.append(ls_carros.pop(cod_car))


def devolver_carro(ls_carros: list[Carro], ls_alugados: list[Carro]) -> None:
    """Devolver carro."""
    if not ls_alugados:
        print('Não constam veiculos para devolução.')
        return
    print('Segue a listagem dos veiculos para devolução.')
    mostrar_lista_carros(ls_alugados)
    while (cod_car := int(input('Qual deseja devolver? '))) not in range(
        len(ls_alugados),
    ):
        pass
    carro = ls_alugados[cod_car]
    if (
        input(
            'Confirma a devolução do '
            f'{carro.montadora}/{carro.modelo}({carro.ano})? (s)im | *(n)ão ',
        ).casefold()
        == 's'
    ):
        ls_carros.append(ls_alugados.pop(cod_car))
        print(
            f'{carro.montadora}/{carro.modelo}({carro.ano})'
            ' Devolvido com sucesso!',
        )
    return


def run():
    """Run it."""
    while True:
        clear()
        print(
            '==========',
            'Bem vindo à locadora de carros!',
            '==========',
            'O que deseja fazer?',
            '',
            ' 0 - Mostrar portifólio |'
            ' 1 - Alugar um carro |'
            ' 2 - Devolver carro |'
            ' t - terminar ',
            sep='\n',
        )
        match op := input():
            case '0':
                mostrar_lista_carros(carros)
            case '1':
                alugar_carro(carros, alugados)
            case '2':
                devolver_carro(carros, alugados)
            case 't':
                break
            case _:
                print(op)

        if input('Deseja finalizar (S)im *(N)ão? ').casefold() in ['s', 'sim']:
            break


if __name__ == '__main__':
    ic()
    run()
