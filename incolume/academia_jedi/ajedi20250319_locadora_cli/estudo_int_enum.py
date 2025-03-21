from enum import IntEnum

# Configuração de exemplo
config = {
    'categorias': {
        'CARRO': 1,
        'MOTO': 2,
        'CAMINHAO': 3,
    },
}


class Categoria(IntEnum):
    """Enumerador personalizado com suporte a busca por nome ou valor.
    """

    @classmethod
    def _missing_(cls, value):
        """Método chamado quando um valor não é encontrado no enumerador.
        Tenta encontrar o membro correspondente com base no nome ou valor.
        """
        if isinstance(value, str) and value.isdigit():
            # Se o valor for uma string numérica, converte para inteiro
            value = int(value)
        else:
            # Se o valor for uma string não numérica, capitaliza o texto
            value = (
                value.upper()
            )  # Usando `upper` para garantir compatibilidade

        # Procura o membro correspondente pelo nome ou valor
        for member in cls:
            if value in (member.name, member.value):
                return member

        # Retorna None se nenhum membro for encontrado
        return None


# Criando dinamicamente os membros do enumerador a partir da configuração
for name, value in config['categorias'].items():
    Categoria._value2member_map_[value] = Categoria(
        value,
    )  # Mapeamento interno do Enum
    setattr(Categoria, name, Categoria(value))

if __name__ == '__main__':
    # Testando a classe Categoria
    print(Categoria.CARRO)  # Saída: Categoria.CARRO
    print(Categoria(1))  # Saída: Categoria.CARRO
    print(Categoria('carro'))  # Saída: Categoria.CARRO
    print(Categoria('1'))  # Saída: Categoria.CARRO
    print(Categoria.MOTO == 2)  # Saída: True
    print(Categoria('moto') == 2)  # Saída: True
    print(Categoria('CAMINHAO'))  # Saída: Categoria.CAMINHAO
    print(Categoria('invalido'))  # Saída: None
