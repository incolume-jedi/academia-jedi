from enum import Enum, auto


class Weekday0(Enum):
    DOM = auto()
    SEG = auto()
    TER = auto()
    QUA = auto()
    QUI = auto()
    SEX = auto()
    SAB = auto()


class Weekday(Enum):
    DOM = 'Domingo'
    SEG = 'Segunda'
    TER = 'Terça'
    QUA = 'Quarta'
    QUI = 'Quinta'
    SEX = 'Sexta'
    SAB = 'Sábado'


def weekend0(dia):
    match Weekday0(dia):
        case 1 | 7:
            return True
        case _:
            return False


def weekend(dia):
    match Weekday(dia).value:
        case 'Sábado' | 'Domingo':
            return True
        case _:
            return False


def run():
    print(Weekday0(1))

    print(Weekday('Segunda'), f"{weekend('Segunda')=}")
    print(Weekday('Domingo'), f"{weekend('Domingo')=}")
    print(Weekday('Sábado'), f"{weekend('Sábado')=}")
    print(f"{Weekday('Sexta')} {weekend('Sexta')=}")


if __name__ == '__main__':  # pragma: no cover
    run()
