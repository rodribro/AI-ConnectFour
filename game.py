import math

rows = 6
cols = 7

def initialize_board(rows, cols):
    return [['-' for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def drop_piece(board, col, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == '-':
            board[row][col] = player
            break

def check_winner(board, player):
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    for row in range(len(board) - 3):
        for col in range(len(board[0])):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + 3 - i][col + i] == player for i in range(4)):
                return True

    return False

def player_vs_player(rows, cols):
    board = initialize_board(rows, cols)
    player = 'X'

    while True:
        print_board(board)
        column = int(input(f"Player {player}, enter the column number (1-{cols}): ")) - 1

        if not (0 <= column < cols):
            print("Invalid column! Please choose a column within the board range.")
            continue

        drop_piece(board, column, player)
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if all(board[0][col] != '-' for col in range(cols)):
            print_board(board)
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'



def evaluate_segment(segment, player):
    if segment.count(player) == 3 :
        return 50
    elif segment.count(player) == 2 :
        return 10
    elif segment.count(player) == 1 :
        return 1
    elif segment.count(player) == 0 :
        return 0
    elif segment.count(player) == 1 :
        return -1
    elif segment.count(player) == 2 :
        return -10
    elif segment.count(player) == 3 :
        return -50
    else:
        return 0

def evaluate_board(board, player):
    total_score = 0

    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            segment = board[row][col:col+4]
            total_score += evaluate_segment(segment, player)

    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            segment = [board[row+i][col] for i in range(4)]
            total_score += evaluate_segment(segment, player)

    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            segment = [board[row+i][col+i] for i in range(4)]
            total_score += evaluate_segment(segment, player)

    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            segment = [board[row+3-i][col+i] for i in range(4)]
            total_score += evaluate_segment(segment, player)

    return total_score

player_vs_player(6,7)

