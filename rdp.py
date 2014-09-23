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
ntot, arr = mp.read_dump_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

r = arr['rad'][:]
den = arr['den'][:]

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)

rc('font', size = 17)

plt.xlabel('Radius [kpc]')
plt.ylabel('Density [cm$^{-3}$]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)
plt.yscale('log')

print 'len of r:', len(r)

plt.scatter(r[idw], den[idw], c = 'r', s = 1, marker = 'o', edgecolors = 'none')
plt.scatter(r[idc], den[idc], c = 'g', s = 1, marker = 'o', edgecolors = 'none')

plt.xlim(0, rsize)
plt.ylim(1E-6, 1E2)

figure_name = 'r-den-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
