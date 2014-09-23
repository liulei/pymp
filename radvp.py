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
	print 'radv_paral: not enough parameter!'
	print '\tUsage: radv_paral.py dir_name base_name snap_num nproc radius'
	print '\tExample: radv_paral.py hd-1 1E3 0001 1 20.0'

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])
rsize = float(sys.argv[5])

ntot = 0
ntot, arr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
	+ arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r)

v = arr['pos'][:, 0] * arr['vel'][:, 0] + arr['pos'][:, 1] * arr['vel'][:, 1] \
	+ arr['pos'][:, 2] * arr['vel'][:, 2]

v /= r

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)

rc('font', size = 17)

plt.xlabel('Radius [kpc]')
plt.ylabel('Radial Velocity [km/s]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

print 'len of r:', len(r)
print 'len of v:', len(v)

plt.plot(r[idw], v[idw], 'r,', markersize = 1, hold = True)
plt.plot(r[idc], v[idc], 'g,', hold = True)

plt.xlim(0, rsize)
plt.ylim(-100.0, 600.0)

figure_name = 'r-v-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
