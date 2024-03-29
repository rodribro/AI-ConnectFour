from astar import *
from mcts import *
from board import *
from minimax import *

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

        if algorithm is None:
            board.drop_piece(column)
        else:
            if algorithm == "astar" or algorithm == "minimax":
                board.drop_piece(column, board.evaluate)
            elif algorithm == "mcts":
                board.drop_piece(column)

        if board.game_over:
            board.print_board()
            print(f"Player {board.game_over} wins!")
            break

        if all(board.grid[0][col] != '-' for col in range(board.cols)):
            board.print_board()
            print("It's a draw!")
            break

        if algorithm is not None:
            if algorithm == "astar":
                board.drop_piece(astar(board), heuristic=board.evaluate)
                
            elif algorithm == "mcts":
                board.drop_piece(mcts(board))
            elif algorithm == "minimax":
                board.drop_piece(minimax(board, 1))
            else:
                pass