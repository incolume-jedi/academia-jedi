import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
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
            if all(pos[x - 3 : x]):
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
