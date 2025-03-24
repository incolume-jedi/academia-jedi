"""Pysnake module."""

import curses
import time


def game_loop(window):
    """Loop."""
    for idx in range(10):
        window.addstr(f'i = {idx}\n')
        window.refresh()
        time.sleep(1)


def run():
    """Run it."""
    curses.wrapper(game_loop)


if __name__ == '__main__':
    run()
