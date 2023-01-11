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

arr_1d = np.arange(10,20,1)

arr_con = arr_1d[arr_1d>15]  #equivalent to arr_1d = arr_1d[np.where(arr_1d>15)]
print(arr_con)

arr_1d[arr_1d>15] = 2   #equivalent to np.where(arr1d>15,2,arr_1d)
print(arr_1d)
arr_1d[arr_1d<15] = 0
print(arr_1d)


# arr_1 = np.arange(9).reshape(3,3)
# print(arr_1)
#
# arr_1_sec = np.where(arr_1>4)
# print(arr_1_sec)
