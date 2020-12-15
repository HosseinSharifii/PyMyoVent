import numpy as np
import pandas as pd
import scipy.constants as scipy_constants


def display_exp_r4(data,dpi=None):
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec

    no_of_rows = 2
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([4, 4])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax = f.add_subplot(spec2[0,0])
    ax.plot('x','r4',data = data, label='detachment rate')
    x_bound = ax.get_xbound()
    ax.set_xticks([-10,0,10])
    ax.set_xlabel("x (nm)")
    ax.set_ylabel('detachment rate (s$^{-1}$)')

    ax1 = f.add_subplot(spec2[1,0])
    ax1.plot('x','r3',data = data, label='detachment rate')
    x_bound = ax.get_xbound()
    ax1.set_xticks([-10,0,10])
    ax1.set_xlabel("x (nm)")
    ax1.set_ylabel('atachment rate (s$^{-1}$)')

    print("Saving exp detachment rate figure to")
    save_figure_to_file(f, "exp_J4", dpi=dpi)

def save_figure_to_file(f,fname,dpi=None):
    "This function is adopted by Hossein.Sharifi"
    import os
    from skimage.io import imsave

    cwd=os.getcwd()
    filename=cwd + "/"+fname+".png"
    f.savefig(filename, dpi=dpi)

if __name__ == '__main__':

     b_min = -10
     b_max = 10
     b_width = 1
     x = np.arange(b_min,b_max+1,b_width)

     k_3 = 100
     k_4_0 = 86.996
     k_4_1 = 72.3979
     k_cb = 0.000626314
     delta = 0.3
     T = 288
     max_rate = 5000

     r3 = k_3 * np.exp(-k_cb * (x**2) / (2.0 * 1e18 * scipy_constants.Boltzmann * T))
     r4 = k_4_0 * np.exp(-k_cb * x * delta /(1e18 * scipy_constants.Boltzmann * T))
     #r4 = k_4_0 * np.exp(-k_4_1*(k_cb*x))
     indicies = np.where(np.abs(x)>8)
     r4[indicies] = r4[indicies] + (np.abs(x[indicies])- 8)*max_rate
     r4[r4 > max_rate] = max_rate
     data = pd.DataFrame({'x':x,'r3':r3,'r4':r4})
     display_exp_r4(data,dpi=300)
