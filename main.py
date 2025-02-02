from uniform_cost_search import uniform_cost_search
from puzzle import total_path

def print_state(state): 
    for i in range(0,9,3):
        print(" ".join(map(str,state[i:i+3]))) #this will put a space between each number and break into groups of 3

print("write 1 for default puzzle or 2 to input your own")
choice = int(input())
if choice == 1:
    initial_state = [1,2,3,4,5,6,7,0,8]
    
else:
    print("enter your own puzzle and use a zero for the blank!")
    initial_state = []
    for i in range(3):
        row = input(f"type in 3 numbers per row with spaces in between and press enter after each row: ").split()
        initial_state.extend(map(int,row)) #organizes the row into the initial state

solution_node = uniform_cost_search(initial_state)
if solution_node:
    path = total_path(solution_node)
    for state in path: #will print all of the states that it takes to get to the goal state
        print_state(state)
        print("\n")
else:
    print("No solution found!")
