import heapq

GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#different iterations of the puzzle
class PuzzleState:

    def __init__(self, board, parent_state = None, move_direction = None, heuristic_function = None):
        self.board = board
        self.parent_state = parent_state
        self.move_direction = move_direction
        self.heuristic_function = heuristic_function

        if self.heuristic_function is not None:
            self.h = self.heuristic_function(self.board)
        else:
            self.heuristic_function = 0

        if self.parent_state is None:
            self.g = 0
        else:
            self.g = self.parent_state.g + 1

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    #heuristic in uniform cost seach is 0 so this function will only return 0 
    @staticmethod
    def uniform_cost(board):
        return 0

    #calculates the distance between the current state and the goal state
    #If reached goal state then distance = 0
    @staticmethod
    def manhattan_distance(board):
        distance = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != 0 and board[i][j] != GOAL_STATE[i][
                        j]:  # Ignore 0 (empty space)
                    expected_i, expected_j = find_goalstate_position(
                        board[i][j])
                    distance += abs(expected_i - i) + abs(expected_j - j)
        return distance

    #counts how many tiles are not in the right positon
    #If reached goal state then count = 0
    @staticmethod
    def misplaced_tile(board):
        count = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 0 and board[i][j] != GOAL_STATE[i][
                        j]:  # Ignore 0 (empty space)
                    count += 1
        return count

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
        new_neighbors = []

        #Move Up
        if zero_position_row > 0:
            new_board = [row[:] for row in self.board]
            new_board[zero_position_row][zero_position_column] = new_board[
                zero_position_row - 1][zero_position_column]
            new_board[zero_position_row - 1][zero_position_column] = 0
            new_neighbor_state = PuzzleState(new_board, self, "U", self.heuristic_function)
            new_neighbors.append(new_neighbor_state)

        #Move Down
        if zero_position_row < 2:
            new_board = [row[:] for row in self.board]
            new_board[zero_position_row][zero_position_column] = new_board[
                zero_position_row + 1][zero_position_column]
            new_board[zero_position_row + 1][zero_position_column] = 0
            new_neighbor_state = PuzzleState(new_board, self, "D", self.heuristic_function)
            new_neighbors.append(new_neighbor_state)

        #Move Left
        if zero_position_column > 0:
            new_board = [row[:] for row in self.board]
            new_board[zero_position_row][zero_position_column] = new_board[
                zero_position_row][zero_position_column - 1]
            new_board[zero_position_row][zero_position_column - 1] = 0
            new_neighbor_state = PuzzleState(new_board, self, "L", self.heuristic_function)
            new_neighbors.append(new_neighbor_state)

        #Move Right
        if zero_position_column < 2:
            new_board = [row[:] for row in self.board]
            new_board[zero_position_row][zero_position_column] = new_board[
                zero_position_row][zero_position_column + 1]
            new_board[zero_position_row][zero_position_column + 1] = 0
            new_neighbor_state = PuzzleState(new_board, self, "R", self.heuristic_function)
            new_neighbors.append(new_neighbor_state)

        return new_neighbors


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

#finds the postion of the numbers in the goal state to compare in later iterations
def find_goalstate_position(num):
    for i in range(len(GOAL_STATE)):
        for j in range(len(GOAL_STATE[i])):
            if GOAL_STATE[i][j] == num:
                return i, j
    return -1, -1


def general_search(initial_state, heuristic_function):
    unexplored_nodes = []
    explored_nodes = set()
    max_queue_size = 0
    nodes_expanded = 0
    
    #pushes the starting node to the priorty queue
    heapq.heappush(unexplored_nodes, initial_state)
    while len(unexplored_nodes) > 0:
        max_queue_size = max(max_queue_size, len(unexplored_nodes))
        nodes_expanded +=1
        current_state = heapq.heappop(unexplored_nodes)
        depth = current_state.g
        if current_state.is_goal():
            path_trace = []
            while current_state:
                path_trace.append(current_state.board)
                current_state = current_state.parent_state
            path_trace.reverse()
            for i in path_trace:
                print(i[0])
                print(i[1])
                print(i[2])
                print()
            print("Goal State!")
            print()
            print("Solution depth was" , depth)
            print("Number of nodes expanded:" , nodes_expanded)
            print("Max queue size:" , max_queue_size)
            return path_trace
        board_tuple = tuple(map(tuple,current_state.board))
        if board_tuple in explored_nodes:
            continue
        explored_nodes.add(board_tuple)
        neighbor_states = current_state.get_neighbors()

        for i in neighbor_states:
            if tuple(map(tuple,i.board)) not in explored_nodes:
                heapq.heappush(unexplored_nodes, i)
                

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
    
if __name__ == "__main__":
    puzzle = get_user_puzzle()

    print("\nYour entered puzzle:")
    for row in puzzle:
        print(row)

    # Select the algorithm to use
    heuristic_function = select_algorithm(puzzle)
    
    general_search(PuzzleState(puzzle, None, None, heuristic_function), heuristic_function)
    
