import heapq


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
            print("Goal state reached!")
            print()
            print(f"Solution depth was {depth}")
            print(f"Number of nodes expanded: {nodes_expanded}")
            print(f"Max queue size: {max_queue_size}")
            return path_trace
        
        board_tuple = tuple(map(tuple,current_state.board))
        if board_tuple in explored_nodes:
            continue
        explored_nodes.add(board_tuple)
        neighbor_states = current_state.get_neighbors()

        for i in neighbor_states:
            if tuple(map(tuple,i.board)) not in explored_nodes:
                heapq.heappush(unexplored_nodes, i)