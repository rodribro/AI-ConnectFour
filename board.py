
class Board:
    def __init__(self, rows, cols, turn):
        self.rows = rows
        self.cols = cols
        self.PLAYER1 = 'X'
        self.PLAYER2 = 'O'
        self.score = 0
        self.game_over = False
        self.grid = [['-' for _ in range(cols)] for _ in range(rows)]
        self.turn = turn
        self.last_move = None
        
    def __lt__(self, board):
            return self.score < board.score 

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
            
    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

    def drop_piece(self, col, heuristic=None):
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == '-':
                self.grid[row][col] = self.turn
                self.change_turn()
                self.last_move = col
                if heuristic is not None:
                    self.score = heuristic()  
                else:
                    self.score = self.evaluate()  
                return True
        return False           
    
                             

    
    def copy(self):
        new_grid = [[item for item in row] for row in self.grid]  
        new_board = Board(self.rows, self.cols, self.turn)
        new_board.grid = new_grid
        return new_board
    
    def __str__(self):

        board_string = ""
        for row in self.grid:
            board_string += "".join(row) + "\n"  
        return board_string.rstrip() 
    
    def get_legal_moves(self):
        legal_moves = []
        for col in range(self.cols):
            if self.grid[self.rows - 1][col] == '-':
                legal_moves.append(col)
        return legal_moves


    def is_full(self):
        return all(self.grid[0][col] != '-' for col in range(self.cols))

    def get_segment(self, start_row, start_col, d_row, d_col):
        segment = []
        for i in range(4):
            row = start_row + i * d_row
            col = start_col + i * d_col
            segment.append(self.grid[row][col])
        return segment
    
    def check_winner(self, player):
      for row in range(len(self.grid)):
          for col in range(len(self.grid[0]) - 3):
              if all(self.grid[row][col + i] == player for i in range(4)):
                  self.game_over= player
                  return True

      for row in range(len(self.grid) - 3):
          for col in range(len(self.grid[0])):
              if all(self.grid[row + i][col] == player for i in range(4)):
                self.game_over= player
                return True

      for row in range(len(self.grid) - 3):
          for col in range(len(self.grid[0]) - 3):
              if all(self.grid[row + i][col + i] == player for i in range(4)):
                self.game_over= player
                return True
              if all(self.grid[row + 3 - i][col + i] == player for i in range(4)):
                  self.game_over= player
                  return True

      return False
    
    def get_successors(self):
        successors = []
        for i in range(self.cols):
            suc = self.copy()
            if suc.drop_piece(i):
                successors.append(suc)
        return successors
    

