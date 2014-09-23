#!/usr/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

#dir_name = 'hd-1'
#base_name = '1E3'
#snap_num = '0001'
#nproc = 1

if len(sys.argv) < 6:
	print 'snapp: not enough parameter!'
	print '\tUsage: snapp.py dir_name base_name snap_num nproc range'
	print '\tExample: snapp.py hd-1 1E3 0001 1 20.0'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])
size = float(sys.argv[5])

ntot = 0
ntot, arr = mp.read_dump_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

x = arr['pos'][:, 0]
y = arr['pos'][:, 1]
z = arr['pos'][:, 2]

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)
ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

rc('font', size = 17)
width, height = rcParams['figure.figsize']
sz = min(width, height)

plt.figure(figsize = (sz, sz))
plt.xlabel('X [kpc]')
plt.ylabel('Z [kpc]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.13)

plt.plot(x[idw], z[idw], 'r,', markersize = 1, hold = True)
plt.plot(x[idc], z[idc], 'g,', markersize = 1, hold = True)
plt.plot(x[ids], z[ids], 'b,', markersize = 1, hold = True)

plt.xlim(-size, size)
plt.ylim(-size, size)

figure_name = 'snap-xz-' + dir_name + '-' + base_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)

######################## X-Y #################################################

plt.clf()
plt.figure(figsize = (sz, sz))
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.13)

plt.plot(x[idw], y[idw], 'r,', markersize = 1, hold = True)
plt.plot(x[idc], y[idc], 'g,', markersize = 1, hold = True)
plt.plot(x[ids], y[ids], 'b,', markersize = 1, hold = True)

plt.xlim(-size, size)
plt.ylim(-size, size)

figure_name = 'snap-xy-' + dir_name + '-' + base_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
