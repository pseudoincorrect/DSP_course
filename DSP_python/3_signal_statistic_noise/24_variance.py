import mysignals as sigs
import numpy as np

def calc_var(sig):
    mean = 0.0
    var  = 0.0 
    
    for x in range(len(sig)):
        mean += sig[x]
    mean = mean/len(sig)
    
    for x in range(len(sig)):
        var += (sig[x] - mean)**2
    var /= len(sig) 

    return var

print("with our own algo {}".format(calc_var(sigs.InputSignal_1kHz_15kHz)))
print("with numpy        {}".format(np.var(sigs.InputSignal_1kHz_15kHz)))
