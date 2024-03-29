from heapq import heappop, heappush, heapify
from board import Board

class Node:
    def init(self, board, player, parent=None, column_played=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.column_played = column_played
        self.score = 0

    def lt(self, node):
        return self.score < node.score 

def astar(board):
    successors = board.get_successors()

    frontier = []
    for suc in successors:
       heappush(frontier, suc)

    best = heappop(frontier)
    return best.last_move