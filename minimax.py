from board import Board
import math

class Node:
    def __init__(self, board: Board, player, parent=None, column_played=None):
        self.board:Board = board
        self.player = player
        self.parent = parent
        self.column_played = column_played
        self.score = 0

    def __lt__(self, node):
        return self.score < node.score 

def minimax_pruns(node:Node, depth, alpha, beta, maximizing_player=True):
    if depth == 0 or node.board.game_over:
        return node.score

    if maximizing_player:
        max_eval = -math.inf
        for child_node in node.board.get_successors():
            eval = minimax_pruns(Node(child_node, node.board.turn), depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child_node in node.board.get_successors():
            eval = minimax_pruns(Node(child_node, node.board.turn), depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

    
def minimax(board, depth):
    legal_moves = board.get_legal_moves()
    best_move = None
    max_eval = -math.inf
    for move in legal_moves:
        new_board = board.copy()
        new_board.drop_piece(move)
        new_node = Node(new_board, board.turn)
        eval = minimax_pruns(new_node, depth - 1, -math.inf, math.inf, False) 
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move
