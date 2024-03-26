from astar import *
from mcts import *
from time import sleep
from board import Board

def play_game(board, algorithm=None):
    while True:
        board.print_board()


        if board.game_over:
            print(f"Player {board.game_over} wins!")
            break


        column = int(input(f"Player {board.turn}, enter the column number (1-{board.cols}): ")) - 1

        if not (0 <= column < board.cols):
            print("Invalid column! Please choose a column within the board range.")
            continue
        
        
        board.drop_piece(column)

        if board.game_over:
            print(Board.get_outcome())

        if algorithm is not None:
            #sleep(0.5)
            if algorithm == "astar":
                board.drop_piece(astar(board))
            elif algorithm == "mcts":
                board.drop_piece(mcts(board))
            else:
                pass

        
        
    
    


    
        

