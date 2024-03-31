from board import Board
from game import algvsalg, play_game
from minimax import minimax
from mcts import mcts
from astar import astar

def display_menu():
    print("Which algorithm do you want to play against?")
    print("1 - A* Algorithm")
    print("2 - Monte Carlo Tree Search (MCTS)")
    print("3 - Minimax with Alpha-Beta Pruning")
    print("4 - Alg vs Alg")

def display_alg_vs_alg_menu(time):
    print("Which algorithm do you want to be player " + str(time) + "?")
    print("1 - A* Algorithm")
    print("2 - Monte Carlo Tree Search (MCTS)")
    print("3 - Minimax with Alpha-Beta Pruning")

def get_algorithm_choice():
    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ['1', '2', '3','4']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

if __name__ == '__main__':
    rows = 6
    cols = 7
    first_player = 'X'
    algs = ['astar', 'mcts', 'minimax']
    display_menu()
    algorithm_choice = get_algorithm_choice()

    if algorithm_choice == '1':
        play_game(Board(rows, cols, first_player), algorithm="astar")
    elif algorithm_choice == '2':
        play_game(Board(rows, cols, first_player), algorithm="mcts")
    elif algorithm_choice == '3':
        play_game(Board(rows, cols, first_player), algorithm="minimax")
    elif algorithm_choice == '4':
        display_alg_vs_alg_menu(1)
        first_algorithm_choice = get_algorithm_choice()
        display_alg_vs_alg_menu(2)
        second_algorithm_choice = get_algorithm_choice()
        algvsalg(algs[int(first_algorithm_choice) - 1], algs[int(second_algorithm_choice) - 1])
    else:
        pass

