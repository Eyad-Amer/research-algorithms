from ast import main
from tkinter.tix import MAIN
from breadth_first_search import *

"""
The function "four_neighbor_function" receive a node and returns the 4 neighbors of the node
through the function "breadth_first_search" that receives 3 parameters: source node, destination node and neighbors function and returns the four neighbors of the given node in a 2D lattice

>>> breadth_first_search(start=(0, 0), end=(2, 2),neighbor_function=four_neighbor_function)
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

>>> breadth_first_search(start=(0, 0), end=(2, 3),neighbor_function=four_neighbor_function)
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]

"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()