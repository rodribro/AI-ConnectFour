from heapq import heappop, heappush
from board import *

def astar(board, player):
    successors, _ = board.get_successors()

    frontier = []
    for suc in successors:
      if player == 'X':
         suc.score *=-1 #multiplying by -1 
      heappush(frontier, suc)

    best = heappop(frontier)
    return best.last_move