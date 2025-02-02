def print_state(state): 
    for i in range(0,9,3):
        print(" ".join(map(str,state[i:i+3]))) #this will put a space between each number and break into groups of 3

print("write 1 for default puzzle or 2 to input your own")
choice = int(input())
if choice == 1:
    initial_state = [1,2,3,4,8,0,7,6,5]
    
else:
    print("enter your own puzzle and use a zero for the blank!")
    initial_state = []
    for i in range(3):
        row = input(f"enter the {i + 1} row using spaces in between the numbers").split()
        initial_state.extend(map(int,row)) #organizes the row into the initial state


goal_state = [1,2,3,4,5,6,7,8,0]

print_state(initial_state)