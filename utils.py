from puzzle_state import PuzzleState

def get_user_puzzle():
    print("Welcome to my 8-PuzzleSolver for my CS170 Class Winter 2025")
    print()
    print("Please enter a valid 8-puzzle in the following format:")
    print()
    print("For example:\n1 2 3\n4 5 6\n7 8 0\n")

    puzzle_row_one = list(map(int, input("Enter the first row: ").split()))
    puzzle_row_two = list(map(int, input("Enter the second row: ").split()))
    puzzle_row_three = list(map(int, input("Enter the third row: ").split()))

    user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]

    return user_puzzle

def select_algorithm(puzzle):
    print("\nSelect the algorithm you want to use:")
    print("1. Uniform Cost Search")
    print("2. A* with Misplaced Tile Heuristic")
    print("3. A* with Manhattan Distance Heuristic")
    print()
    algorithm_choice = int(input("Enter your choice (1, 2, or 3): "))
    print()

    if algorithm_choice == 1:
        print("You have selected Uniform Cost Search. Running now...")
        return PuzzleState.uniform_cost
    elif algorithm_choice == 2:
        print("You have selected Misplaced Tile Heuristic. Running now...")
        return PuzzleState.misplaced_tile
    elif algorithm_choice == 3:
        print("You have selected Manhattan Distance Heuristic. Running now...")
        return PuzzleState.manhattan_distance
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return select_algorithm(puzzle)