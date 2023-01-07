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

