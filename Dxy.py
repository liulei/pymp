#!/usr/bin/python
# Dxy.py: plot xz projection of density with color

import numpy as np
from matplotlib import *
from matplotlib import colors, ticker, colorbar, mpl
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'Dxz: not enough parameter!'
	print '\t usage: Dxz.py dir_name snap_num'
	print '\t example: Dxz.py PK-7 0001'
	sys.exit(0)

dir_name = sys.argv[1]
snap_num = sys.argv[2]

file_in = prefix + '/' + dir_name + '/' + snap_num + '.Dsort'

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
	vmin = 1e-2, vmax = 1.01e0, edgecolors = 'none')
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0), format = '%.e')
#cb = plt.colorbar(format = '%.e')
cb.set_label('Density [cm$^{-3}$]')

plt.xlim(-50, 50)
plt.ylim(-50, 50)

figure_name = 'Dxz-' + dir_name + '.eps'
plt.savefig(figure_name)
