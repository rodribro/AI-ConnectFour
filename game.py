from astar import *
from mcts import *
from board import *
from minimax import *

def play_game(board: Board, algorithm=None):
    while True:
        board.print_board()

        if board.game_over:
            board.change_turn()
            print(f"Player {board.turn} wins!")
            break

        column = input(f"Player {board.turn}, enter the column number (1-{board.cols}): ")

        if not (column.isdigit() and  0 <= int(column)-1 < board.cols ):
            print("Invalid column! Please choose a column within the board range.")
            continue
        
        column = int(column) - 1
        if algorithm is None:
            board.drop_piece_search(column)
        else:
            if algorithm == "astar" or algorithm == "minimax":
                board.drop_piece_search(column)
            elif algorithm == "mcts":
                board.drop_piece_adversarial(column)
                board.change_turn()

        if board.game_over:
            board.print_board()
            board.change_turn()
            print(f"Player {board.turn} wins!")
            break
        
        #use isfull
        if all(board.grid[0][col] != '-' for col in range(board.cols)):
            board.print_board()
            print("It's a draw!")
            break

        if algorithm is not None:
            if algorithm == "astar":
                board.drop_piece_search(astar(board))
            elif algorithm == "mcts":
                board.drop_piece_adversarial(mcts(board))
                board.change_turn()
            elif algorithm == "minimax":
                board.drop_piece_search(minimax(board))
            else:
                pass


def algvsalg(alg1, alg2):
    board = Board(6, 7, 'X')
    begginning = True
    while True:
        if board.game_over:
            board.print_board()
            winner = alg1 if board.turn == 'O' else alg2
            print(f"Player {winner} wins!")
            break
        if alg1 in ['astar', 'minimax']:
            if alg1 == 'astar':
                if begginning:
                    board.drop_piece_search(random.choice(range(board.cols)))
                board.drop_piece_search(astar(board))
            if alg1 == 'minimax':
                board.drop_piece_search(minimax(board))
            begginning = False
        else:
            board.drop_piece_adversarial(mcts(board))
        board.print_board()

        if board.game_over:
            board.print_board()
            board.change_turn()
            winner = alg1 if board.turn == 'O' else alg2
            print(f"Player {winner} wins!")
            break

        if all(board.grid[0][col] != '-' for col in range(board.cols)):
            board.print_board()
            print("It's a draw!")
            break
        
        if alg2 in ['astar', 'minimax']:
            if alg2 == 'astar':
                board.drop_piece_search(astar(board))
            if alg2 == 'minimax':
                board.drop_piece_search(minimax(board))
        else:
            board.drop_piece_adversarial(mcts(board))
        board.print_board()
        
        
