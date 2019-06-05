import numpy as np

def sigmoid(x):
    """
    Compute the sigmoid function for the input here.
    Arguments:
    x -- A scalar or numpy array.
    Return:
    s -- sigmoid(x)
    """
    return 1/(1 + np.exp(-x))

a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])
print(b[1])