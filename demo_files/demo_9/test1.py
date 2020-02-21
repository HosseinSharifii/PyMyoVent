from math import *
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,20,1)
y= (2*np.exp(x))
y2 = (1e8+np.exp(x))

f=plt.figure()
plt.plot(x,y,label='y')
plt.plot(x,y2,label = 'y2')
plt.legend()
plt.show()
