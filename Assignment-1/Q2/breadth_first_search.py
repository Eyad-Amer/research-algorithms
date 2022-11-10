
'''
# Question 2 #

The function "four_neighbor_function" receive a node and returns the 4 neighbors of the node
through the function "breadth_first_search" that receives 3 parameters: source node, destination node and neighbors function and returns the four neighbors of the given node in a 2D lattice

'''

from ast import main
from lib2to3.pytree import Node
from multiprocessing import current_process
from os import path
from queue import Queue


# Function that returns the 4 neighbors of the node
def four_neighbor_function(node: Node):
    (x,y) = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

# The function receives 3 parameters: source node, destination node and neighbors function and returns the four neighbors of the given node in a 2D lattice
def breadth_first_search(start, end, neighbor_function):
    visited = set() # visitors nodes
    queue = Queue() # Queue
    parent = dict() # key:vlaue of parent node

    # Start from the starting point
    visited.add(start)  
    queue.put(start)  

    while not queue.empty():
        current_node = queue.get()

        # if we have finithed
        if current_node == end:
            break

        # add the neighbor
        for i in neighbor_function(current_node):
            if i not in visited:
                visited.add(i)
                queue.put(i)
                parent[i] = current_node

    current_node = end
    path = [end]

    while parent[current_node] != start:
        path.append(parent[current_node])
        current_node = parent[current_node]

    path.append(start)

    # print the result
    result = [] 
    for i in range(len(path)):
        result.append(path.pop())
    return result


if __name__ == '__main__':
    print(breadth_first_search(start=(0, 0), end=(2, 2),neighbor_function=four_neighbor_function))
    print(breadth_first_search(start=(0, 0), end=(2, 3),neighbor_function=four_neighbor_function))

