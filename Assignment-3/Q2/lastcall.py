

# Question 2:
#-----------------------------------------------------
# The function 'lastcall' has a decorator @lastcall
# it receives a function and if the parameter that that given to the function 
# is a new one we print it, otherwise we print a message that told that we have that parameter before
#-----------------------------------------------------

def lastcall(f):
    '''
    >>> f(2)
    4
    >>> f(2)
    'I already told you the answer'
    >>> f(10)
    100
    >>> f(2)
    'I already told you the answer'
    >>> f(10)
    'I already told you the answer'
    '''
    previous_outputs = []

    def wrap(*args, **kwargs):

        if args[0] in previous_outputs:
            return("I already told you the answer")
        
        if kwargs in previous_outputs:
            return("I already told you the answer")

        # if that a new one parameter
        elif args not in previous_outputs or karg not in previous_outputs:
            for arg in args:
                previous_outputs.append(arg)
                return f(*args, **kwargs)
                    
            for karg in kwargs:
                previous_outputs.append(karg)
                return f(*args, **kwargs)
    return wrap

@lastcall
def f(x: int):
    return x**2

# main function
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    # print(f(2))
    # print(f(2))
    # print(f(10))
    # print(f(2))
    # print(f(10)) 

      

    

    
    