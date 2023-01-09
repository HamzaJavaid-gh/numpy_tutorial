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


# Exercise 1
# create simple 1D vector of random numbers of type int32

arr_1 = np.array([1,2,3], dtype=np.int32)

# 2
# create simple 2D vector of type float32
arr_2 = np.array([[1,2,3],
                  [4,5,6]], dtype=np.float32)

# 3
# create 1D vector of 1s that have 6 elements
arr_ones = np.ones(5, dtype=np.int32)
print(arr_ones)
# create 2D vector of 1s
arr_2d = np.ones((5,5), dtype=np.float32)
# create 3D vector of 1s
arr_3d = np.ones((10,5,5), dtype=np.int64)

# Do all same things with zeros

arr_zeros = np.zeros(5)

arr_2d = np.zeros((5,5))

arr_3d = np.zeros((50,5,5))

# Do all these with arange

arr_1d = np.arange(5)

arr_1d_step = np.arange(10,21,1)

arr_1d_2d = np.arange(16).reshape(4,4)
print(arr_1d_2d)

arr_1d_3d = np.arange(8).reshape(2,2,2)
print(arr_1d_3d)

# Do all these with linspace

arr_1d = np.linspace(11,20,10).astype(np.int64)
arr_1d_arange = np.arange(11,21,1)
print(arr_1d)
print(arr_1d_arange)

arr_2d_lin = np.linspace(10,20,8).astype(np.int64).reshape(2,2,2)
print(arr_2d_lin)

# Explore zeros like and ones_like and full

simple_arr = np.arange(1,11,1)
ones_arr = np.ones_like(simple_arr) #imp for image processing applications
zeros_arr = np.zeros_like(simple_arr)


