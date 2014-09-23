#!/usr/bin/python

from numpy import *
import numpy as np
import mp
import mp_snap_mc
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 5:
	print 'histmcp: not enough parameter!'
	print '\tUsage: histmcp.py dir_name base_name snap_num nproc'
	print '\tExample: histmcp.py MCT-1 dwarf 0001 4'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])

ntot = 0
ntot, time, arr = mp_snap_mc.read_mc(mp.prefix, dir_name, base_name, snap_num, nproc)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
	+ arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r)

idc = np.where(arr['type'] == mp.TYPE_COLD)

ml = 1E1
mh = 1E5

logml = log10(ml)
logmh = log10(mh)

mass = arr['mass'][idc]

nbin = 20

dm = (logmh - logml) / nbin

count = np.zeros(nbin, dtype = float)
xlogm = np.arange(nbin, dtype = float)
xlogm = logml + (xlogm + 0.5) * dm

xm = np.power(10.0, xlogm)

mtot = 0.0

for i in range(0, len(mass)):
	
	logm = np.log10(mass[i])
	
	id = int((logm - logml) / dm)

	if (id >= 0 and id < nbin):
		
		mtot += mass[i]
		count[id] += 1.0

count /= dm
count /= mtot

rc('font', size = 17)

plt.title(dir_name + ' ' + snap_num)

plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

plt.xscale('log')
plt.yscale('log')

plt.plot(xm, count, drawstyle = 'steps-mid')
#plt.plot(xm, count)

print xm

plt.xlim(ml, mh)
#plt.ylim(-100.0, 600.0)

figure_name = 'hist-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
