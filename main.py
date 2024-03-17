from astar import *
from board import *
from game import *



def playerVSastar():
    rows = 6
    cols = 7
    next_player = 'X'  # Human player
    board = Board(rows, cols, next_player)

    while not board.is_full():
        # Human player's turn
        board.print_board()
        human_col = int(input("Enter column to place your piece (0-6): "))
        while not board.drop_piece(human_col, board.PLAYER1):
            print("Invalid move! Try again.")
            human_col = int(input("Enter column to place your piece (0-6): "))

        if board.check_winner(board.PLAYER1):
            print("Congratulations! You win!")
            break

        # AI player's turn
        ai_node = astar(board, board.PLAYER2)
        ai_col = None
        if ai_node:
            ai_col = find_move(ai_node)
            board.drop_piece(ai_col, board.PLAYER2)

        if board.check_winner(board.PLAYER2):
            print("AI wins!")
            break

    if board.is_full() and not board.check_winner(board.PLAYER1) and not board.check_winner(board.PLAYER2):
        print("It's a draw!")

if __name__ == "__main__":
    playerVSastar()