

import sys
import math



maxNumber = 0 # max number in the list
countWorst = 0 # loss 
maxWorst = 0 # maximal loss

n = int(input())
v = [] # an list that have the numbers of the 
for i in input().split(): # input n numbers
    v.append(int(i))

maxNumber = v[0]

for i in range(len(v)-1):
    if maxNumber > v[i+1]: # if we have a loss
        countWorst = v[i+1] - maxNumber
    else:
        maxNumber = v[i+1] # update maximal number

    # update maximal loss
    if maxWorst > countWorst:
        maxWorst = countWorst

# print the answer
print(maxWorst)
