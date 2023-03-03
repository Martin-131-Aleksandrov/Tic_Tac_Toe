from tic_tac_toe.core.validator import is_position_in_range, is_place_available
from tic_tac_toe.core.helper import get_row_col, current_board, is_winner, is_board_full


def play(players, board, turns):
    current_turn_count = 1

    while True:
        current_player_name = turns[current_turn_count % 2]
        position = int(input(f"{current_player_name},choose a free position(1-9):"))
        if is_position_in_range(position):
            if is_place_available(board, position):
                row, col = get_row_col(position)
                board[row][col] = players[current_player_name]
                current_board(board)
                if is_winner(board):
                    print(f"Congrats {current_player_name}!")
                    exit(0)
                if is_board_full(board):
                    print(
                        "******************\n*The game is tie.*\n******************")
                    exit(0)

        else:
            pass
        current_turn_count += 1
