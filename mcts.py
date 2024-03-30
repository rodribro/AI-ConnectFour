import random
import math
import time
from board import *

class MCTSNode:
    # mudar o state para board
    def __init__(self, board, parent=None):
        self.state = board
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self):
        return len(self.state.get_legal_moves()) == len(self.children)

    def select_child(self):
        max_ucb1 = float('-inf')
        selected_child = None
        for child in self.children:
            if child.visits == 0:
                return child
            ucb1 = (child.wins / child.visits) + 1.41 * math.sqrt(math.log(self.visits) / child.visits)
            if ucb1 > max_ucb1:
                max_ucb1 = ucb1
                selected_child = child
        return selected_child

    def expand(self):
        legal_moves = self.state.get_legal_moves()
        random.shuffle(legal_moves)
        for move in legal_moves:
            child_state = self.state.copy()
            child_state.drop_piece_adversarial(move) #mudar drop piece para ficar so para o mcts
            new_node = MCTSNode(child_state, parent=self)
            self.children.append(new_node)
        return self.select_child()

    def simulate(self):
        sim_state = self.state.copy()
        while not sim_state.game_over:
            legal_moves = sim_state.get_legal_moves()
            sim_state.drop_piece_adversarial(random.choice(legal_moves))
        return sim_state.game_over

    def backpropagate(self, result):
        self.visits += 1
        if result == 'X':
            self.wins += 1
        elif result == 'O':
            self.wins -= 1
        if self.parent:
            self.parent.backpropagate(result)

def mcts(board, timeout=2):
    start_time = time.time()
    root = MCTSNode(board)
    while time.time() - start_time < timeout:
        node = root
        while not node.state.game_over:
            if not node.is_fully_expanded():
                node = node.expand()
                break
            else:
                node = node.select_child()
        result = node.simulate()
        node.backpropagate(result)
    best_child = max(root.children, key=lambda child: child.wins / child.visits)
    return best_child.state.last_move
