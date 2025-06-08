"""Pysnake module."""

import curses
import logging
import os
import secrets
import time
from copy import copy
from dataclasses import dataclass, field

from icecream import ic


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

    window: curses.window = field(init=True, default=None)
    simbol: str = ''
    lin: int = field(default=15)
    col: int = field(default=10)

    def __post_init__(self):
        """Post init."""
        logging.debug(ic(self))

    def new_position(self):
        """New position."""
        heigth, width = self.window.getmaxyx()
        self.lin = min(max(secrets.randbelow(heigth), 1), heigth - 2)
        self.col = min(max(secrets.randbelow(width), 1), width - 2)
        return self

    def draw(self) -> None:
        """Draw it."""
        logging.debug(ic())
        self.window.addch(self.lin, self.col, self.simbol)


@dataclass
class Snake:
    """Snake class."""

    window: curses.window
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

    def __iter__(self):
        """Iteration."""
        for value in self.segments:
            yield from value

    def move(self, direction: int, *, ate_fruit: bool = False) -> None:
        """Move snake."""
        logging.debug(ic())
        head = copy(self.segments[0])
        move_actor(head, direction)
        self.segments.insert(0, head)
        if not ate_fruit:
            self.segments.pop()

    def draw(self) -> None:
        """Draw snake."""
        logging.debug(ic())
        head = self.segments[0]
        self.window.addch(head.lin, head.col, self.symbol_head)
        for body in self.segments[1:]:
            self.window.addch(body.lin, body.col, self.symbol_body)

    def check_hit_border(self) -> bool:
        """Check if hit border."""
        logging.debug(ic())
        return check_actor_hit_border(
            actor=self.segments[0],
            window=self.window,
        )

    def check_hit_itself(self) -> bool:
        """Check if hit itself."""
        logging.debug(ic())
        head = self.segments[0]
        ic(head)
        return


def draw_screen(window: curses.window) -> None:
    """Desenhar tela."""
    window.clear()
    window.border(0)


def draw_actor(actor: Personagem, window: curses.window) -> None:
    """Desenha ator."""
    window.addch(actor.lin, actor.col, actor.simbol)


def get_new_direction(
    window: curses.window,
    current_direction: int,
    timeout: int = 1000,
) -> int | None:
    """Checa nova direção."""
    opposites = {
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT,
    }

    window.timeout(timeout)
    direction = window.getch()
    if (direction in opposites) and (
        current_direction != opposites.get(direction)
    ):
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


def snake_hit_fruit(snake: Snake, fruit: Fruit) -> bool:
    """Snake hit fruit.

    Args:
        snake (_type_): _description_
        fruit (_type_): _description_
    """
    return [fruit.lin, fruit.col] in [[s.lin, s.col] for s in snake.segments]


def finish_game(score: int, window: curses.window, msg: str = '') -> None:
    """Finish game."""
    heigth, width = window.getmaxyx()
    msg = msg or f'Fim de Jogo: Você perdeu! Coletou {score} frutas!!'
    window.clear()
    window.addstr(heigth // 2, (width - len(msg)) // 2, msg)
    window.refresh()
    time.sleep(2)


def game_run(window: curses.window, speed: int = 1000) -> None:
    """Game loop."""
    curses.curs_set(0)
    snake = Snake(window=window)
    current_direction = curses.KEY_DOWN
    fruit = Fruit(window=window, simbol=curses.ACS_DIAMOND)
    snake_ate_fruit = False
    score = 0

    while True:
        draw_screen(window)
        snake.draw()
        fruit.draw()
        if not (
            direction := get_new_direction(
                window=window,
                current_direction=current_direction,
                timeout=speed,
            )
        ):
            direction = current_direction
        snake.move(direction=direction, ate_fruit=snake_ate_fruit)
        if snake.check_hit_border():
            break
        if snake_hit_fruit(snake=snake, fruit=fruit):
            snake_ate_fruit = True
            fruit.new_position().draw()
            score += 1
        else:
            snake_ate_fruit = False

        current_direction = direction
    finish_game(score=score, window=window)


def clear():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605


def select_difficulty():
    """Difficulty game."""
    speeds = {
        '1': 1000,
        '2': 500,
        '3': 150,
        '4': 90,
        '5': 35,
    }
    clear()
    while 1:
        op = input('Selecione a dificuldade entre 1 e 5: ')
        if op in speeds:
            break
    return speeds.get(op)


def run():
    """Run it."""
    curses.wrapper(game_run, speed=select_difficulty())


if __name__ == '__main__':
    run()
