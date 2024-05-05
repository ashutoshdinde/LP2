import heapq

# Define the goal state
goal_state = [1,2,3,8,0,4,7,6,5]

# Define the function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_x, goal_y = divmod(goal_state.index(state[i]), 3)
            current_x, current_y = divmod(i, 3)
            distance += abs(goal_x - current_x) + abs(goal_y - current_y)
    return distance

# Define the function to generate the next possible states
def generate_next_states(state):
    next_states = []
    zero_index = state.index(0)
    if zero_index > 2:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
        next_states.append(new_state)
    if zero_index < 6:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
        next_states.append(new_state)
    if zero_index % 3 != 0:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
        next_states.append(new_state)
    if zero_index % 3 != 2:
        new_state = state[:]
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
        next_states.append(new_state)
    return next_states

# Define the function to print the puzzle state
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
    print()

# Define the A* algorithm
def solve_8_puzzle(initial_state):
    frontier = [(manhattan_distance(initial_state), initial_state, 0)]
    explored = set()
    while frontier:
        _, state, cost = heapq.heappop(frontier)
        if state == goal_state:
            print("Solution found!")
            print_puzzle(state)
            return cost
        explored.add(tuple(state))
        print(f"Current state (cost = {cost}):")
        print_puzzle(state)
        for next_state in generate_next_states(state):
            if tuple(next_state) not in explored:
                heapq.heappush(frontier, (manhattan_distance(next_state) + cost + 1, next_state, cost + 1))
    return None

# Example usage
initial_state = [1,3,4,8,6,2,7,0,5]
print("Initial state:")
print_puzzle(initial_state)
solution_cost = solve_8_puzzle(initial_state)
if solution_cost is not None:
    print(f"Minimum number of moves: {solution_cost}")
else:
    print("No solution found")