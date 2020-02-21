# Code for displaying growth model
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def display_growth(data_structure, output_file_string="", t_limits=[],dpi=None):

    no_of_rows = 3
    no_of_cols = 1

    f = plt.figure(constrained_layout=True)
    f.set_size_inches([14, 6])
    spec2 = gridspec.GridSpec(nrows=no_of_rows, ncols=no_of_cols,figure=f)

    ax1 = f.add_subplot(spec2[0, 0])
    ax1.plot('time','activation',data=data_structure)
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('Activation')

    ax2 = f.add_subplot(spec2[1, 0])
    ax2.plot('time','hs_force',data=data_structure)
    ax2.set_xlabel('time (s)')
    ax2.set_ylabel('hs_force (KN/m2)')

    ax3 = f.add_subplot(spec2[2, 0])
    ax3.plot('time','average_force',data=data_structure)
    ax3.set_xlabel('time (s)')
    ax3.set_ylabel('average_force (KN/m2)')

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
