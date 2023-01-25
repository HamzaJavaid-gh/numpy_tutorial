import numpy as np


# Excersie 1: Create 1 array of 1's and another of 0's, stack them horizontally then count how many 1's there are

ones_arr_2d = np.ones((5,5))
zeros_arr_2d = np.ones((5,5))

# stack them
# way 1 of concatenating
concat_arr_2d = np.concatenate((ones_arr_2d, zeros_arr_2d), axis=0)
# way 2 of stacking
stack_arr_2d = np.vstack((ones_arr_2d, zeros_arr_2d))
print(stack_arr_2d.shape)
# find number of 1's
ones_count = np.count_nonzero(stack_arr_2d)
print(ones_count)
# another way if you want to find out any constant
ones_count_v2 = np.count_nonzero(stack_arr_2d == 1)
print(ones_count_v2)


# Exercise 2 create 3 arrays stack them and find unique values, also occurances of unique values

arr_uni_zeros = np.zeros((5,5))
arr_uni_ones = np.ones_like(arr_uni_zeros)
arr_uni_const = np.zeros_like(arr_uni_zeros) + 5

stacked_arr_2d = np.vstack((arr_uni_zeros, arr_uni_ones, arr_uni_const))
print(stacked_arr_2d.shape)

uniq_vals = np.unique(stacked_arr_2d)
print(uniq_vals)
#  with occurances
uniq_with_occurance = np.unique(stacked_arr_2d, return_counts=True)
print(uniq_with_occurance)

