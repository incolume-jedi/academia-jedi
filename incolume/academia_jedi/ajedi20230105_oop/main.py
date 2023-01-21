import frutas
import interface
import random


def run():
    fruta = interface.Fruta(nome="Manga espada")
    manga = frutas.Manga(0.2)
    print(fruta)
    print(isinstance(manga, interface.Fruta), manga)

    uva = frutas.Uva(1)
    print(isinstance(uva, interface.Fruta), uva)

    pontos = [
        interface.Point(random.randint(0, 5), random.randint(0, 5)) for _ in range(5)
    ]
    print(pontos)
    print(f"{pontos[0]}")


if __name__ == "__main__":
    run()
