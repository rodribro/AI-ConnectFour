import random
import math
import time
import copy
from board import *

class MCTSNode:
    def __init__(self, board, last = None,parent=None):
        self.state: Board = board
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.last = last

    def __str__(self):
        return f"Visits: {self.visits}, Wins: {self.wins}, Column:{self.last+1}"

    def is_fully_expanded(self):
        _, legal = self.state.successors()
        return len(legal) == len(self.children)
    
    def is_leaf(self):
        if (len(self.children) == 0):
            return True
        else:
            return False

    def select_child(self):
        max_ucb1 = float('-inf')
        selected_child = None
        for child in self.children:
            if child.visits == 0:
                return child
            ucb1 = (child.wins / child.visits) + 1.41 * math.sqrt((math.log(self.visits)*2) / child.visits)
            if ucb1 > max_ucb1:
                max_ucb1 = ucb1
                selected_child = child
        return selected_child

#TODO: Expandir individual 
    def expand(self):
        # Identifica as jogadas possíveis que ainda não foram exploradas
        unexplored_moves = [col for col in range(self.state.cols) if self.state.valid_col(col) and all(col != child.last for child in self.children)]
        
        if unexplored_moves:
            # Escolhe uma jogada não explorada aleatoriamente para a expansão
            move = random.choice(unexplored_moves)
            #print(move)
            #print(unexplored_moves)
            
            #print(unexplored_moves)

            new_board = copy.deepcopy(self.state)
            new_board.drop_piece_adversarial(move)
            new_board.change_turn()
            #new_board.print_board()
            new_node = MCTSNode(new_board, move, parent=self)
            self.children.append(new_node)
            return new_node
        return None


    def simulate(self):
        sim_state = self.state.copy()
        while not sim_state.game_over and not sim_state.is_full():
            #print("AHHHHH")
            _, possible_moves = sim_state.successors()
            sim_state.drop_piece_adversarial(random.choice(possible_moves))
            if sim_state.game_over:
                break
            sim_state.change_turn()
        return sim_state.game_over
    
    
    def backpropagate(self, result):
        self.visits += 1
        if result == self.state.turn:
            self.wins += 0
        elif result == self.state.get_opponent():
            self.wins += 1
        if self.parent:
            self.parent.backpropagate(result)


def mcts(board, timeout=10, iterations = 5000):
    start_time = time.time()
    root = MCTSNode(board)
    for i in range(7):
        root.expand()
    while iterations>0:
        node = root
        while not node.is_leaf():
            if node.is_fully_expanded():
                node = node.select_child()
            else: 
                node = node.expand()
                

        if node.is_leaf():
                node = node.expand()
                
        if node is not None:    
            result = node.simulate()
            node.backpropagate(result)
        iterations-=1
    best_child = max(root.children, key=lambda child: child.wins / child.visits)
    print("--------------------------------------")
    print(best_child)
    for child in root.children:
            if child.visits > 0:
                ratio = child.wins / child.visits
                print(ratio)
                print(child.last + 1)
    
    return best_child.last