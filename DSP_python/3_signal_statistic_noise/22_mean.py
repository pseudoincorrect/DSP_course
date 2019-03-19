import mysignals as sigs
import numpy as np

def calc_mean(sig_src_arr):
    _mean = 0.0
    for x in range(len(sig_src_arr)):
        _mean += sig_src_arr[x]
    _mean = _mean/len(sig_src_arr)
    return _mean
    
print("with our own algo {}".format(calc_mean(sigs.InputSignal_1kHz_15kHz)))
print("with numpy        {}".format(np.mean(sigs.InputSignal_1kHz_15kHz)))
