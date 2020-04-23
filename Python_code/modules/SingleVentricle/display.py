# Code for displaying single circulation model
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def display_pv_loop(data_structure, output_file_string="", t_limits=[],
                    dpi=None):
    no_of_rows = 1
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([10, 10])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    # Check for t_limits, prune data if necessary
    if t_limits:
        t = data_structure['time']
        vi = np.nonzero((t>=t_limits[0])&(t<=t_limits[1]))
        data_structure = data_structure.iloc[vi]

    ax1 = f.add_subplot(spec2[0, 0])
    ax1.plot('volume_ventricle', 'pressure_ventricle', data=data_structure)
    ax1.set_xlim([0, 1.1*np.max(data_structure['volume_ventricle'])])
    ax1.set_xlabel('Volume (liters)')
    ax1.set_ylabel('Pressure (mm Hg)')

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)
def display_baro_results (data_structure, output_file_string="",dpi=None):
    no_of_rows = 6
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([10, 10])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax1 = f.add_subplot(spec2[0, 0])
    ax1.plot('time','pressure_arteries',data=data_structure)
    #ax1.set_xlabel('time (s)', fontsize = 15)
    ax1.set_ylabel('$P_a (mmHg)$', fontsize = 15)
    ax1.tick_params(labelsize = 15)

    if(hasattr(data_structure,'baroreceptor_output')):
        ax2 = f.add_subplot(spec2[1, 0])
        ax2.plot('time','baroreceptor_output',data=data_structure)
        #ax2.set_xlabel('time (s)', fontsize = 15)
        ax2.set_ylabel('$br$', fontsize = 15)
        ax2.tick_params(labelsize = 15)

    if(hasattr(data_structure,'P_tilda')):
        ax3 = f.add_subplot(spec2[2, 0])
        ax3.plot('time','P_tilda',data=data_structure)
        ax3.set_xlabel('time (s)', fontsize = 15)
        ax3.set_ylabel('P_tilda (mmHg)', fontsize = 15)

        ax4 = f.add_subplot(spec2[3, 0])
        ax4.plot('time','f_cs',data=data_structure)
        ax4.set_xlabel('time (s)', fontsize = 15)
        ax4.set_ylabel('f_cs', fontsize = 15)



    ax3 = f.add_subplot(spec2[2, 0])
    ax3.plot('time','heart_period',data=data_structure)
    #ax3.set_xlabel('time (s)', fontsize = 15)
    ax3.set_ylabel('T (s)', fontsize = 15)
    ax3.tick_params(labelsize = 15)

    ax4 = f.add_subplot(spec2[3, 0])
    ax4.plot('time','heart_rate',data=data_structure)
    #ax4.set_xlabel('time (s)', fontsize = 15)
    ax4.set_ylabel('HR (BPM)', fontsize = 15)
    ax4.tick_params(labelsize = 15)

    ax5=f.add_subplot(spec2[4,0])
    ax5.plot('time','k_1',data=data_structure)
    #ax5.set_xlabel('time (s)', fontsize = 15)
    ax5.set_ylabel('$k_1$', fontsize = 15)
    ax5.tick_params(labelsize = 15)

    ax6=f.add_subplot(spec2[5,0])
    ax6.plot('time','k_3',data=data_structure)
    ax6.set_xlabel('time (s)', fontsize = 15)
    ax6.set_ylabel('$k_3$', fontsize = 15)
    ax6.tick_params(labelsize = 15)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_flows(data_structure, output_file_string="",
                  t_limits=[],dpi=None):

    no_of_rows = 1
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([14, 10])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)
    ax1 = f.add_subplot(spec2[0, 0])
    ax1.plot('time', 'flow_ventricle_to_aorta', data=data_structure,
             label='Ventricle to Aorta')
    ax1.plot('time', 'flow_aorta_to_arteries', data=data_structure,
             label='Aorta to Arteries')
    ax1.plot('time', 'flow_arteries_to_arterioles', data=data_structure,
             label='Arteries to arterioles')
    ax1.plot('time', 'flow_arterioles_to_capillaries', data=data_structure,
             label='Arterioles to capillaries')
    ax1.plot('time', 'flow_capillaries_to_veins', data=data_structure,
             label='Capillaries to Veins')
    ax1.plot('time', 'flow_veins_to_ventricle', data=data_structure,
             label='Veins to Ventricle')
    ax1.legend(bbox_to_anchor=(1.05, 1))
    if t_limits:
        ax1.set_xlim(t_limits)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_simulation(data_structure, output_file_string="", t_limits=[],
                       dpi=None):

    no_of_rows = 10
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    if t_limits:
        time_span = t_limits[1]-t_limits[0]
        plot_width = 46
    else:
        plot_width=46
    f.set_size_inches([10, 15])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)
    ax1 = f.add_subplot(spec2[0, 0])
    ax1.plot('time', 'pressure_aorta', data=data_structure, label='Aorta')
    ax1.plot('time', 'pressure_arteries', data=data_structure, label='Arteries')
    ax1.plot('time', 'pressure_arterioles', data=data_structure, label='Arterioles')
    ax1.plot('time', 'pressure_capillaries', data=data_structure, label='Capillaries')
    ax1.plot('time', 'pressure_veins',  data=data_structure, label='Veins')
    ax1.plot('time', 'pressure_ventricle',  data=data_structure, label='Ventricle')
    ax1.set_ylabel('Pressure (mmHg)', fontsize = 10)
    ax1.tick_params(labelsize = 10)
    if t_limits:
        ax1.set_xlim(t_limits)
    ax1.legend(bbox_to_anchor=(1.05, 1),ncol=2,fontsize = 10)

    ax2 = f.add_subplot(spec2[1, 0])
    ax2.semilogy('time', 'volume_aorta', data=data_structure, label='Aorta')
    ax2.semilogy('time', 'volume_arteries', data=data_structure, label='Arteries')
    ax2.semilogy('time', 'volume_arterioles', data=data_structure, label='Arterioles')
    ax2.semilogy('time', 'volume_capillaries', data=data_structure, label='Capillaries')
    ax2.semilogy('time', 'volume_veins',  data=data_structure, label='Veins')
    ax2.semilogy('time', 'volume_ventricle', data=data_structure, label='Ventricle')
    ax2.set_ylabel('log_{10} Volume', fontsize = 10)
    ax2.tick_params(labelsize = 10)
    if t_limits:
        ax2.set_xlim(t_limits)
    ax2.set_ylim([1e-3, 10])
    ax2.set_yticks(np.array([1e-3, 1e-2, 1e-1, 1, 10]))
    ax2.legend(bbox_to_anchor=(1.05, 1),fontsize = 10, ncol=2)

    ax3 = f.add_subplot(spec2[2, 0])
    ax3.plot('time', 'activation', data=data_structure, label='Activation')
    if t_limits:
        ax3.set_xlim(t_limits)
    ax3.set_ylabel('Activation', fontsize = 10)
    ax3.tick_params(labelsize = 10)
    ax3.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    # Look for membrane voltage
    if ('membrane_voltage' in data_structure.columns):
        ax4 = f.add_subplot(spec2[3, 0])
        ax4.plot('time', 'membrane_voltage', data=data_structure, label='Voltage')
        if t_limits:
            ax4.set_xlim(t_limits)
        ax4.set_ylabel('Membrane\nvoltage\n(V)', fontsize = 10)
        ax4.tick_params(labelsize = 10)
        ax4.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)


    ax5 = f.add_subplot(spec2[4, 0])
    ax5.plot('time', 'Ca_conc', data=data_structure, label='Ca concentration')
    if t_limits:
        ax5.set_xlim(t_limits)
    ax5.set_ylabel('Concentration\n[M]', fontsize = 10)
    ax5.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax5.tick_params(labelsize = 10)
    ax5.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    ax6 = f.add_subplot(spec2[5, 0])
    ax6.plot('time', 'hs_length', data=data_structure, label='hs_length')

    if t_limits:
        ax6.set_xlim(t_limits)
    ax6.set_ylabel('Length (nm)', fontsize = 10)
    ax6.tick_params(labelsize = 10)
    ax6.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    ax7 = f.add_subplot(spec2[6, 0])
    ax7.plot('time', 'hs_force', data=data_structure, label='Total force')
    ax7.plot('time', 'cb_force', data=data_structure, label='Crossbridge force')
    ax7.plot('time', 'pas_force', data=data_structure, label='Passive force')
    if t_limits:
        ax7.set_xlim(t_limits)
    ax7.set_ylabel('Force (N/m2)', fontsize = 10)
    ax7.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax7.tick_params(labelsize = 10)
    ax7.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    ax8 = f.add_subplot(spec2[7, 0])
    ax8.plot('time', 'n_on', data=data_structure, label='N_on')
    ax8.plot('time', 'n_off', data=data_structure, label='N_off')
    ax8.plot('time', 'n_bound', data=data_structure, label='N_bound')
    if t_limits:
        ax8.set_xlim(t_limits)
    ax8.set_ylim([0, 1.0])
    ax8.set_ylabel('Thin filament', fontsize = 10)
    ax8.tick_params(labelsize = 10)
    ax8.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    ax9 = f.add_subplot(spec2[8, 0])
    ax9.plot('time', 'M_OFF', data=data_structure, label='M_OFF')
    ax9.plot('time', 'M_ON', data=data_structure, label='M_ON')
    ax9.plot('time', 'M_bound', data=data_structure, label='M_bound')
    if t_limits:
        ax9.set_xlim(t_limits)
    ax9.set_ylim([0, 1.0])
    ax9.set_ylabel('Thick filament', fontsize = 10)
    ax9.tick_params(labelsize = 10)
    ax9.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    ax10 = f.add_subplot(spec2[9, 0])
    ax10.plot('time', 'volume_ventricle', data=data_structure, label='Ventricle')
    #ax10.plot('time','LVEDV','r-',data=data_structure, label="EDV")
    #ax10.plot('time','LVESV','r-',data=data_structure, label="ESV")
    if t_limits:
        ax10.set_xlim(t_limits)
    ax10.set_ylabel('Volume (ml)', fontsize = 10)
    ax10.tick_params(labelsize = 10)
    ax10.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_simulation_publish(data_structure, output_file_string="", t_limits=[],
                       dpi=None):

    no_of_rows = 8
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    if t_limits:
        time_span = t_limits[1]-t_limits[0]
        plot_width = 46
    else:
        plot_width=46
    f.set_size_inches([10, 15])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax0 = f.add_subplot(spec2[0, 0])
    ax0.plot('time', 'activation', data=data_structure, label='Activation')
    if t_limits:
        ax0.set_xlim(t_limits)
    ax0.set_ylabel('Activation', fontsize = 15)
    ax0.tick_params(labelsize = 15)
    ax0.legend(bbox_to_anchor=(1.05, 1),fontsize = 15)

    if ('membrane_voltage' in data_structure.columns):
        ax1 = f.add_subplot(spec2[1, 0])
        ax1.plot('time', 'membrane_voltage', data=data_structure, label='Voltage')
        if t_limits:
            ax1.set_xlim(t_limits)
        ax1.set_ylabel('Membrane\nvoltage\n(V)', fontsize = 15)
        ax1.tick_params(labelsize = 15)
        ax1.legend(bbox_to_anchor=(1.05, 1),fontsize = 15)

    ax2 = f.add_subplot(spec2[2, 0])
    ax2.plot('time', 'Ca_conc', data=data_structure, label='Ca concentration')
    if t_limits:
        ax2.set_xlim(t_limits)
    ax2.set_ylabel('Concentration\n[M]', fontsize = 15)
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax2.tick_params(labelsize = 15)
    ax2.legend(bbox_to_anchor=(1.05, 1),fontsize = 15)

    ax3 = f.add_subplot(spec2[3, 0])
    ax3.plot('time', 'hs_length', data=data_structure, label='hs_length')

    if t_limits:
        ax3.set_xlim(t_limits)
    ax3.set_ylabel('Length (nm)', fontsize = 15)
    ax3.tick_params(labelsize = 15)
    ax3.legend(bbox_to_anchor=(1.05, 1),fontsize = 15)

    ax4 = f.add_subplot(spec2[4, 0])
    ax4.plot('time', 'hs_force', data=data_structure, label='Total force')
    ax4.plot('time', 'cb_force', data=data_structure, label='Crossbridge force')
    ax4.plot('time', 'pas_force', data=data_structure, label='Passive force')
    if t_limits:
        ax4.set_xlim(t_limits)
    ax4.set_ylabel('Force (N/m2)', fontsize = 15)
    ax4.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax4.tick_params(labelsize = 15)
    ax4.legend(bbox_to_anchor=(1.05, 1),fontsize = 15)

    ax5 = f.add_subplot(spec2[5, 0])
    ax5.plot('time', 'volume_ventricle', data=data_structure, label='Ventricle')
    #ax10.plot('time','LVEDV','r-',data=data_structure, label="EDV")
    #ax10.plot('time','LVESV','r-',data=data_structure, label="ESV")
    if t_limits:
        ax5.set_xlim(t_limits)
    ax5.set_ylabel('Volume (ml)', fontsize = 15)
    ax5.tick_params(labelsize = 15)
    ax5.legend(bbox_to_anchor=(1.05, 1),fontsize = 15)

    ax6 = f.add_subplot(spec2[6, 0])
    ax6.plot('time', 'pressure_aorta', data=data_structure, label='Aorta')
    ax6.plot('time', 'pressure_arteries', data=data_structure, label='Arteries')
    ax6.plot('time', 'pressure_arterioles', data=data_structure, label='Arterioles')
    ax6.plot('time', 'pressure_capillaries', data=data_structure, label='Capillaries')
    ax6.plot('time', 'pressure_veins',  data=data_structure, label='Veins')
    ax6.plot('time', 'pressure_ventricle',  data=data_structure, label='Ventricle')
    ax6.set_ylabel('Pressure (mmHg)', fontsize = 15)
    ax6.tick_params(labelsize = 15)
    if t_limits:
        ax6.set_xlim(t_limits)
    ax6.legend(bbox_to_anchor=(1.05, 1),ncol=2,fontsize = 15)

    ax7 = f.add_subplot(spec2[7, 0])
    ax7.semilogy('time', 'volume_aorta', data=data_structure, label='Aorta')
    ax7.semilogy('time', 'volume_arteries', data=data_structure, label='Arteries')
    ax7.semilogy('time', 'volume_arterioles', data=data_structure, label='Arterioles')
    ax7.semilogy('time', 'volume_capillaries', data=data_structure, label='Capillaries')
    ax7.semilogy('time', 'volume_veins',  data=data_structure, label='Veins')
    ax7.semilogy('time', 'volume_ventricle', data=data_structure, label='Ventricle')
    ax7.set_ylabel('log_{10} Volume', fontsize = 15)
    ax7.tick_params(labelsize = 15)
    if t_limits:
        ax7.set_xlim(t_limits)
    ax7.set_ylim([1e-3, 10])
    ax7.set_yticks(np.array([1e-3, 1e-2, 1e-1, 1, 10]))
    ax7.legend(bbox_to_anchor=(1.05, 1),fontsize = 15, ncol=2)
    ax7.set_xlabel('time (s)',fontsize = 15)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_growth(data_structure, output_file_string="",signal="",
                    t_limits=[],dpi=None):

    no_of_rows = 4
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([7, 5])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,figure=f)

    ax0 = f.add_subplot(spec2[0, 0])
    ax0.plot('time','ventricle_wall_thickness',data=data_structure)
    if t_limits:
        ax0.set_xlim(t_limits)
    ax0.set_ylabel('LVW_t(mm)')#, fontsize = 10)
    ax0.tick_params(labelsize = 10)


    ax1 = f.add_subplot(spec2[1, 0])
    ax1.plot('time','ventricle_wall_volume',data=data_structure)
    if t_limits:
        ax1.set_xlim(t_limits)
    ax1.set_ylabel('LVW vol(ml)')#, fontsize = 10)
    ax1.tick_params(labelsize = 10)

    ax2 = f.add_subplot(spec2[2, 0])
    ax2.plot('time','number_of_hs',data=data_structure)
    if t_limits:
        ax2.set_xlim(t_limits)
    ax2.set_ylabel('NHS')#, fontsize = 10)
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax2.tick_params(labelsize = 10)

    ax3 = f.add_subplot(spec2[3, 0])
    ax3.plot('time','volume_ventricle',data=data_structure)
    if t_limits:
        ax3.set_xlim(t_limits)
    ax3.set_ylabel('LV vol(ml)')#, fontsize = 10)
    ax3.set_xlabel('time (s)')#, fontsize = 10)
    ax3.tick_params(labelsize = 10)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_growth_summary(data_structure, output_file_string="",signal="",
                    t_limits=[],dpi=None):

    no_of_rows = 10
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([46, 28])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,figure=f)
    #gs=f.add_gridspec(3,1)
