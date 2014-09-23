#!/usr/bin/python

# Nitrogen.py: plot Nitrogen abundance as a function of time for different 
# radius.

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'Nitrogen.py: not enough parameter!'
	print '\tUsage: ./Nitrogen.py file_name ending_time radius(optional)'
	print '\tExample: ./Nigrogen.py PK-7 1000 1.0(optional)'
	sys.exit(0)

file_in = prefix + '/' + sys.argv[1] + '/mass.dat'
if len(sys.argv) == 4:
	file_in = prefix + '/' + sys.argv[1] + '/mass_%.1fkpc.dat' % \
		(float(sys.argv[3]))

rc('font', size = 20)

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

# now can only do like this:
Z = array[:]['mass_Z']

N_warm = np.log10(Z[:, ID_N, 0] / Z[:, ID_H, 0] / 14.0) - 7.86 + 12.0
N_cold = np.log10(Z[:, ID_N, 1] / Z[:, ID_H, 1] / 14.0) - 7.86 + 12.0
N_star = np.log10(Z[:, ID_N, 2] / Z[:, ID_H, 2] / 14.0) - 7.86 + 12.0

if len(sys.argv) == 3:
	plt.title(sys.argv[1])
if len(sys.argv) == 4:
	plt.title(sys.argv[1] + ' within ' + sys.argv[3] + ' kpc')
plt.xlabel('Time [Myr]')
plt.ylabel('Nitrogen Abundance [N/H]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.plot(time, N_warm, '-', color = 'r', hold = True)
plt.plot(time, N_cold, '-', color = 'g', hold = True)
plt.plot(time, N_star, '-', color = 'b', hold = True)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(-5.0, -1)
figure_name = 'Nitrogen-' + sys.argv[1] + '.eps'
if len(sys.argv) == 4:
	figure_name = 'Nitrogen-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.eps'

plt.savefig(figure_name)

