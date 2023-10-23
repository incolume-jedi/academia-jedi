import logging
from typing import Optional

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

logging.debug(board)


def show_board():
    print('    0    1    2')
    for index, row in enumerate(board):
        print(index, row)


def move_game(
    board: list,
    gamer: str,
    row: int,
    col: int,
    options: Optional[list] = None,
):
    options = options or ['X', 'O']
    gamer = gamer.upper()
    if gamer not in options:
        msg = 'Invalid Gamer.'
        raise ValueError(msg)
    if board[row][col] in options:
        msg = 'Field ocupade.'
        raise OverflowError(msg)
    board[row][col] = gamer
    show_board()
    logging.debug(check_winner(board))
    return board


def check_winner(board: list, options=None):
    options, winner = options or ['X', 'O'], None
    rows, cols = len(board), len(board[0])

    def element_pos(option):
        return (
            [board[x][y] == option for x in range(rows) for y in range(cols)]
            + [board[y][x] == option for x in range(rows) for y in range(cols)]
            + [board[x][x] == option for x in range(len(board))]
            + [
                board[len(board) - 1 - x][x] == option
                for x in range(len(board))
            ]
        )

    def check_values(pos: list):
        for x in range(3, len(pos) + 1, 3):
            if all(pos[x - 3: x]):
                return True
        return None

    def get_winner(xpos: list, opos: list):
        winner = ''
        if check_values(xpos):
            winner = 'X'
        elif check_values(opos):
            winner = 'O'

        return winner or None

    xpos = element_pos(options[0])
    opos = element_pos(options[1])
    winner = get_winner(xpos, opos)
    return f"{winner}'s Wins"


def run():
    show_board()
    move_game(board, 'x', 1, 1)
    move_game(board, 'o', 0, 1)
    move_game(board, 'x', 0, 0)
    move_game(board, 'o', 2, 2)
    move_game(board, 'x', 2, 0)
    move_game(board, 'o', 0, 2)
    move_game(board, 'x', 1, 0)
    print(check_winner(board))


if __name__ == '__main__':  # pragma: no cover
    run()
