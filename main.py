from board import Board
from game import play_game


if __name__ == '__main__':
  rows = 6
  cols = 7
  first_player = 'X'

  play_game(Board(rows,cols, first_player), algorithm="astar")