from puzzle_state import PuzzleState
from utils import get_user_puzzle, select_algorithm
from search import general_search
    
if __name__ == "__main__":
    puzzle = get_user_puzzle()

    print("\nYour entered puzzle:")
    for row in puzzle:
        print(row)

    # Select the algorithm to use
    heuristic_function = select_algorithm(puzzle)
    
    general_search(PuzzleState(puzzle, None, None, heuristic_function), heuristic_function)
    
