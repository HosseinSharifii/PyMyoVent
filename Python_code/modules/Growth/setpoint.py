import numpy as np
import pandas as pd

def growth_driver(self):
    if self.growth["driven_signal"][0] == "stress":
        i=self.start_index
#0.88
        self.passive_stress_null =\
            0.88*((self.hs.hs_data["pas_force"][int(i/2):i+1]).mean())
        self.gr_data['pas_force_null'] =\
        pd.Series(np.full(self.data_buffer_size,self.passive_stress_null))
#1.23
        self.cb_stress_null =\
            1.23*((self.hs.hs_data["cb_force"][int(i/2):i+1]).mean())
        self.gr_data['cb_force_null'] = \
        pd.Series(np.full(self.data_buffer_size,self.cb_stress_null))

        print('***')
        print('Growth module is activated!')
        print('with passive force_null of ',self.passive_stress_null)
        print('and active force_null of',self.cb_stress_null)
        print('***')

    #return setpoint
