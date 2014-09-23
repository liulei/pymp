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

if len(sys.argv) < 4:
	print 'rd: not enough parameter!'
	print '\tUsage: rd.py dir_name snap_num  radius'
	print '\tExample: rd.py fbk-1 0001 50.0'
	sys.exit()

dir_name = sys.argv[1]
snap_num = sys.argv[2]
rsize = float(sys.argv[3])

ntot = 0
ntot, arr = mp.read_dump(mp.prefix, dir_name, snap_num)

r = arr['rad'][:]
den = arr['den'][:]

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)

rc('font', size = 17)

plt.xlabel('Radius [kpc]')
plt.ylabel('Density [cm$^{-3}$]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)
plt.xscale('log')
plt.yscale('log')

print 'len of r:', len(r)

plt.scatter(r[idw], den[idw], c = 'r', s = 1, marker = 'o', edgecolors = 'none')
plt.scatter(r[idc], den[idc], c = 'g', s = 1, marker = 'o', edgecolors = 'none')

#plt.xlim(0, rsize)
plt.xlim(0.1, rsize)
plt.ylim(1E-6, 1E4)

figure_name = 'r-den-' + dir_name + '-' + snap_num + '.png'
plt.savefig(figure_name)
