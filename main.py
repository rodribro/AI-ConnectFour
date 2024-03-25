from board import Board
from game import play_game

def display_menu():
    print("Which algorithm do you want to play against?")
    print("1 - A* Algorithm")
    print("2 - Monte Carlo Tree Search (MCTS)")

def get_algorithm_choice():
    while True:
        choice = input("Enter your choice (1/2): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    rows = 6
    cols = 7
    first_player = 'X'

    display_menu()
    algorithm_choice = get_algorithm_choice()

    if algorithm_choice == '1':
        play_game(Board(rows, cols, first_player), algorithm="astar")
    elif algorithm_choice == '2':
        play_game(Board(rows, cols, first_player), algorithm="mcts")
