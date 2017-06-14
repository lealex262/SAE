
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def SAE(X, S, lamb):

    # Local Variables: A, C, B, S, W, X, lambda
    # Function calls: sylvester, SAE
    #% SAE is Semantic Auto-encoder
    #% Inputs:
    #%    X: dxN data matrix.
    #%    S: kxN semantic matrix.
    #%    lambda: regularisation parameter.
    #%
    #% Return: 
    #%    W: kxd projection matrix.
    A = np.dot(S, S.conj().T)
    B = np.dot(np.dot(lamb, X), X.conj().T)
    C = np.dot(np.dot(1.+lamb, S), X.conj().T)
    W = sylvester(A, B, C)
    return 