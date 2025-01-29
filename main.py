import heapq
import random

GOAL_STATE = [[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 0]]

#finds the postion of the numbers in the goal state to compare in later iterations 
def find_goalstate_position(num):
    for i in range(len(GOAL_STATE)):
        for j in range(len(GOAL_STATE[i])):
            if GOAL_STATE[i][j] == num:
                return i, j
    return -1,-1

#heuristic in uniform cost seach is 0 so this function will only return 0
def uniform_cost(state):
    return 0

#calculates the distance between the current state and the goal state
#If reached goal state then distance = 0
def manhattan_distance(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):  
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:  # Ignore 0 (empty space)
                expected_i, expected_j = find_goalstate_position(state[i][j])
                distance += abs(expected_i - i) + abs(expected_j - j)
    return distance

#counts how many tiles are not in the right positon
#If reached goal state then count = 0
def misplaced_tile(state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]: # Ignore 0 (empty space)
                count += 1
    return count
'''
def general_search(problem, queueing_function):
    nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    loop do
        if EMPTY(nodes):
            return "failure"  # No solution found
        node = REMOVE-FRONT(nodes)  # Remove the first node
        if problem.GOAL-TEST(node.STATE):
            return node  # Return the solution if goal state is found
        nodes = queueing_function(nodes, EXPAND(node, problem.OPERATORS))
'''

def general_search(initial_state, heuristic_function):
    unexplored_nodes = []
    explored_nodes = set()

    #pushes the starting node to the priorty queue
    heapq.heappush(unexplored_nodes,initial_state)
    while len(unexplored_nodes) > 0:
        current_state = heapq.heappop(unexplored_nodes)
        if current_state.is_goal():
            path_trace = []
            while current_state:
                path_trace.append(current_state.board)
                current_state = current_state.parent_state
            path_trace.reverse()
            return path_trace
        if current_state.board in explored_nodes:
            continue
        explored_nodes.add(current_state.board)
        neighbor_states = current_state.get_neighbors()
        
    
#different iterations of the puzzle
class PuzzleState:
    def __init__(self, board, parent_state):
        self.board = board
        self.parent_state = parent_state

    def is_goal(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if GOAL_STATE[i][j] != self.board[i][j]:
                    return False
        return True


    def get_neighbors(self):
        zero_position_row, zero_position_column = -1, -1
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    zero_position_row, zero_position_column = i, j
        #need to finish             
        
# gets user input 
def generate_random_puzzle():
    numbers = list(range(9)) 
    random.shuffle(numbers)  # Shuffle to create a random order

    # Convert the flat list into a 2D list for the puzzle
    return [numbers[:3], numbers[3:6], numbers[6:]]
    
def get_user_puzzle():
    print("Enter 1 to use a default puzzle or enter 2 to create your own")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        # Generate a random default puzzle
        user_puzzle = generate_random_puzzle()
        print("Random default puzzle:")
        for row in user_puzzle:
            print(row[0], row[1], row[2])

    elif choice == "2":
        print("Enter your puzzle, using a zero to represent the blank.")
        print(
            "Please only enter valid 8-puzzles. Enter the numbers separated by spaces."
        )
        print("For example:\n1 2 3\n4 5 6\n7 8 0\n")        

        puzzle_row_one = input("Enter the first row: ").split()
        puzzle_row_two = input("Enter the second row: ").split()
        puzzle_row_three = input("Enter the third row: ").split()

        # Convert each element of the rows to integers using a for loop
        puzzle_row_one_int = []
        puzzle_row_two_int = []
        puzzle_row_three_int = []
        
        for num in puzzle_row_one:
            puzzle_row_one_int.append(int(num))

        for num in puzzle_row_two:
            puzzle_row_two_int.append(int(num))

        for num in puzzle_row_three:
            puzzle_row_three_int.append(int(num))

        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return get_user_puzzle() 
        
    return user_puzzle
    
def select_algorithm(puzzle):
    print("\nSelect the algorithm you want to use:")
    print("1. Uniform Cost Search")
    print("2. A* with Misplaced Tile Heuristic")
    print("3. A* with Manhattan Distance Heuristic")
    input("Enter your choice (1, 2, or 3): ").strip()

if __name__ == "__main__":
    puzzle = get_user_puzzle()

    print("\nYour entered puzzle:")
    for row in puzzle:
        print(row)

    select_algorithm(puzzle)
