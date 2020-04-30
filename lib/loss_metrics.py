import tensorflow.keras.backend as K
import tensorflow as tf

def Loss(loss_type = None, wealth = None, w = None, loss_param=None):
    if loss_type == "Entropy":
        return Entropy(wealth, w, loss_param)
    elif loss_type == "CVaR":
        return CVaR(wealth, w, loss_param)

def Entropy(wealth = None, w = None, loss_param = None):
    _lambda = loss_param
    # Entropy (exponential) risk measure
    return (1/_lambda)*K.log(K.mean(K.exp(-_lambda*wealth)))

def CVaR(wealth = None, w = None, loss_param = None):
    alpha = loss_param
    # Expected shortfall risk measure
    return K.mean(w + (K.maximum(-wealth-w,0)/(1.0-alpha)))

