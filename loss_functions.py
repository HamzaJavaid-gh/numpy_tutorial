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


def kl_divergence(y_true, y_pred):
    y_out = y_true*np.log2(y_true/y_pred)
    return y_out

def js_divergence(y_true, y_pred):
    m_val = 1/(2*(y_true+y_pred))
    y_out = 0.5 * kl_divergence(y_true, m_val) + 0.5 * kl_divergence(y_pred, m_val)
    return y_out

def euclidean_dis(feat_v1, feat_v2):
    y_out = np.sum(np.square(feat_v1 - feat_v2))
    return y_out

MARGIN = 10
def contrastive_loss(feat_v1, feat_v2, y_true):
    y_out = (y_true)*np.square(euclidean_dis(feat_v1, feat_v2)) \
        (1 - y_true)*np.max([MARGIN-euclidean_dis(feat_v1, feat_v2),0])
    return y_out

