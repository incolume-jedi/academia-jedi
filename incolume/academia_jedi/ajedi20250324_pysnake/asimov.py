"""Asimov solution."""

import curses
import logging
import random
import time

from icecream import ic

# ruff: noqa: T201

ic.disable()


def draw_screen(window: curses.window) -> None:
    """Desenhar tela."""
    window.clear()
    window.border(0)


def draw_actor(actor: list, char: str, window: curses.window) -> None:
    """Desenha ator."""
    window.addch(*actor, char)


def check_actor_hit_border(actor: list, window: curses.window) -> bool:
    """Checa limite tela."""
    heigth, width = window.getmaxyx()
    return ((actor[0] <= 0) or (actor[0] >= heigth - 1)) or (
        (actor[1] <= 0) or (actor[1] >= width - 1)
    )


def check_snake_hit_border(snake, window):
    """Check_snake_hit_border.

    Args:
        snake (list): _description_
        window (_type_, optional): _description_. Defaults to window.
    """
    head = snake[0]
    return check_actor_hit_border(actor=head, window=window)


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


def move_actor(actor: list, direction: int) -> None:
    """Move ator."""
    match direction:
        case curses.KEY_UP:
            logging.debug(ic('MOVE UP'))
            actor[0] -= 1
        case curses.KEY_DOWN:
            logging.debug(ic('MOVE DOWN'))
            actor[0] += 1
        case curses.KEY_LEFT:
            logging.debug(ic('MOVE LEFT'))
            actor[1] -= 1
        case curses.KEY_RIGHT:
            logging.debug(ic('MOVE RIGHT'))
            actor[1] += 1


def move_snake(
    snake: list,
    direction: int,
    *,
    snake_ate_fruit: bool = False,
) -> None:
    """Move snake."""
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0, head)
    if not snake_ate_fruit:
        snake.pop()


def draw_snake(snake, window):
    """Draw snake.

    Args:
        snake (_type_): _description_
        window (_type_): _description_
    """
    head = snake[0]
    draw_actor(actor=head, window=window, char='@')
    for body in snake[1:]:
        draw_actor(actor=body, window=window, char='§')


def get_new_fruit(window):
    """Get new fruit."""
    heigth, width = window.getmaxyx()
    return [random.randint(1, heigth - 2), random.randint(1, width - 2)]


def snake_hit_fruit(snake, fruit):
    """Snake hit fruit.

    Args:
        snake (_type_): _description_
        fruit (_type_): _description_
    """
    return fruit in snake


def snake_hit_itself(snake: list) -> bool:
    """Snake hit itself."""
    return snake[0] in snake[1:]


def is_direction_opposite(direction: int, current_direction: int) -> bool:
    """Check direction."""
    match direction:
        case curses.KEY_UP:
            logging.debug(ic('MOVE UP'))
            return current_direction == curses.KEY_DOWN
        case curses.KEY_DOWN:
            logging.debug(ic('MOVE DOWN'))
            return current_direction == curses.KEY_UP
        case curses.KEY_LEFT:
            logging.debug(ic('MOVE LEFT'))
            return current_direction == curses.KEY_RIGHT
        case curses.KEY_RIGHT:
            logging.debug(ic('MOVE RIGHT'))
            return current_direction == curses.KEY_LEFT


def game_loop(window):
    """Run game.

    Args:
        window (_type_): _description_
    """
    curses.curs_set(0)
    snake: list = [
        [10, 15],
        [9, 15],
        [8, 15],
        [7, 15],
    ]
    current_direction: int = curses.KEY_DOWN
    fruit = get_new_fruit(window=window)
    snake_ate_fruit = False
    score = 0

    while True:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit, window=window, char=curses.ACS_DIAMOND)
        if (
            direction := get_new_direction(window=window)
        ) is None or is_direction_opposite(direction, current_direction):
            direction = current_direction

        move_snake(
            snake=snake,
            direction=direction,
            snake_ate_fruit=snake_ate_fruit,
        )
        if check_snake_hit_border(
            snake=snake,
            window=window,
        ) or snake_hit_itself(snake=snake):
            break
        if snake_hit_fruit(snake=snake, fruit=fruit):
            snake_ate_fruit = True
            fruit = get_new_fruit(window=window)
            score += 1
        else:
            snake_ate_fruit = False
        current_direction = direction
    finish_game(score=score, window=window)


def finish_game(score: int, window: curses.window, msg: str = '') -> None:
    """Finish game."""
    heigth, width = window.getmaxyx()
    msg = msg or f'Fim de Jogo: Você perdeu! Coletou {score} frutas!!'
    window.addstr(heigth // 2, (width - len(msg)) // 2, msg)
    window.refresh()
    time.sleep(2)


def run():
    """Run it."""
    curses.wrapper(game_loop)


if __name__ == '__main__':
    run()
