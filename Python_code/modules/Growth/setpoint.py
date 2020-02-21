import numpy as np
import pandas as pd

def return_setpoint(self,start_time_second,time_step,data):
    window = 5000

#    setpoint_array = np.array(data[50000:].rolling(window=window).mean())
#    setpoint=np.mean(setpoint_array[window:])

    max_data = data[50000:].max()
    min_data = data[50000:].min()
    setpoint = (max_data-min_data)/2+min_data
    """i=int(start_time_second/time_step)
    number_of_segments = 10
    n=number_of_segments
    interval_span_seconds=start_time_second/n
    interval_span_index = int(interval_span_seconds/time_step)
    setpoint_array= np.zeros(n)
    for j in range(n):
        setpoint_array[j]=np.mean(data[(i+(j-n)*interval_span_index):i])
    setpoint = np.mean(setpoint_array)"""
    return setpoint
