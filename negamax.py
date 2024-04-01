from board import Board

def negamax_alg(board, depth, player, alpha, beta):
    if depth == 0 or board.game_over:
        return board.evaluate() * (-1 if player == board.PLAYER2 else 1), None

    max_score = -float('inf')
    best_move = None

    for move in board.get_legal_moves():
        new_board = board.copy()
        new_board.drop_piece_search(move)
        score, _ = negamax_alg(new_board, depth - 1, player, -beta, -alpha)
        score = -score

        if score > max_score:
            max_score = score
            best_move = move

        alpha = max(alpha, score)
        if alpha >= beta:
            break

    return max_score, best_move

def negamax(board, depth):
    _, best_move = negamax_alg(board, depth, board.turn, -float('inf'), float('inf'))
    return best_move