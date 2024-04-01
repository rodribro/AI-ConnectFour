# module with alpha-beta pruning
import random
from time import time
from board import *

PRINT_BEST = True
PRINT_ALL = True

MAX_DEPTH = 3
MAX_DEPTH = 5


def minimax_pruns(board, depth, player, alpha=float("-inf"), beta=float("+inf")):
    nodes_generated = 0

    if board.check_winner(board.turn) or depth == 0:
        return (board.score, None), nodes_generated + 1

    if player:
        max_scores = [(float('-inf'), None)]
        successors, cols = board.get_successors()

        for i in range(len(successors)):
            t, nodes = minimax_pruns(successors[i], depth - 1, False, alpha, beta)
            score, _ = t
            alpha = max(alpha, score)
            if beta <= alpha:
                #break
                pass
            nodes_generated += nodes
            if PRINT_ALL:
                if depth == MAX_DEPTH:
                    print("Col: " + str(cols[i]) + " Score: " + str(score))
            if score > max_scores[0][0]:
                max_scores.clear()
                max_scores.append((score, cols[i]))
            elif score == max_scores[0][0]:
                max_scores.append((score, cols[i]))
            

        return random.choice(max_scores), nodes_generated
    else:
        min_scores = [(float('inf'), None)]
        successors, cols = board.get_successors()
        for i in range(len(successors)):
            t, nodes = minimax_pruns(successors[i], depth - 1, True, alpha, beta)
            nodes_generated += nodes
            score, _ = t
            beta = min(beta, score)
            if beta <= alpha:
                #break
                pass
            if PRINT_ALL:
                if depth == MAX_DEPTH:
                    print("Col: " + str(cols[i]) + " Score: " + str(score))
            if score < min_scores[0][0]:
                min_scores.clear()
                min_scores.append((score, cols[i]))
            elif score == min_scores[0][0]:
                min_scores.append((score, cols[i]))
        return random.choice(min_scores), nodes_generated


def minimax(board):
    ti = time()
    if board.turn == 'X':
        t, nodes_generated = minimax_pruns(board, MAX_DEPTH, True)
        score, col = t
    else:
        t, nodes_generated = minimax_pruns(board, MAX_DEPTH, False)
        score, col = t
    tf = time()
    if PRINT_BEST:
        print("Best column: " + str(col + 1))
        print("Best score: " + str(score))
        print("Time: " + str(round(tf - ti, 5)) + "s")
        print("Nodes generated: " + str(nodes_generated) + "\n")
    return col