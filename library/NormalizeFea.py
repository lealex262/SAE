
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def NormalizeFea(fea, row):

    # Local Variables: nSmp, fea, i, feaNorm, mFea, fea2, row
    # Function calls: max, mynorm, issparse, ones, exist, NormalizeFea, sum, size
    #% if row == 1, normalize each row of fea to have unit norm;
    #% if row == 0, normalize each column of fea to have unit norm;
    if not exist('row', 'var'):
        row = 1.
    
    
    #% if row
    #%     nSmp = size(fea,1);
    #%     feaNorm = max(1e-14,full(sum(fea.^2,2)));
    #%     fea = spdiags(feaNorm.^-.5,0,nSmp,nSmp)*fea;
    #% else
    #%     nSmp = size(fea,2);
    #%     feaNorm = max(1e-14,full(sum(fea.^2,1))');
    #%     fea = fea*spdiags(feaNorm.^-.5,0,nSmp,nSmp);
    #% end
    #%             
    #% return;
    if row:
        [nSmp, mFea] = matcompat.size(fea)
        if issparse(fea):
            fea2 = fea.conj().T
            feaNorm = mynorm(fea2, 1.)
            for i in np.arange(1., (nSmp)+1):
                fea2[:,int(i)-1] = fea2[:,int(i)-1]/matcompat.max(1e-10, feaNorm[int(i)-1])
                
            fea = fea2.conj().T
        else:
            feaNorm = np.sum((fea**2.), 2.)**.5
            fea = fea/feaNorm[:,int(np.ones(1., mFea))-1]
            
        
    else:
        [mFea, nSmp] = matcompat.size(fea)
        if issparse(fea):
            feaNorm = mynorm(fea, 1.)
            for i in np.arange(1., (nSmp)+1):
                fea[:,int(i)-1] = fea[:,int(i)-1]/matcompat.max(1e-10, feaNorm[int(i)-1])
                
        else:
            feaNorm = np.sum((fea**2.), 1.)**.5
            fea = fea/feaNorm[int(np.ones(1., mFea))-1,:]
            
        
        
    
    return [fea]