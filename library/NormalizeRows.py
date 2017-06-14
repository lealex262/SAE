
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def NormalizeRows(a, type):

    # Local Variables: a, b, type, normF, normFUsed
    # Function calls: sum, bsxfun, sqrt, nargin, abs, error, NormalizeRows
    #% Normalizes the rows of a using specified normalisation type. Makes sure 
    #% there is no division by zero: b will not contain any NaN entries.
    #%
    #% a:            data with row vectors
    #% type:         String:
    #%                   'L1' (default) Sums to 1
    #%                   'L2' Unit Length
    #%                   'Sqrt->L1' Square root followed by L1
    #%                   'L1->Sqrt' L1 followed by Square root. Becomes unit length
    #%                   'Sqrt->L2' Square root followed by L2. Square rooting
    #%                               while keeping the sign
    #%                   'None' No normalization
    #% 
    #% b:            normalized data with row vecors. 
    #% normF:        Normalization factor per row (when valid)
    #%
    #% Jasper Uijlings, 2011
    #% Default: L1
    if nargin == 1.:
        type = 'L1'
    
    
    _switch_val=type
    if False: # switch 
        pass
    elif _switch_val == 'L1':
        normF = np.sum(a, 2.)
        #% Get sums
        normFUsed = normF
        normFUsed[int((normFUsed == 0.))-1] = 1.
        #% Prevent division by zero
        b = bsxfun(rdivide, a, normFUsed)
        #% Normalise
    elif _switch_val == 'L2':
        normF = np.sqrt(np.sum((a*a), 2.))
        #% Get length
        normFUsed = normF
        normFUsed[int((normFUsed == 0.))-1] = 1.
        #% Prevent division by zero
        b = bsxfun(rdivide, a, normFUsed)
    elif _switch_val == 'Sqrt->L1':
        b = NormalizeRows(np.sqrt(a), 'L1')
        normF = np.array([])
    elif _switch_val == 'L1->Sqrt':
        #% This is the same as ROOTSIFT
        b = np.sqrt(NormalizeRows(np.abs(a), 'L1'))
        normF = np.array([])
    elif _switch_val == 'Sqrt->L2':
        b = NormalizeRows(np.sqrt(a), 'L2')
        normF = np.array([])
    elif _switch_val == 'None':
        b = a
        normF = np.array([])
    else:
        matcompat.error('Wrong normalization type given')
    
    return [b, normF]