import copy

# Question 1:
#-----------------------------------------------------
# The iterator receives a list S of different positive numbers and a positive number C as input.
# A) The function returns a series of all subsets of S, whose sum is at most C.
# B) The function returns a series of all subsets of S, whose sum is at most C in ascending order.
#-----------------------------------------------------

class bounded_subsets:
    '''
    >>> for s in bounded_subsets([1,2,3], 4):   print(s) 
    [] 
    [1] 
    [2] 
    [3] 
    [1, 2] 
    [1, 3]

    >>> for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):   print(s) 
     (0, [])
    (1, [0])
    (2, [1])
    (3, [2])
    (4, [3])
    
    '''

    def __init__(self, S: list, C: float):
        self.S = S
        self.C = C
        self.ans = [[]]
    
        for i in self.S:
            if i < 0:
                raise Exception("Error, negative number")
            elif i <= self.C:
                self.ans.append([i])

        self.create_subsets(self.ans)
        self.first = 0
        self.end = len(self.ans)

    # self iterator    
    def __iter__(self):
        return self

    # iterator.next++
    def __next__(self):
        
        if self.first >= self.end : raise StopIteration

        res = self.first
        self.first += 1
        return self.ans[res]

    def create_subsets(self, ans: list):
       
        for i in ans:
            if sum(i) < self.C:
                for j in self.S:
                    temp = []
                    if j not in i:
                        if j + sum(i) <= self.C:
                            temp = copy.deepcopy(i)
                            temp.append(j)
                            temp.sort()
                            
                            if temp not in ans:
                                ans.append(temp)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    for s in bounded_subsets([1,2,3], 4):   
        print(s)

    # for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):  
    #     print(s) 
