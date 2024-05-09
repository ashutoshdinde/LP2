return sum(abs(state.index(i) // 3 - goal_state.index(i) // 3) + abs(state.index(i) % 3 - goal_state.index(i) % 3) for i in state if i != 0)
