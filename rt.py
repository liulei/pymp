#!/usr/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 4:
    print 'rtp: not enough parameter!'
    print '\tUsage: rt.py dir_name snap_num radius'
    print '\tExample: rtp.py PKlh-1 0010 20.0'
    sys.exit(-1)

dir_name = sys.argv[1]
snap_num = sys.argv[2]
rsize = float(sys.argv[3])

ntot = 0
ntot, arr = mp.read_dump(mp.prefix, dir_name, snap_num)

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

figure_name = 'r-T-' + dir_name + '-' + snap_num + '.png'
plt.savefig(figure_name)

figure_name = 'r-T-' + dir_name + '-' + snap_num + '.eps'
#plt.savefig(figure_name)