#    ax1 = f.add_subplot(spec2[0, 0])
#    ax1.plot('time','activation',data=data_structure)
#    ax1.set_xlabel('time (s)')
#    ax1.set_ylabel('Activation')


    ax1 = f.add_subplot(spec2[0, 0])
    #spec21 = gridspec.GridSpec(nrows=2, ncols=1, figure=ax1)

    ax1.plot('time','pressure_arteries',data=data_structure)
    if t_limits:
        ax1.set_xlim(t_limits)
    #ax1.set_xlabel('time (s)', fontsize = 15)
    ax1.set_ylabel('pressure \narteries', fontsize = 20)
    ax1.tick_params(labelsize = 25)
    ax1.set_title('Baroreceptor',fontsize=30,fontweight='bold')

    if(hasattr(data_structure,'heart_period')):

        ax2 = f.add_subplot(spec2[1, 0])
        #ax2.plot('time','heart_period',data=data_structure)
        ax2.plot('time','heart_rate',data=data_structure)
        #ax2.plot('time','cb_force_null',data=data_structure)
        if t_limits:
            ax2.set_xlim(t_limits)
        #ax2.set_xlabel('time (s)', fontsize = 20)
        #ax2.set_ylabel('heart period', fontsize = 20)
        #ax2.set_ylabel('cb force null', fontsize = 20)
        ax2.set_ylabel('heart rate', fontsize = 20)
        ax2.tick_params(labelsize = 25)

    ax3 = f.add_subplot(spec2[2, 0])
    ax3.plot('time','hs_force',data=data_structure, label='hs force')
    #if (signal == "stress"):
        #ax3.plot('time','hs_force_null',data=data_structure, label='hs force null')
    #ax3.set_xlabel('time (s)', fontsize = 20)
    if t_limits:
        ax3.set_xlim(t_limits)
    ax3.set_ylabel('cell force \n(N/m2)', fontsize = 20)
    ax3.ticklabel_format(style='sci', axis='y', scilimits=(0, 0),)
    ax3.tick_params(labelsize = 25)
    ax3.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)


    ax4 = f.add_subplot(spec2[3, 0])

    if (signal == "stress"):
        ax4.plot('time', 'cb_force', data=data_structure, label='cb_force')
        ax4.plot('time','cb_force_null',data=data_structure, label='cb force null')
        ax4.set_ylabel('Active force \n(N/m2)', fontsize = 20)
    elif (signal == "ATPase") :
        ax4.plot('time', 'ATPase', data=data_structure, label='ATPase')
        ax4.plot('time','ATPase_null',data=data_structure, label='ATPase null')
        ax4.set_ylabel('ATPase (kJ)', fontsize = 20)

    if t_limits:
        ax4.set_xlim(t_limits)
    ax4.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax4.tick_params(labelsize = 25)
    ax4.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)
    ax4.set_title('Concnetric growth',fontsize=30,fontweight='bold')

    ax5 = f.add_subplot(spec2[4, 0])
    ax5.plot('time','ventricle_wall_thickness',data=data_structure, label='original')
    #ax5.plot('time','filtered_wall_thickness','r-',data=data_structure, label='filtered')
    if t_limits:
        ax5.set_xlim(t_limits)
    ax5.set_ylabel('wall thickness (m)', fontsize = 20)

    #ax4.set_xlabel('time (s)')
    ax5.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax5.tick_params(labelsize = 25)
    ax5.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax6 = f.add_subplot(spec2[5, 0])
    ax6.plot('time','ventricle_wall_volume',data=data_structure)
    if t_limits:
        ax6.set_xlim(t_limits)
    #ax5.set_xlabel('time (s)', fontsize = 20)
    ax6.set_ylabel('wall volume (L)', fontsize = 20,)
    ax6.tick_params(labelsize = 25)

    if (signal == "strain"):
        ax7 = f.add_subplot(spec2[6, 0])
        ax7.plot('time', 'cell_strain', data=data_structure, label='cell_strain')
        ax7.plot('time', 'cell_strain_null', data=data_structure, label='cell_strain null')
        if t_limits:
            ax7.set_xlim(t_limits)
        #ax9.set_xlabel('time (s)', fontsize = 20)
        ax7.set_ylabel('cell strain', fontsize = 20)
        ax7.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax7.tick_params(labelsize = 25)
        ax7.legend(bbox_to_anchor=(1.05, 1))



    ax7 = f.add_subplot(spec2[6, 0])
    ax7.plot('time', 'pas_force', data=data_structure, label='Passive force')
    if (signal == "stress"):
        ax7.plot('time', 'pas_force_null', data=data_structure, label='Passive force null')

    #ax6.set_xlabel('time (s)', fontsize = 15)
    if t_limits:
        ax7.set_xlim(t_limits)
    ax7.set_ylabel('Passive force \n(N/m2)', fontsize = 20)
    ax7.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax7.tick_params(labelsize = 25)
    ax7.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)
    ax7.set_title('Eccentric growth',fontsize=30,fontweight='bold')

    ax8 = f.add_subplot(spec2[7, 0])
    ax8.plot('time','number_of_hs',data=data_structure,label='original')
    #ax9.plot('time','filtered_n_hs','r-',data=data_structure,label='filtered')
    if t_limits:
        ax8.set_xlim(t_limits)
    ax8.set_ylabel('number of \n half_sarcomeres', fontsize = 20)
    ax8.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax8.tick_params(labelsize = 25)
    ax8.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax9 = f.add_subplot(spec2[8, 0])
    #ax9.plot('time', 'hs_length', data=data_structure, label='hs length')
    ax9.plot('time', 'pas_force_null', data=data_structure, label='Passive force null')
    #ax9.plot('time', 'cell_strain_null', data=data_structure, label='cell_strain null')
        #ax9.set_xlabel('time (s)', fontsize = 15)
    if t_limits:
        ax9.set_xlim(t_limits)
    ax9.set_ylabel('Passive force null', fontsize = 20)
    ax9.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax9.tick_params(labelsize = 25)
    ax9.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax10 = f.add_subplot(spec2[9, 0])
    ax10.plot('time','volume_ventricle',data=data_structure)
    ax10.plot('time','LVEDV',data=data_structure)
    ax10.plot('time','LVESV',data=data_structure)
    if t_limits:
        ax10.set_xlim(t_limits)
    ax10.set_xlabel('time (s)', fontsize = 20)
    ax10.set_ylabel('ventricle volume \n(L)', fontsize = 20)
    ax10.tick_params(labelsize = 25)


    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_circulatory(data_structure, output_file_string="", t_limits=[],
                       dpi=None):
    no_of_rows = 4
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    if t_limits:
        time_span = t_limits[1]-t_limits[0]
        plot_width = 46
    else:
        plot_width=46
    f.set_size_inches([plot_width, 20])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)
    ax1 = f.add_subplot(spec2[0, 0])
    ax1.plot('time', 'pressure_aorta', data=data_structure, label='Aorta')
