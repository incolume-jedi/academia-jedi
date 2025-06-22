"""Estudo enum."""

from enum import IntEnum

# ruff: noqa: PLR2004
config = {
    'categorias': {
        'CARRO': 1,
        'MOTO': 2,
        'CAMINHAO': 3,
    },
}


@classmethod
def _missing_(cls, value):
    """Método chamado quando um valor não é encontrado no enumerador.

    Tenta encontrar o membro correspondente com base no nome ou valor.
    """
    if isinstance(value, str) and value.isdigit():
        value = int(value)
    else:
        value = value.upper()

    for member in cls:
        if value in (member.name, member.value):
            return member

    return None


Categoria: IntEnum = IntEnum(
    'Categoria',
    config['categorias'],
    module=__name__,
)

Categoria._missing_ = _missing_


if __name__ == '__main__':
    # Testando a classe Categoria
    print(Categoria.CARRO)  # Saída: Categoria.CARRO
    print(Categoria(1))  # Saída: Categoria.CARRO
    print(Categoria('carro'))  # Saída: Categoria.CARRO
    print(Categoria('1'))  # Saída: Categoria.CARRO
    print(Categoria.MOTO == 2)  # Saída: True
    print(Categoria('moto') == 2)  # Saída: True
    print(Categoria('CAMINHAO'))  # Saída: Categoria.CAMINHAO
