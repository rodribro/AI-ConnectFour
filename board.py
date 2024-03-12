class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.PLAYER1 = 'X'
        self.PLAYER2 = 'O'
        self.grid = [['-' for _ in range(cols)] for _ in range(rows)]

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

    def drop_piece(self, col, player):
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == '-':
                self.grid[row][col] = player
                return True
        return False

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
                  return True

      for row in range(len(self.grid) - 3):
          for col in range(len(self.grid[0])):
              if all(self.grid[row + i][col] == player for i in range(4)):
                  return True

      for row in range(len(self.grid) - 3):
          for col in range(len(self.grid[0]) - 3):
              if all(self.grid[row + i][col + i] == player for i in range(4)):
                  return True
              if all(self.grid[row + 3 - i][col + i] == player for i in range(4)):
                  return True

      return False

    def segment_has_both(self,segment):
        player2_count = 0
        player1_count = 0
        for i in segment:
            if i == self.PLAYER2:
                player2_count += 1
            if i == self.PLAYER1:
                player1_count += 1

        return player2_count != 0 and player1_count != 0

    def evaluate_segment(self, segment, player):
        if self.segment_has_both(segment) or segment.count(player):
            return 0
        if  segment.count(player) == 3 :
            if(player == self.PLAYER1):
                return 50
            else:
                return -50
        if  segment.count(player) == 2 :
            if(player == self.PLAYER1):
                return 10
            else:
                return -10
        if  segment.count(player) == 1 :
            if(player == self.PLAYER1):
                return 1
            else:
                return -1
            
        return 0
        

    def evaluate(self, player):
        total_score = 0

        for row in range(self.rows):
            for col in range(self.cols - 3):
                segment = self.get_segment(row, col, 0, 1)
                total_score += self.evaluate_segment(segment, player)

        for col in range(self.cols):
            for row in range(self.rows - 3):
                segment = self.get_segment(row, col, 1, 0)
                total_score += self.evaluate_segment(segment, player)

        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                segment = self.get_segment(row, col, 1, 1)
                total_score += self.evaluate_segment(segment, player)

        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                segment = self.get_segment(row + 3, col, -1, 1)
                total_score += self.evaluate_segment(segment, player)

        return total_score
        
