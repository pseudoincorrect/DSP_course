from matplotlib import pyplot as plt 
from matplotlib import style
import mysignals as sg

style.use('ggplot')
f, plt_arr = plt.subplots(3, sharex = True)
f.suptitle('Multiplot')

plt_arr[0].plot(sg.InputSignal_1kHz_15kHz)
plt_arr[0].set_title('plot 0')
plt_arr[1].plot(sg.InputSignal_1kHz_15kHz)
plt_arr[1].set_title('plot 1')
plt_arr[2].plot(sg.InputSignal_1kHz_15kHz)
plt_arr[2].set_title('plot 2')

plt.show()
