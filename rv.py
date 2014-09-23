#!/usr/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys


if len(sys.argv) < 4:
	print 'rv: not enough parameter!'
	print '\tUsage: rv.py dir_name snap_num radius'
	print '\tExample: rv.py PK-7 0005 50'
	sys.exit(0)

dir_name = sys.argv[1]
snap_num = sys.argv[2]
rsize = float(sys.argv[3])

ntot, arr = mp.read_single(mp.prefix, dir_name, snap_num)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
	+ arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r)

v = arr['vel'][:, 0] * arr['vel'][:, 0] + arr['vel'][:, 1] * arr['vel'][:, 1] \
	+ arr['vel'][:, 2] * arr['vel'][:, 2]

v = np.sqrt(v)

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)
ids = np.where(arr['type'] == mp.TYPE_STAR_SINGLE)

rc('font', size = 17)

plt.title(dir_name + ' ' + snap_num)

plt.xlabel('Radius [kpc]')
plt.ylabel('Total velocity [km/s]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

print 'len of r:', len(r)
print 'len of v:', len(v)

#plt.scatter(r[idw], v[idw], s = 1, c = 'r', edgecolors = 'none')
plt.scatter(r[idc], v[idc], s = 1, c = 'g', edgecolors = 'none')
plt.scatter(r[ids], v[ids], s = 1, c = 'b', edgecolors = 'none')

plt.xlim(0, rsize)
plt.ylim(0.0, 150.0)

eps_name = 'r-totalv-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(eps_name)

