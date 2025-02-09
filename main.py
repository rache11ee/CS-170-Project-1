from uniform_cost_search import uniform_cost_search
from puzzle import total_path
from misplaced_heuristic import a_star_misplaced_heuristic
from manhattan_heuristic import a_star_manhattan_heuristic
import time

def print_state(state): 
    for i in range(0,9,3):
        print(" ".join(map(str,state[i:i+3]))) #this will put a space between each number and break into groups of 3

print("write 1 for default puzzle or 2 to input your own")
choice = int(input())
if choice == 1:
    initial_state = [7,2,4,5,0,6,8,3,1]
    
else:
    print("enter your own puzzle and use a zero for the blank!")
    initial_state = []
    for i in range(3):
        row = input(f"type in 3 numbers per row with spaces in between and press enter after each row: ").split()
        initial_state.extend(map(int,row)) #organizes the row into the initial state

print("write 1 to use a* misplaced heuristic, 2 to use a* manhattan heuristic, or 3 to use uniform cost search")
algorithm = int(input())

start_time = time.time()

if algorithm == 1:
    solution_node, max_queue_size, nodes_expanded = a_star_misplaced_heuristic(initial_state)
elif algorithm == 2:
    solution_node, max_queue_size, nodes_expanded = a_star_manhattan_heuristic(initial_state)
elif algorithm == 3:
    solution_node, max_queue_size, nodes_expanded = uniform_cost_search(initial_state)

end_time = time.time()
    

if solution_node:
    path, heuristics, costs = total_path(solution_node)
    for state, heuristic, cost in zip(path, heuristics, costs): #will print all of the states that it takes to get to the goal state
        if state == initial_state:
            print("Initial state: ")
            print_state(state)
            print("\n")
        else:
            print(f"The best state to expand with g(n): {cost} and h(n): {heuristic} is...")
            print_state(state)
            print("\n")
    print(f"Solved in {end_time - start_time:.6f} seconds!")
    print(f"Solution depth was {len(path)}")
    print(f"Max queue size: {nodes_expanded}")
    print(f"Number of nodes expanded: {max_queue_size}")
else:
    print("No solution found!")


