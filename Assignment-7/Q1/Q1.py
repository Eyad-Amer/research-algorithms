
import math
import random
import time
import numpy as np
import cvxpy as cp
from cvxpy import log
import matplotlib.pyplot as plt


# Question 1:
#-----------------------------------------------------
# The purpose of the question is to check which library is faster: numpy or cvxpy 
# A) Write code that automatically creates a system of linear equations on different sizes, with random coefficient.
# B) Solve each of the system of linear equations using numpy and cvxpy.
# C) Graph the runtime as a function of system size.
#-----------------------------------------------------

numOfVariables  = 5 # number of variables in the system of linear equations
coefficients = 10 # number of the sizes of linear equations

################################## (A) #########################################

# The function creates a system of linear equations on different sizes, with random coefficient
# The function receives the number of linear equations it needs to produce
# The function generates and returns a systems of linear equations
def create_linear_equations():

    numOfVar = np.random.randint(low=1, high=numOfVariables) # random of the number of variables
    coefficient = np.random.randint(low=coefficients*-1, high=coefficients) # random coefficient

    # The system of linear equations to be solved is represented in the form of matrix AX = B
    A, X, B = [], [], []

    # creates a system of linear equations on different sizes, with random coefficient
    for i in range(0, numOfVar):
        coefficient = np.random.randint(low=coefficients*-1, high=coefficients) # random coefficient
        tempa = []
        B.append([coefficient]) # results
        X.append(['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i]]) # variables
        for j in range(0, numOfVar):
            coefficient = np.random.randint(low=coefficients*-1, high=coefficients) # random coefficient
            tempa.append(coefficient) # coefficients
            
        A.append(tempa)

    return A,B

################################## (B) #########################################

# Solve the system of linear equations using numpy
# The system of linear equations to be solved is represented in the form of matrix AX = B
def numpy_solution(A, B):
    a = np.array(A)
    b = np.array(B)
    x = np.linalg.solve(a, b)

    return x
    # print(np.allclose(np.dot(a, x), b))


# Solve the system of linear equations using cvxpy
# The system of linear equations to be solved is represented in the form of matrix AX = B
def cvxpy_solution(A,B):
    A = np.array(A)
    n = A.shape[0]
    X = cp.Variable(shape=(n,1))
    constraints = [A @ X == B]
    prob = cp.Problem(cp.Minimize(0) ,constraints)
    prob.solve()
    return X.value

        

if __name__ == "__main__":
    A, B = create_linear_equations()
    numpy_time = []
    cvxpy_time = []


    start1 = time.time()
    for i in range(1, 20):
        numpy_solution(A, B)
    end1 = time.time()    
    print("numpy:", end1 - start1)
    

    start2 = time.time()
    for i in range(1, 20):
        cvxpy_solution(A, B)
    end2 = time.time()    
    print("cvxpy:", end2 - start2)

    for i in range (1, 20):
        start1 = time.time()
        numpy_solution(A, B)
        end1 = time.time() 
        numpy_time.append(end1 - start1)

    for i in range (1, 20):
        start2 = time.time()
        cvxpy_solution(A, B)
        end2 = time.time() 
        cvxpy_time.append(end2 - start2)

    
    # making the graph that compare the two options
    fig, gr = plt.subplots()

    gr.plot(numpy_time, 'blue')
    gr.plot(cvxpy_time, 'red')
    gr.set_title('numpy: blue --- cvxpy: red')
    plt.show()
    # numpy faster then cvxpy


   