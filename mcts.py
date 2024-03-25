import random
import math
import time

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.score = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_successors())

    def is_terminal(self):
        return self.state.game_over or self.state.is_full()


    #TODO: a exploration esta bem?
    def select_child(self, exploration_parameter=math.sqrt(2)):
        if not self.children:
            return None

        best_child = None
        best_score = float('-inf')

        for child in self.children:
            exploitation = child.score / child.visits if child.visits > 0 else 0
            exploration = math.sqrt(math.log(self.visits) / child.visits) if child.visits > 0 else float('inf')
            score = exploitation + exploration_parameter * exploration
            if score > best_score:
                best_score = score
                best_child = child

        return best_child

#TODO: isto tem de estar mal mas pode ser das outras funcoes estou a ganhar em 4 jogadas
def uct_search(root, budget, timeout):
    start_time = time.time()
    iterations = 0
    while time.time() - start_time < timeout and iterations < budget:
        node = select_node(root)

        # Expansion
        if not node.is_terminal():
            expand_node(node)

        # Rollout e Backpropagate
        rollout_node(node)



        iterations += 1

    return select_best_child(root)

# nao sei que merda é o lambda so copiei do gajo
def select_best_child(node):
    return max(node.children, key=lambda n: n.visits)



def select_node(node):
    while node.children:
        node = node.select_child()
    return node


def expand_node(node):
    successors = node.state.get_successors()
    for successor in successors:
        node.children.append(Node(successor, parent=node))

#TODO: o rollout deve estar mal    
def rollout_node(node):
    sim_state = node.state.copy()
    while not sim_state.game_over and not sim_state.is_full():
        successors = sim_state.get_successors()
        random_successor = random.choice(successors)
        sim_state = random_successor.copy()
    score = sim_state.evaluate() if sim_state.game_over else 0
    backpropagate(node, score)

#TODO: Ver se isto esta bem
def backpropagate(node, score):
    current_node = node
    while current_node:
        current_node.visits += 1
        current_node.score += score
        current_node = current_node.parent
        score *= -1  #troca para o outro player nao sei se é assim a melhor forma




def mcts(board, budget=1000, timeout=10):
    root = Node(board)
    best_child = uct_search(root, budget, timeout)
    return best_child.state.last_move
