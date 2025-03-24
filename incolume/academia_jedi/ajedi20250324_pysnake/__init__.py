"""Pysnake module."""

import curses
from dataclasses import dataclass, asdict
import time
from typing import NamedTuple
from collections import namedtuple
import logging
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


def game_loop(window):
    """Loop."""
    curses.curs_set(0)
    heigth, width = window.getmaxyx()
    personagem = Personagem(10, 15, curses.ACS_DIAMOND)

    window.border(0)
    window.addch(personagem.lin, personagem.col, personagem.simbol)
    while True:
        window.timeout(1000)
        char = window.getch()
        window.clear()
        match char:
            case curses.KEY_UP:
                logging.debug(ic('MOVE UP'))
                personagem.lin -= 1
            case curses.KEY_DOWN:
                logging.debug(ic('MOVE DOWN'))
                personagem.lin += 1
            case curses.KEY_LEFT:
                logging.debug(ic('MOVE LEFT'))
                personagem.col -= 1

            case curses.KEY_RIGHT:
                logging.debug(ic('MOVE RIGHT'))
                personagem.col += 1
            case _:
                pass
        window.border(0)
        if (personagem.lin <= 0) or (personagem.lin >= heigth -1):
            return
        if (personagem.col <=0) or(personagem.col >= width -1):
            return

        window.addch(personagem.lin, personagem.col, personagem.simbol)




def run():
    """Run it."""
    curses.wrapper(game_loop)
    print('Fim de jogo!!!!')


if __name__ == '__main__':
    run()
