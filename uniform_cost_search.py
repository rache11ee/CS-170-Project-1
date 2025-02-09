import heapq
from node import Node
from puzzle import get_children

goal_state = [1,2,3,4,5,6,7,8,0]

def uniform_cost_search(initial_state):
    initial_node = Node(initial_state)

    node_collection = []
    heapq.heappush(node_collection,initial_node) #initial node is being pushed into the node collection

    heap_history = set()
    max_queue_size = 1
    
    while node_collection:
        current_node = heapq.heappop(node_collection) #heap will pop off the node with the smallest cost
        if current_node.state == goal_state:
            return current_node, max_queue_size, len(heap_history)
        heap_history.add(tuple(current_node.state))
        
        for child in get_children(current_node):
            if tuple(child.state) not in heap_history: #if the child's path has not been explored, add it to the node collection
                child.total_cost = child.goal_cost
                heapq.heappush(node_collection,child)
        
        max_queue_size = max(max_queue_size, len(node_collection))

    return None, max_queue_size


