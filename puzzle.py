from node import Node

def get_possible_moves(state):
    moves = []
    empty_index = state.index(0)
    row, col = empty_index // 3, empty_index % 3

    if row > 0:
        moves.append((-1,0)) #this will move the blank up, but NOT side to side
    if row < 2:
        moves.append((1,0)) #this will move the blank down
    if col > 0:
        moves.append((0,-1)) #this will move the blank to the left
    if col < 2:
        moves.append((0,1)) #this will move the blank to the right

def get_children(node):
    children = []
    empty_index = node.state.index(0)
    row, col = empty_index // 3, empty_index % 3

    for dir_of_x, dir_of_y in get_possible_moves(node.state): #makes a move, outputs (children) are created as a result of that move
        new_row, new_col = row + dir_of_x, col + dir_of_y
        new_index = new_row * 3 + new_col
        new_state = node.state[:]
        new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
        children.append(Node(new_state,node,(dir_of_x,dir_of_y),0,node.cost + 1))
        
    return children