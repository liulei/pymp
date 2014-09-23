#!/usr/bin/python

# oxy_compare.py: plot [O/H] as a function of time for different radius on the
# same figure

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'oxy_compare: not enough parameter!'
	print '\tUsage: ./oxy_compare.py file_name ending_time'
	print '\tExample: ./oxy_compare.py PK-7 1000'
	sys.exit(0)

NH_sol = 7.86 # arXiv:0903.3406 [astro-ph]
OH_sol = 8.65 # Asplund (2005)
FeH_sol = 7.51 # McWilliam (1997)

prefix = '/home/liulei/program/mp-cd-sph/run'
rc('font', size = 12)

fig = plt.figure()
fig.set_figwidth(5.3)
fig.set_figheight(3.6)


# 1.0 kpc:
file_in = prefix + '/' + sys.argv[1] + '/mass_1.0kpc.dat'

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

Z = array[:]['mass_Z']

O_warm = np.log10(Z[:, ID_O, 0] / Z[:, ID_H, 0] / 16.0) + 12.0
O_cold = np.log10(Z[:, ID_O, 1] / Z[:, ID_H, 1] / 16.0) + 12.0
O_star = np.log10(Z[:, ID_O, 2] / Z[:, ID_H, 2] / 16.0) + 12.0

plt.plot(time, O_warm - OH_sol, '-', color = 'r', hold = True)
plt.plot(time, O_cold - OH_sol, '-', color = 'g', hold = True)
plt.plot(time, O_star - OH_sol, '-', color = 'b', hold = True)

# 5.0 kpc:
file_in = prefix + '/' + sys.argv[1] + '/mass_5.0kpc.dat'

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

Z = array[:]['mass_Z']

O_warm = np.log10(Z[:, ID_O, 0] / Z[:, ID_H, 0] / 16.0) + 12.0
O_cold = np.log10(Z[:, ID_O, 1] / Z[:, ID_H, 1] / 16.0) + 12.0
O_star = np.log10(Z[:, ID_O, 2] / Z[:, ID_H, 2] / 16.0) + 12.0

plt.plot(time, O_warm - OH_sol, '--', color = 'r', hold = True)
plt.plot(time, O_cold - OH_sol, '--', color = 'g', hold = True)
plt.plot(time, O_star - OH_sol, '--', color = 'b', hold = True)

plt.xlabel('Time [Myr]')
plt.ylabel('[O/H]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(5.0 - OH_sol, 1.0+ 10.2 - OH_sol)

lg = plt.legend(('Hot/warm (< 1.0 kpc)', 'Cold (< 1.0 kpc)', 'Star (< 1.0 kpc)', 'Hot/warm (< 5.0 kpc)', 'Cold (< 5.0 kpc)', 'Star (< 5.0 kpc)'), \
	ncol = 2, prop = {'size': 9})
lg.get_frame().set_linewidth(0)

figure_name = 'Oxygen-compare-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)

