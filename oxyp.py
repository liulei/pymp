#!/usr/bin/python

# oxy.py: plot oxygen abundance as a function of time for different radius 
# and [O/Fe] as a function of [Fe/H]

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'oxy: not enough parameter!'
	print '\tUsage: ./oxy.py file_name ending_time radius(optional)'
	print '\tExample: ./oxy.py PK-7 1000 1.0(optional)'
	sys.exit(0)

file_in = prefix + '/' + sys.argv[1] + '/mass.dat'
if len(sys.argv) == 4:
	file_in = prefix + '/' + sys.argv[1] + '/mass_%.1fkpc.dat' % \
		(float(sys.argv[3]))

rc('font', size = 20)

array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time']

# now can only do like this:
Z = array[:]['mass_Z']

print 'metal:', Z[:, ID_H, :]

O_warm = np.log10(Z[:, ID_O, 0] / Z[:, ID_H, 0] / 16.0) - 8.9 + 12.0
O_cold = np.log10(Z[:, ID_O, 1] / Z[:, ID_H, 1] / 16.0) - 8.9 + 12.0
O_star = np.log10(Z[:, ID_O, 2] / Z[:, ID_H, 2] / 16.0) - 8.9 + 12.0

Fe_warm = np.log10(Z[:, ID_Fe, 0] / Z[:, ID_H, 0] / 56.0) - 7.55 + 12.0
Fe_cold = np.log10(Z[:, ID_Fe, 1] / Z[:, ID_H, 1] / 56.0) - 7.55 + 12.0
Fe_star = np.log10(Z[:, ID_Fe, 2] / Z[:, ID_H, 2] / 56.0) - 7.55 + 12.0

OFe_warm = O_warm - Fe_warm
OFe_cold = O_cold - Fe_cold
OFe_star = O_star - Fe_star

if len(sys.argv) == 3:
	plt.title(sys.argv[1])
if len(sys.argv) == 4:
	plt.title(sys.argv[1] + ' within ' + sys.argv[3] + ' kpc')
plt.xlabel('Time [Myr]')
plt.ylabel('Oxygen Abundance [O/H]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.plot(time, O_warm, '-', color = 'r', hold = True)
plt.plot(time, O_cold, '-', color = 'g', hold = True)
plt.plot(time, O_star, '-', color = 'b', hold = True)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(-4.0, 1.0)
figure_name = 'Oxygen-' + sys.argv[1] + '.eps'
if len(sys.argv) == 4:
	figure_name = 'Oxygen-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.eps'

plt.savefig(figure_name)


plt.clf()
if len(sys.argv) == 3:
	plt.title(sys.argv[1])
if len(sys.argv) == 4:
	plt.title(sys.argv[1] + ' within ' + sys.argv[3] + ' kpc')
plt.xlabel('Time [Myr]')
plt.ylabel('[O/Fe]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.plot(Fe_warm, OFe_warm, '-', color = 'r', hold = True)
plt.plot(Fe_cold, OFe_cold, '-', color = 'g', hold = True)
plt.plot(Fe_star, OFe_star, '-', color = 'b', hold = True)
plt.xlim(-6.0, 1.0)
plt.ylim(-0.5, 1.5)
figure_name = 'OFe-' + sys.argv[1] + '.eps'
if len(sys.argv) == 4:
	figure_name = 'OFe-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.eps'

plt.savefig(figure_name)


