import numpy as np

arr_1 = np.arange(5,10)

arr_2 = arr_1[arr_1 > 7] #this should give output 8 9
print(arr_2)
arr_1[arr_1 > 7] = 15 # the last 2 elements shoould've been replaced with 15
print(arr_1)


# To check if any element is greater than 7
check_flag_any = np.any(arr_1 > 7)

# To check if all elements are greater than 7
check_flag_all = np.all(arr_1 > 7)


# Working with indices based operations

arr_in1 = np.arange(1,6)
arr_in2 = np.arange(6,11)

# arr_in2(np.where(arr_in1>4)) # trying to get last element of arr2, not possible

# correct way
ind_arr = np.where(arr_in1>4)
print(arr_in2[ind_arr])
# or
print(arr_in2[np.where(arr_in1>4)])


# Explanation of np.where, np.argwhere

# np.where only returns the indices
# on 1d array
arr_1d = np.arange(1,10,1)
print(arr_1d)
arr_con = np.where(arr_1d>6)
print(arr_con)
print(arr_1d[arr_con])

# if you want to replace elements based on a condition
arr_con2 = np.where(arr_1d>6,0,arr_1d)
print(arr_con2)

arr_con3 = np.where(arr_1d>4,5,8)
print(arr_con3)


# exrcises for conditionals within the array
# 1D array
arr_1d = np.arange(10,20,1)

arr_con = arr_1d[arr_1d>15]  #equivalent to arr_1d = arr_1d[np.where(arr_1d>15)]
print(arr_con)

arr_1d[arr_1d>15] = 2   #equivalent to np.where(arr1d>15,2,arr_1d)
print(arr_1d)
arr_1d[arr_1d<15] = 0
print(arr_1d)


# 2D Arrays

arr_2d = np.arange(1,10,1).reshape(3,3)
print(arr_2d)

# use np.where
arr_mid_ind = np.where(arr_2d>5)
print(arr_2d[arr_mid_ind])
# use only the condition
arr_mid_ind = arr_2d[arr_2d > 5]
print(arr_mid_ind)

# now set all the elements
arr_set_2d = np.where(arr_2d>5,2,arr_2d)
print(arr_set_2d)
# with simple conditionals
arr_2d[arr_2d>5] = 2
print(arr_2d)


# 3D array

arr_3d = np.arange(1,9,1).reshape(2,2,2)
print(arr_3d)

# use np.ehre to perform conditionals

arr_3d_mid = np.where(arr_3d>5)
print(arr_3d[arr_3d_mid])

# use simple conditionals to do the same

set_arr = arr_3d[arr_3d>5]
print(set_arr)

# Now do the set and return the original elements as well

arr_mid = np.where(arr_3d>5,2,arr_3d)
print(arr_mid)
# do with conditional
arr_3d[arr_3d>5] = 2
print(arr_3d)