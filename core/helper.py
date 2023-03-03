from tic_tac_toe.core.matrix_definition import matrix_position


def get_row_col(pos):
    return matrix_position[pos]


def current_board(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def is_row_winner(board):
    is_found = False
    for row in board:
        if row.count("X") == len(row) or row.count("O") == len(row):
            is_found = True
    return is_found


def is_col_winner(board):
    is_found = False
    first = [board[0][0], board[1][0], board[2][0]]
    second = [board[0][1], board[1][1], board[2][1]]
    third = [board[0][2], board[1][2], board[2][2]]
    if first.count("X") == len(board) or first.count("O") == len(board):
        is_found = True
    elif second.count("X") == len(board) or second.count("O") == len(board):
        is_found = True
    elif third.count("X") == len(board) or third.count("O") == len(board):
        is_found = True
    return is_found


def is_diagonal_win(board):
    is_found = False
    left_diagonal = [board[0][0], board[1][1], board[2][2]]
    right_diagonal = [board[0][2], board[1][1], board[2][0]]
    if left_diagonal.count("X") == len(board) or left_diagonal.count("O") == len(board):
        is_found = True
    elif right_diagonal.count("X") == len(board) or right_diagonal.count("O") == len(board):
        is_found = True
    return is_found


def is_winner(board):
    if is_row_winner(board):
        return True
    elif is_col_winner(board):
        return True
    elif is_diagonal_win(board):
        return True
    return False


def is_board_full(board):
    is_full = True
    for row in board:
        if " " in row:
            is_full = False
    return is_full
