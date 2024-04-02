
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
        self.algorithm = None
        
    
    
    
    def valid_col(self, col):
        if col < 0 or col >= self.cols:
            return False  # Column out of range
        return '-' in [row[col] for row in self.grid]  # Check if the column has empty slots

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

    def drop_piece_search(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == '-':
                self.grid[row][col] = self.turn
                self.change_turn() 
                self.evaluate()
                
                self.last_move = col
                return True
        return False
    
    def drop_piece_adversarial(self, col):
        for row in range(self.rows -1 , -1 , -1):
            if self.grid[row][col] == '-':
                self.grid[row][col] = self.turn
                self.last_move = col
                self.check_winner(self.turn)
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
            if self.grid[0][col] == '-' :
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
        possible_moves = []

        for i in range(self.cols):
            suc = self.copy()
            if suc.drop_piece_search(i):
                successors.append(suc)
                possible_moves.append(i)
        return successors, possible_moves
    
    def successors(self):
        successors=[]
        possible_moves = []
        for col in range(self.cols):
            suc = self.copy()
            if suc.drop_piece_adversarial(col):
                successors.append(suc)
                possible_moves.append(col)
                suc.change_turn()

        return successors, possible_moves
            
    def get_opponent(self):
        if self.turn == 'X':
            return 'O'
        else:
            return 'X'
        
    def segment_has_both(self,segment):
        player2_count = 0
        player1_count = 0
        for i in segment:
            if i == self.PLAYER2:
                player2_count += 1
            if i == self.PLAYER1:
                player1_count += 1

        return player2_count != 0 and player1_count != 0


    def evaluate_segment(self, segment):
        if self.segment_has_both(segment) or (segment.count(self.PLAYER1) == 0 and segment.count(self.PLAYER2) == 0):
            return 0
        
        if  segment.count(self.turn) == 3 :
            if(self.turn== self.PLAYER1):
                return 50
            else:
                return -50
        if  segment.count(self.turn) == 2 :
            if(self.turn == self.PLAYER1):
                return 10
            else:
                return -10
        if  segment.count(self.turn) == 1 :
            if(self.turn == self.PLAYER1):
                return 1
            else:
                return -1
        return 0
        
    def evaluate(self):
        total_score = 0
        if self.check_winner(self.PLAYER1):
            total_score += 512 
        if self.check_winner(self.PLAYER2):
            total_score += -512

        for row in range(self.rows):
            for col in range(self.cols - 3):
                segment = self.get_segment(row, col, 0, 1)                
                total_score += self.evaluate_segment(segment)

        for col in range(self.cols):
            for row in range(self.rows - 3):
                segment = self.get_segment(row, col, 1, 0)                
                total_score += self.evaluate_segment(segment)

        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                segment = self.get_segment(row, col, 1, 1)
                total_score += self.evaluate_segment(segment)

        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                segment = self.get_segment(row + 3, col, -1, 1)                
                total_score += self.evaluate_segment(segment)

        if self.turn == self.PLAYER1:
            total_score += 16
        else:
            total_score -= 16
        self.score = total_score    
        return self.score
        
    
    