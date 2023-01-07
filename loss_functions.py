import numpy as np

def mse_loss(y_true, y_pred):
    loss = np.sum(np.square(y_true - y_pred))
    return loss


def mae_loss(y_true, y_pred):
    loss = np.sum(np.abs(y_true-y_pred))
    return loss


def bin_cross_entropy(y_true, y_pred):
    loss = np.sum((y_true)*np.log(y_pred) + (1-y_true) * np.log(1 - y_pred))
    return loss

def cat_cross_entropy(y_true, y_pred):
    loss = np.sum(y_true*np.log(y_pred))
    return loss


