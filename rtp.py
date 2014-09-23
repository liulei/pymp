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
	print 'rtp: not enough parameter!'
	print '\tUsage: rtp.py dir_name base_name snap_num nproc radius'
	print '\tExample: rtp.py hd-1 1E3 0001 1 20.0'

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])
rsize = float(sys.argv[5])

ntot = 0
ntot, arr = mp.read_dump_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

r = arr['rad'][:]
T = arr['T'][:]

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)

rc('font', size = 17)

plt.xlabel('Radius [kpc]')
plt.ylabel('Temperature [K]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)
plt.yscale('log')

print 'len of r:', len(r)

plt.plot(r[idw], T[idw], 'r,', markersize = 1, hold = True)
plt.plot(r[idc], T[idc], 'g,', markersize = 1, hold = True)

plt.xlim(0, rsize)
plt.ylim(0.9E2, 1E8)

figure_name = 'r-T-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
