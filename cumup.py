#!/usr/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 6:
	print 'rd: not enough parameter!'
	print '\tUsage: rd.py dir_name base_name snap_num nproc radius'
	print '\tExample: rd.py hd-1 1E3 0001 1 50.0'
	sys.exit(0)

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])
rsize = float(sys.argv[5])

ntot = 0
ntot, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

r2 = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
    + arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r2)

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)
ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)
idm = np.where(arr['type'] == mp.TYPE_DM_PARAL)

mdm = arr[idm]['mass']
mdm_tot = mdm.sum()

nbin = 100
dr = rsize / nbin

rbin = np.arange(nbin, dtype = float)
rbin = (rbin + 0.5) * dr

dmbin = np.zeros(nbin, dtype = float)

for i in range(0, ntot):

    idx = int(r[i] / dr)
    if idx < nbin:
        if(arr[i]['type'] == mp.TYPE_DM_PARAL):
            dmbin[idx] += arr[i]['mass']

for i in range(1, nbin):
    dmbin[i] += dmbin[i - 1]

dmbin /= mdm_tot

rc('font', size = 17)

plt.xlabel('Radius [kpc]')
plt.ylabel('Cumulative fraction')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

plt.plot(rbin, dmbin, 'k-')

plt.xlim(0.0, rsize)
plt.ylim(0.0, 1.0)

figure_name = 'fraction-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
