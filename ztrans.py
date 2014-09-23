#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

def smooth_m_trans(file_name):

    arr_in = loadtxt(file_name, dtype = float)
    
    nrow = len(arr_in)
    ncol = len(arr_in[0])
    print nrow, len(arr_in[0])
    di = 20
    ns = nrow / di

    arr_out = zeros((ns, ncol))
    
    id = 0
    for i in range(0, nrow):
        if(i % di == 0 and i + di - 1 < nrow):
            for j in range(0, di):
                arr_out[id, :] += arr_in[i + j, :]
            arr_out[id] /= di
            id += 1
    
    return arr_out

if len(sys.argv) < 3:
    print 'ztrans: not enough parameter!'
    print '\tUsage: ./ztrans.py file_name ending_time'
    print '\tExample: ./ztrans.py PK-7 1000'
    sys.exit(0)

file_in = prefix + '/' + sys.argv[1] + '/Z_trans.dat'

array = smooth_m_trans(file_in)

rc('font', size = 17)

plt.yscale('log')
plt.title(sys.argv[1])
plt.xlabel('Time [Myr]')
plt.ylabel('Metal Transfer Rate [M$_\odot$ / Myr]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

plt.plot(array[:, 0], array[:, 1], hold = True)
plt.plot(array[:, 0], array[:, 2], hold = True)
plt.plot(array[:, 0], array[:, 3], hold = True)
plt.plot(array[:, 0], array[:, 4], hold = True)
plt.plot(array[:, 0], array[:, 5], hold = True)
plt.plot(array[:, 0], array[:, 6], hold = True)
plt.plot(array[:, 0], array[:, 7], hold = True)
plt.plot(array[:, 0], array[:, 8], hold = True)

lg = plt.legend(('SNII_Fe', 'PN_Fe', 'SN1_Fe', 'SW_Fe', 'SNII_O', 'PN_O', 'SN1_O', 'SW_O'), 
    loc = 0, ncol = 2, prop = {'size' : 17})
lg.get_frame().set_linewidth(0)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(0.01, 1.0E8)
figure_name = 'Z-TRANS-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)
