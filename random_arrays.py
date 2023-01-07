import numpy as np

# method 1
arr_randInt = np.random.randint(5,25,(5,5))
print(arr_randInt)
print(arr_randInt.shape)

# method 2
arr_randUni = np.random.rand(5,5)
print(arr_randUni)

# method 3
arr_randSel = np.random.uniform(5,25,(5,5))
print(arr_randSel)

