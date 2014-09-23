#!/usr/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
from matplotlib import colors, ticker, colorbar, mpl
import matplotlib.pyplot as plt
from math import *
import sys

#dir_name = 'hd-1'
#base_name = '1E3'
#snap_num = '0001'
#nproc = 1

if len(sys.argv) < 4:
	print 'Tsort: not enough parameter!'
	print '\tUsage: Tsort.py dir_name snap_num range'
	print '\tExample: Tsort.py PKc-1 0001 20.0'
	sys.exit(1)

dir_name = sys.argv[1]
snap_num = sys.argv[2]
size = float(sys.argv[3])

ntot = 0
ntot, rarr = mp.read_dump(mp.prefix, dir_name, snap_num)

print 'Sorting...'
arr = np.sort(rarr, order = 'T')
arr = arr[::-1]
print 'done!'

x = arr['pos'][:, 0]
y = arr['pos'][:, 1]
z = arr['pos'][:, 2]

T = arr['T'][:]

idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)
ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

rc('font', size = 17)
width, height = rcParams['figure.figsize']
sz = min(width, height)

#plt.figure(figsize = (sz, sz))
plt.xlabel('X [kpc]')
plt.ylabel('Z [kpc]')
plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()
plt.scatter(x[idw], z[idw], s = 1, c = T[idw], marker = 'o', cmap = cmap, \
	norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
cb.set_label('Temperature [K]')

plt.xlim(-size, size)
plt.ylim(-size, size)

figure_name = 'Tsort-xz-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)

######################## X-Y #################################################

plt.clf()
#plt.figure(figsize = (sz, sz))
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()
plt.scatter(x[idw], y[idw], s = 1, c = T[idw], marker = 'o', cmap = cmap, \
	norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
cb.set_label('Temperature [K]')

plt.xlim(-size, size)
plt.ylim(-size, size)

figure_name = 'Tsort-xy-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
