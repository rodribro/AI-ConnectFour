import random
from board import *
from astar import *



board = Board(6,7,'X')

for i in range(10):
    board.drop_piece_search(random.randint(0,6))


print(board)
print(astar(board))

