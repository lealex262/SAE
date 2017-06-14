
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def label_matrix(label_vector):

    # Local Variables: Y, rows, S, labels, label_vector
    # Function calls: indexes, length, zeros, unique, sub2ind, label_matrix, size
    #%LABEL_MATRIX converts the label vector to label matrix.
    #%   Input: 
    #%     label_vector: 1xN, N is the number of samples.
    #%
    #%  Output:
    #%     S: Nxc matrix, c is the number of classes.
    Y = label_vector
    labels = np.unique(Y)
    rows = np.arange(1., (length(Y))+1)
    #%// row indx
    S = np.zeros(length(Y), length(np.unique(indexes)))
    #%// A matrix full of zeros
    S[int(sub2ind[int(matcompat.size[int(S)-1])-1,int(rows)-1,int(indexes)-1])-1] = 1.
    #%// Ones at the desired row/column combinations
    S = S.conj().T
    return 