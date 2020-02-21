# Code for displaying baroreceptor model
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np




def display_baro_results (data_structure, output_file_string="",dpi=None):

    no_of_rows = 5
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([14, 14])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,
                              figure=f)

    ax1 = f.add_subplot(spec2[0, 0])
    ax1.plot('time','pressure_arteries',data=data_structure)
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('arterial_pressure (mmHg)')

    ax2 = f.add_subplot(spec2[1, 0])
    ax2.plot('time','baroreceptor_output',data=data_structure)
    ax2.set_xlabel('time (s)')
    ax2.set_ylabel('baroreceptor_output')

    #ax3 = f.add_subplot(spec2[2, 0])
    #ax3.plot('time','P_tilda',data=data_structure)
    #ax3.set_xlabel('time (s)')
    #ax3.set_ylabel('P_tilda (mmHg)')

    #ax4 = f.add_subplot(spec2[3, 0])
    #ax4.plot('time','f_cs',data=data_structure)
    #ax4.set_xlabel('time (s)')
    #ax4.set_ylabel('f_cs')

    ax5 = f.add_subplot(spec2[2, 0])
    ax5.plot('time','heart_period',data=data_structure)
    ax5.set_xlabel('time (s)')
    ax5.set_ylabel('heart period (s)')

    ax6=f.add_subplot(spec2[3,0])
    ax6.plot('time','k_1',data=data_structure)
    ax6.set_xlabel('time (s)')
    ax6.set_ylabel('k_1')

    ax7=f.add_subplot(spec2[4,0])
    ax7.plot('time','k_3',data=data_structure)
    ax7.set_xlabel('time (s)')
    ax7.set_ylabel('k_3')

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
