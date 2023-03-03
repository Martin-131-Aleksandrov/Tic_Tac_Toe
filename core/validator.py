
from tic_tac_toe.core.helper import get_row_col


def is_position_in_range(pos):
    if 1 <= pos <= 9:
        return True
    else:
        return False


def is_place_available(board, pos):
    rows, col = get_row_col(pos)
    if not board[rows][col] == " ":
        return False
    else:
        return True