#    ax1.plot('time', 'pressure_arteries', data=data_structure, label='Arteries')
    ax1.plot('time', 'pressure_arterioles', data=data_structure, label='Arterioles')
    ax1.plot('time', 'pressure_capillaries', data=data_structure, label='Capillaries')
    ax1.plot('time', 'pressure_veins',  data=data_structure, label='Veins')
    ax1.plot('time', 'pressure_ventricle',  data=data_structure, label='Ventricle')
    ax1.set_ylabel('Pressure', fontsize = 30)
    ax1.tick_params(labelsize = 30)
    if t_limits:
        ax1.set_xlim(t_limits)
    ax1.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax2 = f.add_subplot(spec2[1, 0])
    ax2.semilogy('time', 'volume_aorta', data=data_structure, label='Aorta')
    ax2.semilogy('time', 'volume_arteries', data=data_structure, label='Arteries')
    ax2.semilogy('time', 'volume_arterioles', data=data_structure, label='Arterioles')
    ax2.semilogy('time', 'volume_capillaries', data=data_structure, label='Capillaries')
    ax2.semilogy('time', 'volume_veins',  data=data_structure, label='Veins')
    ax2.semilogy('time', 'volume_ventricle', data=data_structure, label='Ventricle')
    ax2.set_ylabel('Volume', fontsize = 30)
    ax2.tick_params(labelsize = 30)
    if t_limits:
        ax2.set_xlim(t_limits)
    ax2.set_ylim([1e-2, 10])
    #ax2.set_yticks(np.array([1e-3, 1e-2, 1e-1, 1, 10]))
    ax2.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax3 = f.add_subplot(spec2[2, 0])
    ax3.plot('time', 'volume_aortic_regurgitation', data=data_structure, label='Aorta')
    ax3.plot('time', 'volume_mitral_regurgitation', data=data_structure, label='Mitral')
    ax3.set_ylabel('Volume (ml)', fontsize = 30)
    ax3.tick_params(labelsize = 30)
    if t_limits:
        ax2.set_xlim(t_limits)
    #ax3.set_ylim([1e-2, 10])
    #ax2.set_yticks(np.array([1e-3, 1e-2, 1e-1, 1, 10]))
    ax3.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax4 = f.add_subplot(spec2[3, 0])
    ax4.plot('time', 'flow_ventricle_to_aorta', data=data_structure,
             label='Ventricle to Aorta')
