"""Pysnake module."""

import curses
import time


def game_loop(window):
    """Loop."""
    window.addstr('Aperte alguma tecla: \n')
    while True:
        window.timeout(1000)
        char = window.getch()
        window.clear()
        if char == -1:
            window.addstr('Nenhuma tecla precionada!!')
        else:
            window.addstr(f'tecla selecionada "{char}"\n')


def run():
    """Run it."""
    curses.wrapper(game_loop)


if __name__ == '__main__':
    run()
