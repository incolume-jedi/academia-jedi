def subareas(*args):
    match args:
        case [area]:
            print(f'{area} não possui subareas.')
        case [area, args]:
            print(f'"{area}" possui apenas uma subarea: "{args}"')
        case [area, *args]:
            print(
                f'"{area}" possui {len(args):02} subareas. São elas: "{args}"'
            )


def run():
    """"""
    subareas('matemática')
    subareas('design', 'costura')
    subareas(
        'Ciências da Computação',
        'Analise de Sistemas',
        'Computação Gráfica',
        'Engenharia da Computação',
        'Engenheiro de Dados',
        'Analista de Bando de Dados',
        'Analista de Redes',
    )


if __name__ == '__main__':  # pragma: no cover
    run()
