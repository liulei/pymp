#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys
import mp

if len(sys.argv) < 6:
	print 'roxyp: not enough parameter!'
	print '\tUsage: roxyp.py dir_name base_name snap_num nproc radius'
	print '\tExample: roxyp hd-1 1E3 0001 1 20.0'
	sys.exit(0)

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

Oxy = np.log10(arr['mass_Z'][:, mp.ID_O] / arr['mass_Z'][:, mp.ID_H] / 16.0) \
	- 8.9 + 12.0

Fe = np.log10(arr['mass_Z'][:, mp.ID_Fe] / arr['mass_Z'][:, mp.ID_H] / 56.0) \
	- 7.55 + 12.0

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)
ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

rc('font', size = 17)

plt.xlabel('Radius [kpc]')
plt.ylabel('Oxygen Abundance')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

print 'len of r:', len(r)

plt.plot(r[idw], Oxy[idw], 'r,', markersize = 1, hold = True)
#plt.plot(r[idc], Oxy[idc], 'g,', markersize = 1, hold = True)
#plt.plot(r[ids], Oxy[ids], 'b,', markersize = 1, hold = True)

plt.xlim(0, rsize)
plt.ylim(-4.0, 1.0)

figure_name = 'r-oxy-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
