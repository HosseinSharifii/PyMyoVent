import numpy as np
import pandas as pd
from scipy import signal
from scipy.integrate import solve_ivp

from functools import partial
"""simulation_time = 2
time_step = 0.001
Ca_content = 1e-3
k_leak = 2e-3
k_act = 5e-2
k_serca = 10.0

duty_ratio = 0.3
heart_period = 1
activation_frequency = float(1/heart_period)

data_buffer_size = int(simulation_time / time_step)
t = time_step * np.arange(1,data_buffer_size+1)

activation_level =\
    0.5*(1+signal.square(np.pi+2*np.pi*activation_frequency*t,
    duty=duty_ratio))


data = pd.DataFrame({'time':t,
                    'Ca_trans': np.full(data_buffer_size,Ca_content)})
y = np.zeros(2)
y[1] = Ca_content"""
def activation(n,heart_period,time_step,duty_ratio):
    import numpy as np
    activation=np.zeros(n)
    heart_period_index = int(heart_period/time_step)
    for i in range(n):
        if i%heart_period_index==0:
            activation[i:i+int(duty_ratio/time_step)]=1

    return activation
def evolve_kinetics (y, time_step,activation):

    def derives(t,y):
        dy = np.zeros(np.size(y))
        dy[0] = (k_leak+activation*k_act) * y[1] - k_serca * y[0]
        dy[1] = -dy[0]

        return dy
    sol = solve_ivp(derives,[0,time_step], y, method = 'RK23')
    y= sol.y[:,-1]
    #Ca_content = y[0]

    return y

def display_Ca(data,dpi=None):
    from matplotlib import pyplot as plt
    import matplotlib.gridspec as gridspec
    import numpy as np

    no_of_rows = 2
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([10, 4])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax0 = f.add_subplot(spec2[0, 0])
    ax0.plot('time','Ca_trans',data = data,label='Ca transient')
    ax0.set_xlabel("time (ms)")
    ax0.set_ylabel('Ca [mM]')
    ax0.legend(bbox_to_anchor=(1.05, 1),loc = 'best')

    ax1 = f.add_subplot(spec2[1, 0])
    ax1.plot('time','activation',data = data,label='activation')
    ax1.set_xlabel("time (ms)")
    ax1.set_ylabel('activation')
    ax1.legend(bbox_to_anchor=(1.05, 1),loc = 'best')
    print("Saving Ca_states figure to")
    save_figure_to_file(f, "Ca_transient", dpi=dpi)

def save_figure_to_file(f,fname,dpi=None):
    "This function is adopted by Hossein.Sharifi"
    import os
    from skimage.io import imsave

    cwd=os.getcwd()
    filename=cwd + "/"+fname+".png"
    f.savefig(filename, dpi=dpi)

if __name__ == "__main__":
    simulation_time = 2
    time_step = 0.001
    Ca_content = 1e-3
    k_leak = 1e-3
    k_act = 3.5e-1
    k_serca = 8.0

    duty_ratio = 0.003
    heart_period = 0.875
    activation_frequency = float(1/heart_period)

    data_buffer_size = int(simulation_time / time_step)
    t = time_step * np.arange(1,data_buffer_size+1)

    #activation =\
    #    0.5*(1+signal.square(np.pi+2*np.pi*activation_frequency*t,
    #    duty=duty_ratio))
    activation = activation(data_buffer_size,heart_period,time_step,duty_ratio)
    y = np.zeros(2)
    y[1] = Ca_content
    data = pd.DataFrame({'time':t,
                        'Ca_trans': np.zeros(data_buffer_size)})


    for i in np.arange(1,data_buffer_size,1):
        #print(activation[i])
        y = evolve_kinetics(y,time_step,activation[i])

        data.at[i,'time'] = t[i]
        data.at[i,'Ca_trans'] = y[0]*1e3
        data.at[i,'activation'] = activation[i]

    display_Ca(data,dpi = 300)
