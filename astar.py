from heapq import heappop, heappush, heapify
from board import Board

class Node:
    def __init__(self, board, player, parent=None, column_played=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.column_played = column_played
        self.score = 0

    def __lt__(self, node):
        return self.score < node.score 

#TODO: Criar class A* com os respetivos métodos e ajustar código
class astar:
    def astar(board):
        successors = board.get_successors()

        frontier = []
        for suc in successors:
           heappush(frontier, suc)

        best = heappop(frontier)
        return best.last_move

    def segment_has_both(self,segment):
        player2_count = 0
        player1_count = 0
        for i in segment:
            if i == self.PLAYER2:
                player2_count += 1
            if i == self.PLAYER1:
                player1_count += 1

        return player2_count != 0 and player1_count != 0

#TODO: os pontos tem de ser vistos em todas as direçẽos, e independentemente da 1 jogada a bola tem de ir para cima

    def evaluate_segment(self, segment):
        if self.check_winner(self.PLAYER1):
            return 512 
        if self.check_winner(self.PLAYER2):
            return -512 

        if self.segment_has_both(segment) or segment.count(self.turn) == 0:
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
        
    #TODO: Checkar se o evaluete esta mesmo bem
    def evaluate(self):
        total_score = 0

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
        return total_score
    
        
    
    


