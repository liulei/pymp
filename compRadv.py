#!/usr/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

def calc_bin(rw, vw, nbin, rsize):

    rbin = np.arange(nbin, dtype = float)
    vbin = np.zeros(nbin, dtype = float)
    count = np.zeros(nbin, dtype = float)
    dr = rsize / nbin
    rbin = (rbin + 0.5) * dr

    for i in range(0, len(rw)):
        
        index = int(rw[i] / dr)
        if(index < nbin):
            count[index] += 1.0
            vbin[index] += vw[i]

    vbin /= count
    return rbin, vbin

if len(sys.argv) < 4:
	print 'radv_paral: not enough parameter!'
	print '\tUsage: radv_paral.py dir_name snap_num radius'
	print '\tExample: radv.py PK-7 0005 50'
	sys.exit(0)

dir_name = sys.argv[1]
snap_num = sys.argv[2]
rsize = float(sys.argv[3])

ntot, time, arr = mp.read_single(mp.prefix, dir_name, snap_num)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
	+ arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r)

v = arr['pos'][:, 0] * arr['vel'][:, 0] + arr['pos'][:, 1] * arr['vel'][:, 1] \
	+ arr['pos'][:, 2] * arr['vel'][:, 2]

v /= r

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)

rc('font', size = 17)

#plt.title(dir_name + ' ' + snap_num)

plt.xlabel('Radius [kpc]')
plt.ylabel('Radial Velocity [km/s]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.96, bottom = 0.12)

print 'len of r:', len(r)
print 'len of v:', len(v)

plt.scatter(r[idw], v[idw], s = 1, c = 'r', edgecolors = 'none')
plt.scatter(r[idc], v[idc], s = 1, c = 'g', edgecolors = 'none')

ntot, time, arr = mp.read_single(mp.prefix, 'PKlh-50', snap_num)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
	+ arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r)

v = arr['pos'][:, 0] * arr['vel'][:, 0] + arr['pos'][:, 1] * arr['vel'][:, 1] \
	+ arr['pos'][:, 2] * arr['vel'][:, 2]

v /= r

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)

rw = r[idw]
vw = v[idw]
nbin = 20
rbin, vbin = calc_bin(rw, vw, nbin, rsize)

plt.plot(rbin, vbin, 'r--', lw = 3)

plt.xlim(0, rsize)
plt.ylim(-100.0, 600.0)

eps_name = 'r-v-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(eps_name)

