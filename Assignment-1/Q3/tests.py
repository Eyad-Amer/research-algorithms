from ast import main
from tkinter.tix import MAIN
from print_sorted import *

"""
The function receives a data structure of kind consisting of list, tuple, set, dict
and prints it when it is sorted in all levels

>>> print_sorted({"a":5, "c":6, "b":[1,3,2,4]})
{a:5, b:[1,2,3,4], c:6}

>>> print_sorted({"b":[2,3,1,9,7,5], "e":5, "c":(5,2,1,4), "a":[2,1], "d":{2,1,6,4}})
{a:[1, 2] ,b:[1, 2, 3, 5, 7, 9] ,c:(1, 2, 4, 5) ,d:[1, 2, 4, 6] ,e:5}

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()