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



# exercise 1
# create random int array from 10 to 100 with only 5 elements

arr_1 = np.random.randint(10,100,5)
print(arr_1)

# create random int array of shape 5,5

arr_2 = np.random.randint(10,100,(5,5))

# create random array int of shape 80,5,5

arr_3 = np.random.randint(10,100,(80,5,5))


# create uniform array all in the same way

arr_1 = np.random.rand(5)
arr_2 = np.random.rand(5,5)
arr_3 = np.random.rand(80,5,5)

# create normal distribution based custom arrays with the same shapes

arr_1 = np.random.normal(10,100,5)
print(arr_1)
arr_2 = np.random.normal(10,100,(5,5))
arr_3 = np.random.normal(10,100,(80,5,5))

# create pure normal distribution based arrays
arr_1 = np.random.randn(5)
arr_2 = np.random.randn(5,5)
arr_3 = np.random.randn(80,5,5)

