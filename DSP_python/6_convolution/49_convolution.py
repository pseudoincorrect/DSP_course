from matplotlib import pyplot as plt 
from matplotlib import style
from scipy import signal
import mysignals as sg
import csv

csvfile = "./DSP_python/6_convolution/convoluted_signal.csv"

def convolution (sig_in, sig_res):
    sig_out = [0 for _ in range(len(sig_1) + len(sig_2))]
    for x in range (len(sig_in) + len(sig_res)):
        sig_out[x] = 0
    for x in range (len(sig_in)):
        for y in range (len(sig_res)):
            sig_out[x+y] += sig_in[x] * sig_res[y]

    with open (csvfile, "w") as output:
        writer = csv.writer(output, lineterminator = ",")       
        for x in sig_out:
            writer.writerow([x])
            
    return sig_out

sig_1          = sg.InputSignal_1kHz_15kHz
sig_2          = sg.Impulse_response
sig_conv_scipy = signal.convolve(sig_1, sig_2, mode = 'same')
sig_conv_custom = convolution(sig_1, sig_2)



style.use('ggplot')
f, plt_arr = plt.subplots(4, sharex = True)
f.suptitle('Multiplot')
plt_arr[0].plot(sig_1)
plt_arr[0].set_title('InputSignal_1kHz_15kHz')
plt_arr[1].plot(sig_2)
plt_arr[1].set_title('Impulse_response')
plt_arr[2].plot(sig_conv_scipy)
plt_arr[2].set_title('convolution scipy')
plt_arr[3].plot(sig_conv_custom)
plt_arr[3].set_title('convolution custom')
plt.show()
