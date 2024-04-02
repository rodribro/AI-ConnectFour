# module with alpha-beta pruning
import random
from time import time
from board import *

PRINT_BEST = True
PRINT_ALL = False

MAX_DEPTH = 5



def minimax_pruns(board, depth, player, alpha=float("-inf"), beta=float("+inf")):
    nodes_generated = 0

    if board.check_winner(board.turn) or depth == 0:
        return (board.score, board.last_move), nodes_generated + 1

    if player:
        max_scores = [(float('-inf'), None)]
        successors, cols = board.get_successors()

        for i in range(len(successors)):
            t, nodes = minimax_pruns(successors[i], depth - 1, False, alpha, beta)
            score, _ = t
            if PRINT_ALL:
                if depth == MAX_DEPTH:
                    print(str(depth) + "Col: " + str(cols[i]) + " Score: " + str(score) + " " + str(beta))
            
            if max_scores[0][0] == float('-inf'):
                max_scores.clear()
                max_scores.append((score, cols[i]))
            elif score > max_scores[0][0]:
                max_scores.clear()
                max_scores.append((score, cols[i]))
            elif score == max_scores[0][0]:
                max_scores.append((score, cols[i]))
            if score > beta:
                break
                
            alpha = max(alpha, score)

            nodes_generated += nodes
            

        return random.choice(max_scores), nodes_generated
    else:
        min_scores = [(float('inf'), None)]
        successors, cols = board.get_successors()
        for i in range(len(successors)):
            t, nodes = minimax_pruns(successors[i], depth - 1, True, alpha, beta)
            nodes_generated += nodes
            score, _ = t

            if min_scores[0][0] == float('inf'):
                min_scores.clear()
                min_scores.append((score, cols[i]))
            elif score < min_scores[0][0]:
                min_scores.clear()
                min_scores.append((score, cols[i]))
            elif score == min_scores[0][0]:
                min_scores.append((score, cols[i]))

            if PRINT_ALL:
                if depth == MAX_DEPTH:
                    print(str(depth)+ "Col: " + str(cols[i]) + " Score: " + str(score)+ " " + str(alpha))
            if score < alpha:
                break
                
            beta = min(beta, score)
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
        print("Best score: " + str(score))
        print("Best column: " + str(col + 1))
        print("Time: " + str(round(tf - ti, 5)) + "s")
        print("Nodes generated: " + str(nodes_generated) + "\n")
    return col