class Node:
    def __init__(self, state, parent = None, action = None, heuristic = 0, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
    
    