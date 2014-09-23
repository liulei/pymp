#!/usr/bin/python

# N_compare.py: plot [N/H] as a function of time for different radius on the
# same figure

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'N_compare: not enough parameter!'
	print '\tUsage: ./N_compare.py file_name ending_time'
	print '\tExample: ./N_compare.py PK-7 1000'
	sys.exit(0)

#prefix = '/home/liulei/program/mp-cd-sph/run'
rc('font', size = 18)

# 1.0 kpc:
file_in = prefix + '/' + sys.argv[1] + '/mass_1.0kpc.dat'

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

Z = array[:]['mass_Z']

N_warm = np.log10(Z[:, ID_N, 0] / Z[:, ID_H, 0] / 14.0) - NH_sol + 12.0
N_cold = np.log10(Z[:, ID_N, 1] / Z[:, ID_H, 1] / 14.0) - NH_sol + 12.0
N_star = np.log10(Z[:, ID_N, 2] / Z[:, ID_H, 2] / 14.0) - NH_sol + 12.0

plt.plot(time, N_warm, '-', color = 'r', hold = True)
plt.plot(time, N_cold, '-', color = 'g', hold = True)
plt.plot(time, N_star, '-', color = 'b', hold = True)

# 5.0 kpc:
file_in = prefix + '/' + sys.argv[1] + '/mass_5.0kpc.dat'

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

Z = array[:]['mass_Z']

N_warm = np.log10(Z[:, ID_N, 0] / Z[:, ID_H, 0] / 14.0) - NH_sol + 12.0
N_cold = np.log10(Z[:, ID_N, 1] / Z[:, ID_H, 1] / 14.0) - NH_sol + 12.0
N_star = np.log10(Z[:, ID_N, 2] / Z[:, ID_H, 2] / 14.0) - NH_sol + 12.0

plt.plot(time, N_warm, '--', color = 'r', hold = True)
plt.plot(time, N_cold, '--', color = 'g', hold = True)
plt.plot(time, N_star, '--', color = 'b', hold = True)

plt.xlabel('Time [Myr]')
plt.ylabel('Nitrogen Abundance [N/H]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(-4.0, 1.0)

lg = plt.legend(('Hot/warm (< 1.0 kpc)', 'Cold (< 1.0 kpc)', 'Star (< 1.0 kpc)', 'Hot/warm (< 5.0 kpc)', 'Cold (< 5.0 kpc)', 'Star (< 5.0 kpc)'), \
	ncol = 2, prop = {'size': 14})
lg.get_frame().set_linewidth(0)

figure_name = 'Nitrogen-compare-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)

