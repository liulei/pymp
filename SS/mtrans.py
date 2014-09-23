#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys

def smooth_m_trans(file_name):

    struct_m_trans = dtype([('time', float), \
                ('evap', float), \
                ('cond', float), \
                ('sn2', float), \
                ('pn', float), \
                ('sn1', float), \
                ('sw', float), \
                ('phase', float), \
                ('sf', float)])

#   arr_in = loadtxt(file_name, dtype = struct_m_trans)
    arr_in = loadtxt(file_name, dtype = float)
    
    nrow = len(arr_in)
    ncol = len(arr_in[0])
    print nrow, len(arr_in[0])
    di = 200
#    di = 1
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
    print 'mtrans: not enough parameter!'
    print '\tUsage: ./mtrans.py file_name ending_time'
    print '\tExample: ./mtrans.py PK-7 1000'
    sys.exit(0)

print("Hello from Lei's Python script!")

prefix = '/export/home/liulei/program/mp-cd-sph/run'

file_in = prefix + '/' + sys.argv[1] + '/out/mass_trans.dat'

array = smooth_m_trans(file_in)

rc('font', size = 15)

plt.yscale('log')
#plt.title(sys.argv[1])
plt.xlabel('Time [Myr]')
plt.ylabel('Mass Transfer Rate [M$_\odot$ / Myr]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.12)

plt.plot(array[:, 0], array[:, 3], 'b-', hold = True, label = 'SNII')
plt.plot(array[:, 0], array[:, 4], 'g-', hold = True, label = 'PN')
plt.plot(array[:, 0], array[:, 5], 'r-', hold = True, label = 'SNIa')
plt.plot(array[:, 0], array[:, 6], 'y-', hold = True, label = 'SW')
plt.plot(array[:, 0], np.abs(array[:, 1]), 'c-', hold = True, label = 'EVAP')
plt.plot(array[:, 0], array[:, 2], 'k-', hold = True, label = 'COND')
plt.plot(array[:, 0], array[:, 7], 'c--', hold = True, label = 'C2W')
plt.plot(array[:, 0], array[:, 8], 'k--', hold = True, label = 'TRANSIT')

lg = plt.legend(loc = 0, ncol = 4, prop = {'size' : 15})
lg.get_frame().set_linewidth(0)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(1.0E-3, 1.0E7)
figure_name = 'M-TRANS-' + sys.argv[1] + '.png'
plt.savefig(figure_name)
figure_name = 'M-TRANS-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)
