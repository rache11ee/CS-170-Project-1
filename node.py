class Node:
    def __init__(self, state, parent = None, action = None, heuristic = 0, goal_cost = 0, total_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.goal_cost = goal_cost
        self.total_cost = total_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    