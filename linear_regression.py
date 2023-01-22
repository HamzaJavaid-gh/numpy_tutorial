"""This script illustrates simple linear regression problem over a range of epochs
   to show the process of gradient descent"""


"""Linear Regression Equation output = bias + (weight*input) +eta """

import numpy as np
"""STEP 1: First we will generate custom training data and select true values for bias and weight"""

true_bias = 1.02
true_weight = 3.5
eta = 0.01


# Generate 1D vector with a uniform distribution between 10 and 30 of size 100 = input
min = 10
max = 30
N = 100
x_true = np.random.randint(min,max,N)

# Generate y_true = actual_output
y_true = true_bias + (true_weight*x_true) + eta

# shuffle training data
len_data = x_true.size
idx = np.arange(len_data)
np.random.shuffle(idx)
print(idx)

idx_train = idx[:int(len_data*.8)]
idx_val = idx[int(len_data*.8):]
print(idx_val)

# x_train is our training data y_train is our true output data
x_train, y_train = x_true[idx_train], y_true[idx_train]
x_val, y_val = x_true[idx_val], y_true[idx_val]

# select random weight and bias value
# initial_bias = np.random.randint(0,3,1)
# initial_weight = np.random.randint(1,5,1)
initial_bias = 1.5
initial_weight = 5.5

n_epochs = 100
lr = 0.001

for i in range(n_epochs):

    # STEP 1 Forward pass
    y_hat = initial_bias + (initial_weight*x_train) + eta

    # STEP 2 Loss Computation
    loss = np.mean(np.square(y_hat - y_train))
    print('Current Error: ', loss)

    #STEP 3 Gradient Compuattion for b and w
    grad_b = 2 * loss
    grad_W = 2 * (x_train*(y_hat - y_train)).mean()

    #STEP 4 Update params with optimizer (gradient descent)

    initial_bias = initial_bias - (lr * grad_b)
    initial_weight = initial_weight - (lr * grad_W)


print('After 100 epochs Bias and Weight values are: ', initial_bias, initial_weight)













