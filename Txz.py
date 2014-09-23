#!/usr/bin/python
# wc.py: plot energy component of warm and cold as a function of time.
# compare the result with supernova feedback

import numpy as np
from matplotlib import *
from matplotlib import colors, ticker, colorbar, mpl
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'Txz: not enough parameter!'
	print '\t usage: Txz.py dir_name snap_num'
	print '\t example: Txz.py PK-7 0001'
	sys.exit(0)

dir_name = sys.argv[1]
snap_num = sys.argv[2]

file_in = prefix + '/' + dir_name + '/' + snap_num + '.Tsort'

arr = np.loadtxt(file_in, dtype = float)

print 'dimension of array:', len(arr), len(arr[0])

y = arr[:, 2]

print y

id = np.where(np.fabs(y) < 10)

print id

x = arr[id, 1]
z = arr[id, 3]
T = arr[id, 5]

rc('font', size = 17)

plt.title(dir_name + ' ' + snap_num)
plt.xlabel('X [kpc]')
plt.ylabel('Z [kpc]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()
#plt.scatter(x, z, c = T, s = 20.0, cmap = cmap, norm = norm)
plt.scatter(x, z, s = 1, c = T, marker = 'o', cmap = cmap, norm = norm, \
	vmin = 1e3, vmax = 4.1e3, edgecolors = 'none')
cb = plt.colorbar(ticks = ticker.LogLocator(base = 2.0), format = '%.e')
#cb = plt.colorbar(format = '%.e')
cb.set_label('Temperature [K]')

plt.xlim(-50, 50)
plt.ylim(-50, 50)

figure_name = 'Txz-' + dir_name + '.eps'
plt.savefig(figure_name)
