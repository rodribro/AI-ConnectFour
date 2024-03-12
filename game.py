import math
from board import *

rows = 6
cols = 7



def player_vs_player(rows, cols):
    board = Board(6,7)
    player = 'X'

    while True:
        board.print_board()
        column = int(input(f"Player {player}, enter the column number (1-{cols}): ")) - 1

        if not (0 <= column < cols):
            print("Invalid column! Please choose a column within the board range.")
            continue

        board.drop_piece( column, player)
        if board.check_winner( player):
            board.print_board()
            print(f"Player {player} wins!")
            break

        if all(board.grid[0][col] != '-' for col in range(cols)):
            board.print_board()
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'


player_vs_player(6,7)
