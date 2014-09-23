#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

def smooth_array(file_name):

	arr_in = loadtxt(file_name, dtype = float, skiprows = 1)
	
	nrow = len(arr_in)
	ncol = len(arr_in[0])
	print nrow, len(arr_in[0])
	di = 50
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

arr10 = smooth_array('drag_1.0.dat')
arr01 = smooth_array('drag_0.1.dat')

t01 = np.copy(arr01[:, 0])
t10 = np.copy(arr10[:, 0])
# recorded are momentum transfer for one timestep (dt = 0.01 Myr)
# transfer to per Myr
arr01 *= 100.0
arr10 *= 100.0

nullFormatter = ticker.NullFormatter()
yFormatter = ticker.FormatStrFormatter('%.0E')

xrange = 100.0
yrange = 2E7

rc('font', size = 15)
fig = plt.figure()
plt.subplots_adjust(left = 0.17, right = 0.95, top = 0.95, bottom = 0.10)

################################## X direction ############################
ax = fig.add_subplot(111)
plt.plot(t01, arr01[:, 1], 'g--', label = 'C$_\mathsf{drag}$ = 0.1, cold')
plt.plot(t01, arr01[:, 4], 'r--', label = 'C$_\mathsf{drag}$ = 0.1, hot')

plt.plot(t10, arr10[:, 1], 'g-', label = 'C$_\mathsf{drag}$ = 1.0, cold')
plt.plot(t10, arr10[:, 4], 'r-', label = 'C$_\mathsf{drag}$ = 1.0, hot')

lg = plt.legend(ncol = 1, loc = 1, prop = {'size': 13})
lg.get_frame().set_linewidth(0)

#ax.xaxis.set_major_formatter(nullFormatter)
ax.yaxis.set_major_formatter(yFormatter)
plt.ylabel('X Momentum [M$_\odot$km/s/Myr]')
plt.xlabel('Time [Myr]')

plt.xlim(0, xrange)
plt.ylim(-yrange, yrange)

plt.savefig('momentum_X.eps')

rc('font', size = 15)
fig = plt.figure()
plt.subplots_adjust(left = 0.17, right = 0.95, top = 0.95, bottom = 0.10)

################################## Z direction ############################
ax = fig.add_subplot(111)
plt.plot(t01, arr01[:, 3], 'g--', label = 'C$_\mathsf{drag}$ = 0.1, cold')
plt.plot(t01, arr01[:, 6], 'r--', label = 'C$_\mathsf{drag}$ = 0.1, hot')

plt.plot(t10, arr10[:, 3], 'g-', label = 'C$_\mathsf{drag}$ = 1.0, cold')
plt.plot(t10, arr10[:, 6], 'r-', label = 'C$_\mathsf{drag}$ = 1.0, hot')

lg = plt.legend(ncol = 1, loc = 1, prop = {'size': 13})
lg.get_frame().set_linewidth(0)

#ax.xaxis.set_major_formatter(nullFormatter)
ax.yaxis.set_major_formatter(yFormatter)
plt.ylabel('Z Momentum [M$_\odot$km/s/Myr]')
plt.xlabel('Time [Myr]')

plt.xlim(0, xrange)
plt.ylim(-yrange, yrange)

plt.savefig('momentum_Z.eps')
