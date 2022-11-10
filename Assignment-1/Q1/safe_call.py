'''
# Question 1 #

The function receives as input a function and arguments with names, and calls the function with the arguments
and checks if the arguments match the types defined in the annotation of the function
'''
from ast import arguments
from tokenize import String


def safe_call(func, *args, **kwargs): 

    # callable: detect if func is a function
    if not callable(func): 
        raise Exception("The first argument is not a function")

    # if the kwargs don't match the types defined in the annotation of the function
    for i,j in kwargs.items():
        if i in func.__annotations__ and func.__annotations__[i] != type(j):
            #raises an exception
            raise Exception(" The kwargs do not match the types defined") 

    # if the arguments don't match the types defined in the annotation of the function
    function_args = [type(i) for i in args][0 : len(func.__annotations__.values())]
    if list(func.__annotations__.values()) != (function_args):
        #raises an exception
        raise Exception(" The arguments do not match the types defined") 

    return (func(*args, **kwargs))


# main function: examples 
if __name__ == '__main__':

    f = 0
    def f1(x: int, y: float, z):
        return x + y + z

    def f2(x: int, y: str, z):
        return y

    print(safe_call(f1, 5, 5.0, z=3)) #should print 13.0
    print(safe_call(f1, 5, 5.0, 3)) #should print 13.0
    print(safe_call(f2, 5, "c", z=3)) #should print c
    print(safe_call(f1, x="asd", y=5.2, z=3)) #should raises an exception
    print(safe_call(f, x=3, y=2.0, z=5)) #should raises an exception
   
