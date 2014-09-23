#!/home/liulei/local/bin/python

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

if len(sys.argv) < 3:
	print 'hist: not enough parameter!'
	print '\tUsage: hist.py dir_name snap_num'
	print '\tExample: hist.py PKc-1 0005'
	sys.exit(1)

dir_name = sys.argv[1]
snap_num = sys.argv[2]

ntot = 0
ntot, arr = mp.read_single(mp.prefix, dir_name, snap_num)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
	+ arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r)

idc = np.where(arr['type'] == mp.TYPE_COLD)

ml = 1E3
mh = 1E7

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

plt.xlabel('M$_\mathrm{COLD}$ [M$_\odot$]')
plt.ylabel('dN / d(log M$_\mathrm{COLD}$) / M$_\mathrm{COLD}$')
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
