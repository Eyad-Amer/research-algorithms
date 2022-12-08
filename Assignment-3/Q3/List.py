

# Question 3:
#-----------------------------------------------------
# The function behaves as a structure called LIST, which is similar to a list in Python
# and it is possible to access the details in matrix syntax
#-----------------------------------------------------

class List(list):
    # __getitem__() is a magic method in Python, which when used in a class, allows its instances to use the [] (indexer) operators.
    def __getitem__(self, keys):
        
        """
        >>> mylst = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])
        >>> mylst[0,1,3] == 66
        True
        >>> mylst[1,0,0] == 7
        True
        >>> print(mylst[1,1,1])
        11
        >>> print(mylst[0,0,0])
        1
        """

        lst = list(self) # list of self object
        #this loop return the object item in index i in the list
        for i in keys:
            lst = lst[i]
        return lst    

# main function
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    mylst = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])

    print(mylst[1,1,1])
    print(mylst[0,0,0])
   