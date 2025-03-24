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
        match char:
            case -1:
                window.addstr('Nenhuma tecla precionada!!')
            case curses.KEY_UP:
                window.addstr('MOVE UP')
            case curses.KEY_DOWN:
                window.addstr('MOVE DOWN')
            case curses.KEY_LEFT:
                window.addstr('MOVE LEFT')
            case curses.KEY_RIGHT:
                window.addstr('MOVE RIGHT')
            case 27:
                window.terminate()
            case _:
                window.addstr('Não mover')




def run():
    """Run it."""
    curses.wrapper(game_loop)


if __name__ == '__main__':
    run()
