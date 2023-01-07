import numpy as np

arr_1 = np.zeros((3,3,3))
arr_2 = np.ones_like(arr_1)

stacked_in_depth = np.concatenate((arr_1,arr_2), axis=0)
print(stacked_in_depth.shape)

stacked_in_rows = np.concatenate((arr_1, arr_2), axis=1)
stacked_in_col = np.concatenate((arr_1, arr_2), axis=2)




