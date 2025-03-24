"""Pysnake module."""

import curses
import logging
import time
from collections import namedtuple
from dataclasses import asdict, dataclass
from typing import Any, NamedTuple

from icecream import ic


@dataclass
class Personagem:
    """Personagem class"""

    lin: int
    col: int
    simbol: int

    def asdict(self):
        """As dict."""
        return asdict(self)

def draw_screen(window: Any) -> None:
    """Desenhar tela."""
    window.clear()
    window.border(0)

def draw_actor(actor: Personagem, window: Any) -> None:
    """Desenha ator."""
    window.addch(actor.lin, actor.col, actor.simbol)

def get_new_direction(window: Any, timeout:int = 1000) -> int|None:
    """Checa nova direção."""
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        return direction
    return

def move_actor(actor: Personagem, direction: int) -> None:
    """Move ator."""
    match direction:
        case curses.KEY_UP:
            logging.debug(ic('MOVE UP'))
            actor.lin -= 1
        case curses.KEY_DOWN:
            logging.debug(ic('MOVE DOWN'))
            actor.lin += 1
        case curses.KEY_LEFT:
            logging.debug(ic('MOVE LEFT'))
            actor.col -= 1

        case curses.KEY_RIGHT:
            logging.debug(ic('MOVE RIGHT'))
            actor.col += 1

def check_actor_hit_border(actor: Personagem, window: Any) -> bool:
    """Checa limite tela."""
    heigth, width = window.getmaxyx()
    return ((actor.lin <= 0) or (actor.lin >= heigth - 1)) or ((actor.col <= 0) or (actor.col >= width - 1))



def game_loop(window):
    """Loop."""
    curses.curs_set(0)
    personagem = Personagem(10, 15, curses.ACS_DIAMOND)


    while True:
        draw_screen(window)
        draw_actor(actor=personagem, window=window)
        if (direction:=get_new_direction(window=window)):
            move_actor(actor=personagem, direction=direction)
        if check_actor_hit_border(actor=personagem, window=window):
            return


def run():
    """Run it."""
    curses.wrapper(game_loop)
    print('Fim de jogo!!!!')


if __name__ == '__main__':
    run()
