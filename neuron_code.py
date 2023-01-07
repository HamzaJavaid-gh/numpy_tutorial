import numpy as np


def neuron(x_in, w_in, bias):
    y_out = np.dot(x_in,w_in) + bias
    return y_out