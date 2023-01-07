'''This tutorial explains different ways of creating numpy nd.arrays'''

import numpy as np

# Method 1
vector = np.array([2,4,5]) #Simple 1D array with dtype int64

# Method 2
ones_arr = np.ones((2,2)) #Matrices of size 2,2 (row,col) of 1s
zeros_arr = np.zeros((3,3)) #Matrices of size 3,3 (row,col) of 0s


# Method 3
contigous_arr = np.arange(10) #from 0 to 9
print(contigous_arr)
contigous_step_arr = np.arange(5,10,2) #from 5 to 10 in increments of 2
print(contigous_step_arr)

# Method 4
step_arr = np.linspace(5,10,5)
print(step_arr)


# Method 5
reshaped_arr = np.arange(1,11).reshape(5,2)
print(reshaped_arr)