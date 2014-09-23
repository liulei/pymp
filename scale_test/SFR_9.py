#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import mp

def smooth_m_trans(file_name):

    arr_in = np.loadtxt(file_name, dtype = float)
    nrow = len(arr_in)
    ncol = len(arr_in[0])
    print nrow, len(arr_in[0])
    di = 10
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


rc('font', size = 18)

plt.yscale('log')
plt.title('$2\\times10^{9} \mathsf{M}_\odot$', fontsize = 18)
plt.xlabel('Time [Myr]')
plt.ylabel('Star Formation Rate [M$_\odot$ / Year]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

file_in = mp.prefix + '/' + 'hdt-91.1' + '/mass_trans.dat'
array = smooth_m_trans(file_in)
plt.plot(array[:, 0], array[:, 8] / 1.0E6, 'k-', label = '1 node')

file_in = mp.prefix + '/' + 'hdt-91.2' + '/mass_trans.dat'
array = smooth_m_trans(file_in)
plt.plot(array[:, 0], array[:, 8] / 1.0E6, 'y-', label = '2 nodes')

file_in = mp.prefix + '/' + 'hdt-91.4' + '/mass_trans.dat'
array = smooth_m_trans(file_in)
plt.plot(array[:, 0], array[:, 8] / 1.0E6, 'r-', label = '4 nodes')

file_in = mp.prefix + '/' + 'hdt-91.8' + '/mass_trans.dat'
array = smooth_m_trans(file_in)
plt.plot(array[:, 0], array[:, 8] / 1.0E6, 'c-', label = '8 nodes')

file_in = mp.prefix + '/' + 'hdt-91.16' + '/mass_trans.dat'
array = smooth_m_trans(file_in)
plt.plot(array[:, 0], array[:, 8] / 1.0E6, 'm-', label = '16 nodes')

lg = plt.legend(loc = 4, prop = {'size': 16})
lg.get_frame().set_linewidth(0)

plt.xlim(0, 500)
plt.ylim(0.01, 2)
figure_name = 'SFR-91.eps'
plt.savefig(figure_name)
