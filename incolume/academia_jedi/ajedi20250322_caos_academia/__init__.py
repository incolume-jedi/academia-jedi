"""Teoria do caos - academia."""

import random
import secrets
from enum import Enum

import seaborn as sns
from icecream import ic


class Academia:
    """Academia class."""

    def __init__(self):
        """Init."""
        self.halteres = list(range(10, 37, 2))
        self.porta_halteres = {}
        self.reiniciar_dia()

    def reiniciar_dia(self):
        """Reinicia o dia."""
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        """Listar hateres."""
        return [i for i in self.porta_halteres.values() if i != 0]

    def listar_espaços(self):
        """Listar hateres."""
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso: int) -> int:
        """Pegar haltere."""
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso

    def devolver_haltere(self, pos: int, peso: float) -> None:
        """Devolver haltere."""
        self.porta_halteres[pos] = peso

    def calcular_caos(self) -> float:
        """Calculo do caos."""
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)


Tipo: Enum = Enum('Tipo', 'organizado desorganizado'.split())


class Usuario:
    """Usuário class."""

    def __init__(
        self,
        tipo: Tipo = None,
        academia: Academia = None,
        peso: int = 0,
    ):
        """Init."""
        self.tipo = tipo
        self.academia = academia
        self.peso = peso

    def iniciar_treino(self):
        """Iniciar treino."""
        ls_pesos = self.academia.listar_halteres()
        self.peso = secrets.choice(ls_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        """Finalizar treino."""
        espaços = self.academia.listar_espaços()
        if self.tipo == Tipo.organizado:
            if self.peso in espaços:
                self.academia.devolver_haltere(self.peso, self.peso)
            else:
                pos = secrets.choice(espaços)
                self.academia.devolver_haltere(pos, self.peso)

        if self.tipo == Tipo.desorganizado:
            pos = secrets.choice(espaços)
            self.academia.devolver_haltere(pos, self.peso)
        self.peso = 0


if __name__ == '__main__':
    academia = Academia()
    usuarios = [Usuario(Tipo.desorganizado, academia)]
    usuarios.extend([Usuario(Tipo.organizado, academia) for _ in range(19)])
    random.shuffle(usuarios)
    ic(usuarios)
    list_chaos: list[float] = []

    for _ in range(50):
        academia.reiniciar_dia()
        for user in usuarios[:10]:
            user.iniciar_treino()
            user.iniciar_treino()
        list_chaos.append(academia.calcular_caos())

    sns.displot(list_chaos)