#    ax3.plot('time', 'flow_aorta_to_arteries', data=data_structure,
#             label='Aorta to Arteries')
#    ax3.plot('time', 'flow_arteries_to_arterioles', data=data_structure,
#             label='Arteries to arterioles')
#    ax3.plot('time', 'flow_arterioles_to_capillaries', data=data_structure,
#             label='Arterioles to capillaries')
    ax4.plot('time', 'flow_capillaries_to_veins', data=data_structure,
             label='Capillaries to Veins')
    ax4.plot('time', 'flow_veins_to_ventricle', data=data_structure,
             label='Veins to Ventricle')
    ax4.set_ylabel('Flows',fontsize =30)
    ax4.tick_params(labelsize = 30)
    ax4.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)
    if t_limits:
        ax4.set_xlim(t_limits)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_active_force(data_structure, output_file_string="", t_limits=[],
                       dpi=None):

    no_of_rows = 5
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    if t_limits:
        time_span = t_limits[1]-t_limits[0]
        plot_width = 46
    else:
        plot_width=46
    f.set_size_inches([plot_width, 20])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax2 = f.add_subplot(spec2[0, 0])
    ax2.plot('time', 'hs_length', data=data_structure, label='hs_length')

    if t_limits:
        ax2.set_xlim(t_limits)
    ax2.set_ylabel('Length', fontsize = 30)
    ax2.tick_params(labelsize = 30)
    ax2.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax3 = f.add_subplot(spec2[1, 0])
    ax3.plot('time', 'N_overlap', data=data_structure, label='N_overlap')

    if t_limits:
        ax3.set_xlim(t_limits)
    ax3.set_ylabel('Half sarcomere', fontsize = 30)
    ax3.tick_params(labelsize = 30)
    ax3.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax4 = f.add_subplot(spec2[2, 0])
    ax4.plot('time', 'n_on', data=data_structure, label='N_on')
    ax4.plot('time', 'n_off', data=data_structure, label='N_off')
    ax4.plot('time', 'n_bound', data=data_structure, label='N_bound')
    if t_limits:
        ax4.set_xlim(t_limits)
    ax4.set_ylim([0, 1.0])
    ax4.set_ylabel('Thin filament', fontsize = 30)
    ax4.tick_params(labelsize = 30)
    ax4.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax5 = f.add_subplot(spec2[3, 0])
    ax5.plot('time', 'M_OFF', data=data_structure, label='M_OFF')
    ax5.plot('time', 'M_ON', data=data_structure, label='M_ON')
    ax5.plot('time', 'M_bound', data=data_structure, label='M_bound')
    if t_limits:
        ax5.set_xlim(t_limits)
    ax5.set_ylim([0, 1.0])
    ax5.set_ylabel('Thick filament', fontsize = 30)
    ax5.tick_params(labelsize = 30)
    ax5.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax6 = f.add_subplot(spec2[4, 0])
    #ax7.plot('time', 'hs_force', data=data_structure, label='Total force')
    ax6.plot('time', 'cb_force', data=data_structure, label='Crossbridge force')
    #ax7.plot('time', 'pas_force', data=data_structure, label='Passive force')
    if t_limits:
        ax6.set_xlim(t_limits)
    ax6.set_ylabel('Force', fontsize = 30)
    ax6.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax6.tick_params(labelsize = 30)
    ax6.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_systolic_function(data_structure, output_file_string="", t_limits=[],
                       dpi=None):

    no_of_rows = 4
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([7, 5])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    if(hasattr(data_structure,'heart_period')):
        ax0 = f.add_subplot(spec2[0, 0])
        ax0.plot('time','heart_rate',data=data_structure)
        if t_limits:
            ax0.set_xlim(t_limits)
        ax0.set_ylabel('HR', fontsize = 10)
        #ax0.tick_params(labelsize = 25)

    ax1 = f.add_subplot(spec2[1, 0])
    ax1.plot('time', 'stroke_volume', data=data_structure, label='SV')
    if t_limits:
        ax1.set_xlim(t_limits)
    ax1.set_ylabel('SV ($ml$)', fontsize = 10)

    """ax2 = f.add_subplot(spec2[2, 0])
    ax2.plot('time', 'cardiac_output', data=data_structure, label='CO')
    if t_limits:
        ax2.set_xlim(t_limits)
    ax2.set_ylabel('CO ($ml/min$)', fontsize = 10)"""


    ax3 = f.add_subplot(spec2[2, 0])
    ax3.plot('time', 'ejection_fraction', data=data_structure, label='EF')
    if t_limits:
        ax3.set_xlim(t_limits)
    ax3.set_ylabel('EF (%)', fontsize = 10)
    ax3.set_xlabel('time (s)', fontsize = 10)



    #if data_structure["mitral_regurgitant_volume"][-1] != 0:
    ax4 = f.add_subplot(spec2[3, 0])
    ax4.plot('time', 'mitral_regurgitant_volume', data=data_structure, label='MRV')
    if t_limits:
        ax4.set_xlim(t_limits)
    ax4.set_ylabel('MRV ($ml$)', fontsize = 10)
    ax4.set_xlabel('time (s)', fontsize = 10)
    #if data_structure["aortic_regurgitant_volume"][-1] != 0:
