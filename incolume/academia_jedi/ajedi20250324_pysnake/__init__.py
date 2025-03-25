"""Pysnake module."""

import curses
import logging
from copy import copy
from dataclasses import dataclass, field
import secrets
from icecream import ic

# ruff: noqa: T201


@dataclass
class Personagem:
    """Personagem class."""

    lin: int = field(default=10)
    col: int = field(default=15)

    def __post_init__(self):
        """Post init."""
        logging.debug(ic(self))
@dataclass
class Fruit(Personagem):
    """Fruit class."""
    simbol: str = ''

    def __post_init__(self):
        """Post init."""
        logging.debug(ic(self))

    def draw(self, window: curses.window):
        """Draw it."""
        logging.debug(ic())
        heigth, width = window.getmaxyx()
        self.lin = min(max(secrets.randbelow(heigth), 1), heigth -1)
        self.col = min(max(secrets.randbelow(width), 1), width -1)
        window.addch(self.lin, self.col, self.simbol)



@dataclass
class Snake:
    """Snake class."""

    segments: list[Personagem] = field(default_factory=list)
    symbol_head: str = '@'
    symbol_body: str = '§'

    def __post_init__(self):
        """Post init."""
        logging.debug(ic(self))
        self.segments = self.segments or [
            Personagem(),
            *[Personagem(lin=ln) for ln in range(9, 7, -1)],
        ]

    def move(self, direction: int) -> None:
        """Move snake."""
        logging.debug(ic())
        head = copy(self.segments[0])
        move_actor(head, direction)
        self.segments.insert(0, head)
        self.segments.pop()

    def draw(self, window: curses.window) -> None:
        """Draw snake."""
        logging.debug(ic())
        head = self.segments[0]
        window.addch(head.lin, head.col,self.symbol_head)
        for body in self.segments[1:]:
            window.addch(body.lin, body.col,self.symbol_body)


    def check_hit_border(self, window: curses.window) -> bool:
        """Check if hit border."""
        logging.debug(ic())
        return check_actor_hit_border(actor=self.segments[0], window=window)


def draw_screen(window: curses.window) -> None:
    """Desenhar tela."""
    window.clear()
    window.border(0)


def draw_actor(actor: Personagem, window: curses.window) -> None:
    """Desenha ator."""
    window.addch(actor.lin, actor.col, actor.simbol)


def get_new_direction(
    window: curses.window,
    timeout: int = 1000,
) -> int | None:
    """Checa nova direção."""
    window.timeout(timeout)
    direction = window.getch()
    if direction in [
        curses.KEY_UP,
        curses.KEY_DOWN,
        curses.KEY_LEFT,
        curses.KEY_RIGHT,
    ]:
        return direction
    return None


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


def check_actor_hit_border(actor: Personagem, window: curses.window) -> bool:
    """Checa limite tela."""
    heigth, width = window.getmaxyx()
    return ((actor.lin <= 0) or (actor.lin >= heigth - 1)) or (
        (actor.col <= 0) or (actor.col >= width - 1)
    )


def game_run(window):
    """Game loop."""
    curses.curs_set(0)
    snake = Snake()
    current_direction = curses.KEY_DOWN
    fruit = Fruit(simbol=curses.ACS_DIAMOND)
    while True:
        draw_screen(window)
        snake.draw(window=window)
        fruit.draw(window=window)
        if not (direction := get_new_direction(window=window)):
            direction = current_direction
        snake.move(direction=direction)
        if snake.check_hit_border(window=window):
            return
        current_direction = direction


def run():
    """Run it."""
    curses.wrapper(game_run)
    print('Fim de jogo!!!!')


if __name__ == '__main__':
    run()
