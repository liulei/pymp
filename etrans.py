#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys

def smooth_e_trans(file_name):

	struct_m_trans = dtype([('time', float), \
				('evap', float), \
				('cond', float), \
				('sn2', float), \
				('pn', float), \
				('sn1', float), \
				('sw', float), \
				('phase', float), \
				('sf', float)])

#	arr_in = loadtxt(file_name, dtype = struct_m_trans)
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
	print 'etrans: not enough parameter!'
	print '\tUsage: ./etrans.py file_name ending_time'
	print '\tExample: ./etrans.py PK-7 1000'
	sys.exit(0)

prefix = '/home/liulei/program/mp-cd-sph/run'

file_in = prefix + '/' + sys.argv[1] + '/energy_trans.dat'

array = smooth_e_trans(file_in)

rc('font', size = 17)

plt.yscale('log')
plt.title(sys.argv[1])
plt.xlabel('Time [Myr]')
plt.ylabel('Energy Transfer Rate [J / Myr]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

plt.plot(array[:, 0], array[:, 1], hold = True)
plt.plot(array[:, 0], array[:, 2], hold = True)
plt.plot(array[:, 0], array[:, 3], hold = True)
plt.plot(array[:, 0], array[:, 4], hold = True)
plt.plot(array[:, 0], array[:, 5] * 1.0E-3, hold = True)
plt.plot(array[:, 0], np.abs(array[:, 7]), hold = True)
plt.plot(array[:, 0], np.abs(array[:, 8]), hold = True)
plt.plot(array[:, 0], array[:, 6], '--', hold = True)

lg = plt.legend(('SNII', 'PN', 'SN1', 'MECH', 'UV', 'COOL', 'PdV', 'COLL'), 
	loc = 0, ncol = 3, prop = {'size' : 17})
lg.get_frame().set_linewidth(0)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(1.0E42, 1.0E49)
figure_name = 'E-TRANS-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)

out_name = sys.argv[1] + '.sme'
f = open(out_name, 'w')
nrow = len(array)
ncol = len(array[0])
for i in range(0, nrow):
    for j in range(0, ncol):
        f.write('%.3E\t' % array[i, j])
    f.write('\n')
f.close()
