import random
import math
import time
from board import *

class MCTSNode:
    def __init__(self, board, last = None ,parent=None):
        self.state = board
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.last = last

    def __str__(self):
        return f"Visits: {self.visits}, Wins: {self.wins}, Column:{self.last}"

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
        legal_moves, possible_moves = self.state.successors()
        random.shuffle(legal_moves)
        for move, last in zip(legal_moves, possible_moves):
            new_node = MCTSNode(move, last, parent=self)
            self.children.append(new_node)
            #print(new_node)
        return self.select_child()


#TODO: simulate nao para na lista vazia
    def simulate(self):
        sim_state = self.state.copy()
        while not sim_state.check_winner(self.state.turn) and not sim_state.is_full():
            #print("AHHHHH")
            _, possible_moves = sim_state.successors()
            #print(possible_moves)
            sim_state.drop_piece_adversarial(random.choice(possible_moves))
        return sim_state.game_over


    def backpropagate(self, result):
        self.visits += 1
        if result == 'X':
            self.wins += 1
        elif result == 'O':
            self.wins += 0
        if self.parent:
            self.parent.backpropagate(result)


def mcts(board, timeout=5):
    start_time = time.time()
    root = MCTSNode(board)
    root.expand()
    while time.time() - start_time < timeout:
        node = root
        while node.children:
            if node.is_fully_expanded():
                node = node.select_child()                
                break
        if not node.is_fully_expanded():
            node = node.expand()
        result = node.simulate()
        node.backpropagate(result)
    best_child = max(root.children, key=lambda child: child.wins / child.visits)
    print("--------------------------------------")
    print(best_child)
    for child in root.children:
            if child.visits > 0:
                ratio = child.wins / child.visits
                print(ratio)
    return best_child.last