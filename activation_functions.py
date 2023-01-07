import numpy as np


# Relu activation
def relu(x_in):
    y_out = np.where(x_in>0,x_in,0)
    return y_out

# Softmax Activation
def sigmoid(x_in):
    y_out = np.exp(x_in)/np.sum(np.exp(x_in))
    return y_out

# TanH Activation
def tanh(x_in):
    y_out = (np.exp(x_in) - np.exp(-x_in)) / (np.exp(x_in) + np.exp(-x_in))
    return y_out

# Sigmoid Activation
def sigmoid(x_in):
    y_out = 1 / (1 + np.exp(x_in))
    return y_out