#    ax4 = f.add_subplot(spec2[4, 0])
#    ax4.plot('time', 'aortic_regurgitant_volume', data=data_structure, label='ARV')
#    if t_limits:
#        ax4.set_xlim(t_limits)
#    ax4.set_ylabel('ARV ($ml$)', fontsize = 10)
#    ax4.set_xlabel('time (s)', fontsize = 10)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_regurgitation(data_structure, output_file_string="", t_limits=[],
                       dpi=None):
    no_of_rows = 2
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([10, 5])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)
    ax0 = f.add_subplot(spec2[0, 0])
    ax0.plot('time', 'mitral_regurgitant_volume', data=data_structure, label='MRV')
    if t_limits:
        ax0.set_xlim(t_limits)
    ax0.set_ylabel('MRV (L)', fontsize = 10)

    ax1 = f.add_subplot(spec2[1, 0])
    ax1.plot('time', 'aortic_regurgitant_volume', data=data_structure, label='ARV')
    if t_limits:
        ax1.set_xlim(t_limits)
    ax1.set_ylabel('ARV (L)', fontsize = 10)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_ventricular_dimensions(data_structure, output_file_string="", t_limits=[],
                       dpi=None):
    no_of_rows = 7
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([7, 10])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax0 = f.add_subplot(spec2[0, 0])
    ax0.plot('time','LVEDV',data=data_structure)
    if t_limits:
        ax0.set_xlim(t_limits)
    ax0.set_ylabel('LVEDV ($ml$)', fontsize = 10)
    #ax0.tick_params(labelsize = 25)

    ax1 = f.add_subplot(spec2[1, 0])
    ax1.plot('time','LVEDVi',data=data_structure)
    if t_limits:
        ax1.set_xlim(t_limits)
    ax1.set_ylabel('LVEDVi ($ml/m^2$)', fontsize = 10)
    #ax1.tick_params(labelsize = 25)

    ax2 = f.add_subplot(spec2[2, 0])
    ax2.plot('time','LVESV',data=data_structure)
    if t_limits:
        ax2.set_xlim(t_limits)
    ax2.set_ylabel('LVESV ($ml$)', fontsize = 10)
    #ax2.tick_params(labelsize = 25)

    ax3 = f.add_subplot(spec2[3, 0])
    ax3.plot('time','LVESVi',data=data_structure)
    if t_limits:
        ax3.set_xlim(t_limits)
    ax3.set_ylabel('LVESVi ($ml/m^2$)', fontsize = 10)
    #ax3.tick_params(labelsize = 25)

    ax4 = f.add_subplot(spec2[4, 0])
    ax4.plot('time','ventricle_wall_thickness',data=data_structure)
    if t_limits:
        ax4.set_xlim(t_limits)
    ax4.set_ylabel('LVW_t(mm)', fontsize = 10)
    ax4.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    #ax4.tick_params(labelsize = 10)
    #ax4.legend(bbox_to_anchor=(1.05, 1),fontsize = 20)

    ax5=f.add_subplot(spec2[5,0])
    #ax5.plot('time','ventricle_wall_mass',data=data_structure, label="LVM")
    ax5.plot('time','ventricle_wall_mass_mean',data=data_structure, label="mean")
    if t_limits:
        ax5.set_xlim(t_limits)
    ax5.set_ylabel('LVM ($g$)', fontsize = 10)

    ax6=f.add_subplot(spec2[6,0])
    #ax6.plot('time','ventricle_wall_mass_i',data=data_structure, label="LVMi")
    ax6.plot('time','ventricle_wall_mass_i_mean',data=data_structure, label="mean")
    if t_limits:
        ax6.set_xlim(t_limits)
    ax6.set_ylabel('LVMi ($g/m^2$)', fontsize = 10)
    ax6.set_xlabel('time (s)', fontsize = 10)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)
