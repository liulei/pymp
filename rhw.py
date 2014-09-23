#!/usr/bin/python

from numpy import *
import numpy as np
from mp import *
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 4:
	print 'rhs: not enough parameter!'
	print '\tUsage: rhs.py dir_name snap_num  radius'
	print '\tExample: rhs.py fbk-1 0001 50.0'
	sys.exit()

dir_name = sys.argv[1]
snap_num = sys.argv[2]
rsize = float(sys.argv[3])

file_warm = prefix + '/' + dir_name + '/' + 'nb_warm_' + snap_num + '.dump'
arr = np.loadtxt(file_warm, dtype = float, skiprows = 1)

rc('font', size = 17)

plt.title(dir_name + ' ' + snap_num)
plt.xlabel('Radius [kpc]')
plt.ylabel('Smoothing length [kpc]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)
plt.xscale('log')
plt.yscale('log')

plt.scatter(arr[:, 0], arr[:, 1], c = 'r', s = 0.3, marker = 'o', \
    edgecolors = 'none')

plt.xlim(0.01, rsize)
plt.ylim(0.01, 4.0)

figure_name = 'r-h-warm-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)
