import math

class GameMeta:
    PLAYERS = {'none': 0, 'X': 1, 'O': 2}
    OUTCOMES = {'none': 0, 'X': 1, 'O': 2, 'draw': 3}
    INF = float('inf')
    ROWS = 6
    COLS = 7


class MCTSMeta:
    EXPLORATION = math.sqrt(2)
