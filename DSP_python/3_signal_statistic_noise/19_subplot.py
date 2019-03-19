from scipy import signal
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib import style
import mysignals as sg

t = np.linspace(0, 1.0, 2001)

sig_5Hz = np.sin(2 * np.pi * 5 * t)
sig_250Hz = np.sin(2 * np.pi * 250 * t)
sig_combined = sig_250Hz + sig_5Hz

style.use('ggplot')
f, plt_arr = plt.subplots(3, sharex = True)
plt_arr[0].plot(sig_5Hz)
plt_arr[0].set_title('sig_5Hz')
plt_arr[1].plot(sig_250Hz)
plt_arr[1].set_title('sig_250Hz')
plt_arr[2].plot(sig_combined)
plt_arr[2].set_title('sig_combined')

plt.show()
