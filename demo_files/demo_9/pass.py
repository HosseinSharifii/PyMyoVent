from math import *
import numpy as np
import matplotlib.pyplot as plt

#min = 2000
#max = 4000
#slope = 5e4
#n_set = 2.2e6
#n = np.arange(1.5e6,3e6,1)
min = 1e-5#2000
max = 1e-5#7000
slope = 1000
n_set = 3600
n = np.arange(0,10000,1)
if slope != 40 and 50:
    print('u right')
#print(n)
#pass_set= 0.001/(-1-np.exp((n-n_set)/slope))
pass_set = (0+2*np.exp((n-n_set)/slope))/(1+np.exp((n-n_set)/slope))
#pass_set = (1+np.exp((n-n_set)/slope))/(min+max*np.exp((n-n_set)/slope))
f= plt.figure()
plt.plot(n,pass_set)
plt.ticklabel_format(style='sci',axis='both',scilimits=(0,0))
plt.show()
