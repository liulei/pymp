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
	print 'Dsort: not enough parameter!'
	print '\tUsage: Dsort.py dir_name snap_num range'
	print '\tExample: Dsort.py PKc-1 0001 50'
	sys.exit(1)

dir_name = sys.argv[1]
snap_num = sys.argv[2]
size = float(sys.argv[3])

ntot = 0
ntot, rarr = mp.read_dump(mp.prefix, dir_name, snap_num)

print 'Sorting...'
arr = np.sort(rarr, order = 'den')
print 'done!'

x = arr['pos'][:, 0]
y = arr['pos'][:, 1]
z = arr['pos'][:, 2]

den = arr['den'][:]

id1 = (np.abs(y) < 0.2)
id2 = (arr['type'] == mp.TYPE_WARM)
id3 = np.logical_and(id1, id2)
idw = np.where(id3)
#idw = np.where(arr['type'] == mp.TYPE_WARM)
idc = np.where(arr['type'] == mp.TYPE_COLD)
ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

rc('font', size = 17)
width, height = rcParams['figure.figsize']
sz = min(width, height)

#plt.figure(figsize = (sz, sz))
plt.xlabel('X [kpc]')
plt.ylabel('Z [kpc]')
plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

den[idc] = 2.0E-7

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()
plt.scatter(x[idw], z[idw], s = 1, c = den[idw], marker = 'o', cmap = cmap, \
	norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')
plt.scatter(x[idc], z[idc], s = 5, c = den[idc], marker = 'o', cmap = cmap, \
	norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')
#cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0), format = '%.E')
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
cb.set_label('Density [cm$^{-3}$]')

plt.xlim(-size, size)
plt.ylim(-size, size)

figure_name = 'Dsort-xz-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)

######################## X-Y #################################################

plt.clf()
#plt.figure(figsize = (sz, sz))
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()
plt.scatter(x[idw], y[idw], s = 1, c = den[idw], marker = 'o', cmap = cmap, \
	norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')
plt.scatter(x[idc], y[idc], s = 5, c = den[idc], marker = 'o', cmap = cmap, \
	norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')
#cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0), format = '%.E')
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
cb.set_label('Density [cm$^{-3}$]')

plt.xlim(-size, size)
plt.ylim(-size, size)

figure_name = 'Dsort-xy-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
