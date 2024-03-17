import math
import queue
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
        #Não podíamos implementar um counter e uma condição para evitar
        #verificar se alguém já ganhou até ser efetivamente possível ganhar?
        #Como só dá para ganhar a partir de x move
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

def A_Star(initialBoard, heuristic):

    #queue onde vamos guardando os nós pela ordem que
    #devem ser expandidos, expandimos os que apresentarem
    #o menor custo
    boardQueue = queue.PriorityQueue(maxsize=0)
    
    #Structure to keep track of path, dictionary
    #keys represent the current node?
    #values represent the previous node?
    cameFrom = {} 

    #Cost of the path from start node
    #to current node, g(currentboard)
    g = set()
    g[initialBoard] = 0

    #Function to represent current best guess as
    #to which path leads to win
    f = set()
    f[initialBoard] = initialBoard.evaluate(initialBoard, 'O') #Acho que isto não está bem estruturado

    #Heuristica
    heuristic

    #Implementamos aqui a função para gerar filhos?
    def generateChildrenNodes():
        return 0
    
    #while not boardQueue.empty():
        
    
        


