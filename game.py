from astar import astar
from mcts import mcts
from board import Board
from minimax import minimax

def play_game(board: Board, algorithm=None):
    while True:
        board.print_board()

        if board.game_over:
            print(f"Player {board.game_over} wins!")
            break

        column = int(input(f"Player {board.turn}, enter the column number (1-{board.cols}): ")) - 1

        if not (0 <= column < board.cols):
            print("Invalid column! Please choose a column within the board range.")
            continue

        board.drop_piece(column)  # Drop the piece

        if board.game_over:
            board.print_board()
            print(f"Player {board.game_over} wins!")
            break

        if all(board.grid[0][col] != '-' for col in range(board.cols)):
            board.print_board()
            print("It's a draw!")
            break

        # Switch the turn after each move
        board.change_turn()

        if algorithm is not None:
            if algorithm == "astar":
                column_to_play = astar(board)
            elif algorithm == "mcts":
                column_to_play = mcts(board)
            elif algorithm == "minimax":
                column_to_play = minimax(board, 1)
            else:
                column_to_play = None

            if column_to_play is not None:
                board.drop_piece(column_to_play)

        if board.game_over:
            board.print_board()
            print(f"Player {board.game_over} wins!")
            break

        if all(board.grid[0][col] != '-' for col in range(board.cols)):
            board.print_board()
            print("It's a draw!")
            break

        # Switch the turn again if the game is not over
        board.change_turn()
