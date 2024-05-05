import heapq

goal_state = [1,2,3,8,0,4,7,6,5]

def manhattan_distance(state):
    return sum(abs(state.index(i) // 3 - goal_state.index(i) // 3) + abs(state.index(i) % 3 - goal_state.index(i) % 3) for i in state if i != 0)

def generate_next_states(state):
    zero_index = state.index(0)
    next_states = []
    for move in [-3, 3, -1, 1]:
        if 0 <= zero_index + move < 9 and abs(zero_index // 3 - (zero_index + move) // 3) + abs(zero_index % 3 - (zero_index + move) % 3) == 1:
            new_state = state[:]
            new_state[zero_index], new_state[zero_index + move] = new_state[zero_index + move], new_state[zero_index]
            next_states.append(new_state)
    return next_states

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(*state[i:i+3])
    print()

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

initial_state = [1,3,4,8,6,2,7,0,5]
print("Initial state:")
print_puzzle(initial_state)
solution_cost = solve_8_puzzle(initial_state)
if solution_cost is not None:
    print(f"Minimum number of moves: {solution_cost}")
else:
    print("No solution found")
