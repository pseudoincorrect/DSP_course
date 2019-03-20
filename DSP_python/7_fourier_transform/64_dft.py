from math import cos, pi, sin, sqrt, pow
from copy import copy
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal
from mysignals import InputSignal_1kHz_15kHz


def calc_dft (sig_in):
    N = len(sig_in)
    hN = N/2 # hN stand for half N ==>  N/2
    sig_re   = [0] * (hN)
    sig_im   = [0] * (hN)
    sig_magn = [0] * (hN)

    for k in range(hN):
        for i in range(N):
            sig_re[k] += sig_in[i] * cos((2 * pi * i * k) / N)
            sig_im[k] -= sig_in[i] * sin((2 * pi * i * k) / N)

    for x in range(hN):
        sig_magn[x] = sqrt( pow(sig_re[x], 2) + pow(sig_im[x], 2) )

    return [sig_re, sig_im, sig_magn]


def calc_idft (sig_re, sig_im):
    hN         = len(sig_re) # hN stand for half N =  =>   N/2
    N          = 2*hN
    sig_re_tmp = copy(sig_re)
    sig_im_tmp = copy(sig_im)
    sig_out    = [0] * (2*hN)
    re_part    = im_part                           = 0

    for x in range(hN):
        sig_re_tmp[x] /= hN
        sig_im_tmp[x] /= hN

    for k in range(hN):
        for i in range(N):
            re_part = (sig_re_tmp[k] * cos((2 * pi * i * k) / N)) 
            im_part = (sig_im_tmp[k] * sin((2 * pi * i * k) / N)) 
            sig_out[i] += re_part + im_part

    return sig_out


sig_in = InputSignal_1kHz_15kHz 
sigs_dft = calc_dft(sig_in)
sig_idft = calc_idft(sigs_dft[0], sigs_dft[1])


style.use('ggplot')
f, plt_arr = plt.subplots(3, sharex = True)
f.suptitle('Multiplot')
plt_arr[0].plot(sig_in)
plt_arr[0].set_title('InputSignal_1kHz_15kHz')
plt_arr[1].plot(sigs_dft[2])
plt_arr[1].set_title('DFT MAGN')
plt_arr[2].plot(sig_idft)
plt_arr[2].set_title('IDFT')
plt.show()
