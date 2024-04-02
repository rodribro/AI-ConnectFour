from board import *
import time

MAX_DEPTH = 5

def negamax_alg(board: Board, depth, player, alpha, beta):
    if depth == 0 or board.game_over:
        return board.evaluate() * (-1 if player == PLAYER2 else 1), None, 1

    max_score = -float('inf')
    best_move = None
    nodes_generated = 0

    for move in board.get_legal_moves():
        new_board = board.copy()
        new_board.drop_piece_search(move)
        if best_move is None:
            best_move = move
        #player nao esta a mudar!!!!
        score, _, generated = negamax_alg(new_board, depth - 1, player, -beta, -alpha)
        score = -score
        nodes_generated += generated

        if score > max_score:
            max_score = score
            best_move = move

        alpha = max(alpha, score)
        if alpha >= beta:
            break

    return max_score, best_move, nodes_generated

def negamax(board):
    start_time = time.time()
    score, best_move, nodes_generated = negamax_alg(board, MAX_DEPTH, board.turn, -float('inf'), float('inf'))
    print("Best column:", best_move +1)
    print("Best score:", score)
    print("Nodes generated:", nodes_generated)
    print("Time:", time.time() - start_time, "seconds")
    return best_move