def display_ATPase(data_structure, output_file_string="", t_limits=[],
                       dpi=None):
    no_of_rows = 1
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([7, 3])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax0=f.add_subplot(spec2[0,0])
    ax0.plot('time','ATPase',data=data_structure)
    if t_limits:
        ax0.set_xlim(t_limits)
    ax0.set_ylabel('ATPase ($kJ / s$)', fontsize = 10)
    ax0.set_xlabel('time (s)', fontsize = 10)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def display_Ca(data_structure, output_file_string="", t_limits=[],
                       dpi=None):
    no_of_rows = 2
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([7, 5])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax0 = f.add_subplot(spec2[0, 0])
    ax0.plot('time', 'membrane_voltage', data=data_structure, label='Voltage')
    if t_limits:
        ax0.set_xlim(t_limits)
    ax0.set_ylabel('Membrane\nvoltage\n(V)', fontsize = 10)
    ax0.tick_params(labelsize = 10)
    #ax0.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)

    ax1 = f.add_subplot(spec2[1, 0])
    ax1.plot('time', 'Ca_conc', data=data_structure, label='Ca concentration')
    if t_limits:
        ax1.set_xlim(t_limits)
    ax1.set_ylabel('Ca Concentration\n[M]', fontsize = 10)
    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax1.tick_params(labelsize = 10)
    #ax1.legend(bbox_to_anchor=(1.05, 1),fontsize = 10)
    ax1.set_xlabel('time (s)', fontsize = 10)

    if (output_file_string):
        save_figure_to_file(f, output_file_string, dpi)

def save_figure_to_file(f, im_file_string, dpi=None, verbose=1):
    # Writes an image to file

    import os
    from skimage.io import imsave

    # Check directory exists and save image file
    dir_path = os.path.dirname(im_file_string)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    if (verbose):
        print('Saving figure to to %s' % im_file_string)

    f.savefig(im_file_string, dpi=dpi)
