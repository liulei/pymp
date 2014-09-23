#!/export/home/liulei/local/bin/python

import matplotlib.pyplot as plt
import sys
import mp
from numpy import *
#import numpy as np
from matplotlib import *

def smooth_m_trans(file_name):

    arr_in = loadtxt(file_name, dtype = float)
    
    nrow = len(arr_in)
    ncol = len(arr_in[0])
    print nrow, len(arr_in[0])
    di = 200
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

dirs = ['101-hd-3Hs2', '91-hd-3Hs2', '81-hd-3Hs2', '100-hd-3Hs2', '90-hd-3Hs2', '80-hd-3Hs2']
ls = ['r-', 'c-', 'm-', 'r--', 'c--', 'm--']

#dirs = ['101-1', '100-1', '91-1', '90-1' ]
#ls = ['r-', 'r--', 'c-', 'c--' ]


rc('font', size = 20)

plt.yscale('log')
plt.title('Star Formation Rate Comparison')
plt.xlabel('Time [Myr]')
plt.ylabel('Star Formation Rate [M$_\odot$ / Year]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

for i in range(0, 6):
    file_in = mp.prefix + '/' + dirs[i] + '/out/mass_trans.dat'
    array = smooth_m_trans(file_in)
    plt.plot(array[:, 0], array[:, -1] / 1.0E6, ls[i])


plt.xlim(0, 2000)
plt.ylim(0.001, 200)

lg = plt.legend(('$2\\times10^{10} \mathsf{M}_\odot$', \
                '$2\\times10^{9} \mathsf{M}_\odot$', \
                '$2\\times10^{8} \mathsf{M}_\odot$', \
                '$2\\times10^{10} \mathsf{M}_\odot$ (no spin)', \
                '$2\\times10^{9} \mathsf{M}_\odot$ (no spin)', \
                '$2\\times10^{8} \mathsf{M}_\odot$ (no spin)'), \
                loc = 0, ncol = 2, prop = {'size': 13})
lg.get_frame().set_linewidth(0)
figure_name = 'SFR_six_models.png'
plt.savefig(figure_name)
figure_name = 'SFR_six_models.eps'
plt.savefig(figure_name)
