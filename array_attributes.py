import numpy as np


simple_arr = np.array([5,10,115], dtype=np.float64)

print(simple_arr.dtype)
print(simple_arr.shape)
print(simple_arr.size)
print(simple_arr.ndim)


two_dim_arr = np.ones((5,2))
print(two_dim_arr.shape)
