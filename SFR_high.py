#!/usr/bin/python

from numpy import *
#import numpy as np
from mp import *
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
	print 'SFR: not enough parameter!'
	print '\tUsage: ./SFR.py file_name ending_time'
	print '\tExample: ./SFR.py PK-7 1000'
	sys.exit(0)

print("Hello from Lei's Python script!")

file_in = prefix + '/' + sys.argv[1] + '/mass_trans.dat'

array = smooth_m_trans(file_in)

print array[: , 0]
print array[: , 8]

print 'length of file: %d' %(len(array))

rc('font', size = 20)

plt.yscale('log')
plt.title(sys.argv[1])
plt.xlabel('Time [Myr]')
plt.ylabel('Star Formation Rate [M$_\odot$ / Year]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)
plt.plot(array[:, 0], array[:, 8] / 1.0E6, '-', color = 'r')
plt.xlim(0, float(sys.argv[2]))
plt.ylim(0.1, 100)
figure_name = 'SFR-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)
