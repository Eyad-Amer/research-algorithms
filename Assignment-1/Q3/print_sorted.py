from ast import main
from cgitb import reset
from ctypes import sizeof
from ctypes.wintypes import INT
import numbers
from tkinter.tix import MAIN
from tokenize import Number
from unicodedata import numeric

'''
# Question 3 #

The function receives a data structure of kind consisting of list, tuple, set, dict
and prints it when it is sorted in all levels
'''

def print_sorted(lst):

    count = 0
    print("{",end="")

    # sort the the key in dict
    lst_sorted = sorted(lst.items(), key=lambda x: x[0])


    for i in lst_sorted:
        count += 1

        # if the item is a list
        if type(i[1]) is list:
            print(i[0], ":" ,sort_list(i[1]) ,end=" ")

        # if the item is a tuple
        if type(i[1]) is tuple:
            print(i[0], ":" ,sort_tuple(i[1]) ,end=" ")

        # if the item is a set
        if type(i[1]) is set:
            print(i[0], ":" ,sort_set(i[1]) ,end=" ")

        # if the item is a dict
        if type(i) is dict:
            print(i[0], ":" ,sort_dict(i[1]) ,end=" ")

        # if the item is a number
        if type(i[1]) == int or type(i[1]) == float:
            print(i[0], ":" ,i[1] ,end=" ")

        # print a ","
        if count != len(lst_sorted):
            print(", ", end="")

    print("}",end="")

# return a sorted list
def sort_list(l: list):
    result_list = l
    result_list.sort()
    return result_list
        
# return a sorted tuple
def sort_tuple(t: tuple):
    result_tuple = tuple(sorted(t))
    return result_tuple

# return a sorted set
def sort_set(s: set):
    return sorted(s)

# return a sorted dict
def sort_dict(d: dict):
    return dict(sorted(d.items(), key=lambda x:x[0]))


    
# main function: examples 
if __name__ == '__main__':
    l1 = {"b":[2,3,1,9,7,5], "e":5, "c":(5,2,1,4), "a":[2,1], "d":{2,1,6,4}}
    l2 = {"a":5, "c":6, "b":[1,3,2,4]}
    print_sorted(l1) # should print: {a:[1, 2] ,b:[1, 2, 3, 5, 7, 9] ,c:(1, 2, 4, 5) ,d:[1, 2, 4, 6] ,e:5}
    print()
    print_sorted(l2) # should print {a:5, b:[1,2,3,4], c:6}
