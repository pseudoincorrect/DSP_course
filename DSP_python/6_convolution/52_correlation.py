from matplotlib import pyplot as plt 
from matplotlib import style
from scipy import signal
import mysignals as sg

sig_in   = sg.InputSignal_1kHz_15kHz
sig_filt = sg.Impulse_response

sig_conv_out = signal.convolve(sig_in, sig_filt, mode="same")
sig_corr_out = signal.correlate(sig_in, sig_filt, mode="same")

style.use('ggplot')
f, plt_arr = plt.subplots(4, sharex = True)
f.suptitle('Multiplot')
plt_arr[0].plot(sig_in)
plt_arr[0].set_title('InputSignal_1kHz_15kHz')
plt_arr[1].plot(sig_filt)
plt_arr[1].set_title('Impulse_response')
plt_arr[2].plot(sig_conv_out)
plt_arr[2].set_title('convolution scipy')
plt_arr[3].plot(sig_corr_out)
plt_arr[3].set_title('correlation scipy')
plt.show()
