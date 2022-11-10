
from ast import main
from tkinter.tix import MAIN
from safe_call import *


# function for testing
f = 0
def f1(x: int, y: float, z):
    return x + y + z

def f2(x: int, y: str, z):
    return y

def f3(x: float, y: int, z: float):
    return x * y * z

    """
    safe_call function:
    The function receives as input a function and arguments with names, and calls the function with the arguments
    and checks if the arguments match the types defined in the annotation of the function

    # good tests
        >>> safe_call(f1, x=5, y=2.0, z=3)
        10.0

        >>> safe_call(f2, 5, "abc", z=3)
        abc

        >>> safe_call(f3, 5.0, 3, 2.0)
        30.0

    # bad tests - throw Exception
        >>> safe_call(f, 5, 2.0, 3)
        raise an Exception("The first argument is not a function")

        >>> safe_call(f1, 5, "abc", 3)
        raise an Exception(" The arguments do not match the types defined") 
    """

    if not callable(f): 
        raise Exception("The first argument is not a function")

    for i,j in kwargs.items():
        if i in func.__annotations__ and func.__annotations__[i] != type(j):
            raise Exception(" The kwargs do not match the types defined") 

    function_args = [type(i) for i in args][0 : len(func.__annotations__.values())]
    if list(func.__annotations__.values()) != (function_args):
        raise Exception(" The arguments do not match the types defined") 

    print(f1(*args, **kwargs))

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()