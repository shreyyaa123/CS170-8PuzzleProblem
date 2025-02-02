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

#finds the postion of the numbers in the goal state to compare in later iterations
def find_goalstate_position(num):
    for i in range(len(GOAL_STATE)):
        for j in range(len(GOAL_STATE[i])):
            if GOAL_STATE[i][j] == num:
                return i, j
    return -1, -1