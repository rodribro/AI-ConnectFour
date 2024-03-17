import heapq
from board import *

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def generate_successors(board, player):
    successors = []
    for col in range(board.cols):
        if board.drop_piece(col, player):
            successors.append(board)
            # Undo the move for next iteration
            board = Board(board.rows, board.cols, board.next_player)
    return successors

def astar(initial_state, player):
    open_list = []
    closed_set = set()

    initial_node = Node(initial_state, None, 0, initial_state.evaluate(player))
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state.check_winner(player):
            return current_node

        closed_set.add(current_node.state)

        successors = generate_successors(current_node.state, player)
        for successor in successors:

            if successor not in closed_set:
                successor_node = Node(successor, current_node, current_node.cost + 1, successor.evaluate(player))
                heapq.heappush(open_list, successor_node)

    return None