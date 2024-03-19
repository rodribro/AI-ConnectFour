from astar import *
from time import sleep


def play_game(board, algorithm=None):
    while True:
        board.print_board()


        if board.game_over:
            print(f"Player {board.turn} wins!")
            break


        column = int(input(f"Player {board.turn}, enter the column number (1-{board.cols}): ")) - 1

        if not (0 <= column < board.cols):
            print("Invalid column! Please choose a column within the board range.")
            continue
        
        
        board.drop_piece(column)


        #TODO: Ele esta a passar mais um no next_player entao dá a vitória ao jogador errado
        #TODO: depois do input vencedor ele joga mais uma vez
            
        
        if all(board.grid[0][col] != '-' for col in range(board.cols)):
            board.print_board()
            print("It's a draw!")
            break

        if algorithm is not None:
            #sleep(0.5)
            if algorithm == "astar":
                board.drop_piece(astar(board))
            else:
                pass

        
        
    
    


    
        

