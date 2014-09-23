#!/usr/bin/python

# massz.py: plot Z abundance as a function of time for different radius 

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'massz: not enough parameter!'
	print '\tUsage: ./massz.py file_name ending_time radius(optional)'
	print '\tExample: ./massz.py PK-7 1000 1.0(optional)'
	sys.exit(0)

file_in = prefix + '/' + sys.argv[1] + '/mass.dat'
if len(sys.argv) == 4:
	file_in = prefix + '/' + sys.argv[1] + '/mass_%.1fkpc.dat' % \
		(float(sys.argv[3]))

rc('font', size = 20)

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

m_warm = array[:]['m_warm']
m_cold = array[:]['m_cold']
m_star = array[:]['m_star']

# now can only do like this:
Z = array[:]['mass_Z']

mz_warm = Z[:, ID_Z, 0] 
mz_cold = Z[:, ID_Z, 1]
mz_star = Z[:, ID_Z, 2]

z_warm = mz_warm / m_warm
z_cold = mz_cold / m_cold
z_star = mz_star / m_star

if len(sys.argv) == 3:
	plt.title(sys.argv[1])
if len(sys.argv) == 4:
	plt.title(sys.argv[1] + ' within ' + sys.argv[3] + ' kpc')
plt.xlabel('Time [Myr]')
plt.ylabel('Metallicity [Z]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.yscale('log')
plt.plot(time, z_warm, '-', color = 'r', hold = True)
plt.plot(time, z_cold, '-', color = 'g', hold = True)
plt.plot(time, z_star, '-', color = 'b', hold = True)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(1.0E-6, 1.0E-2)
figure_name = 'Z-' + sys.argv[1] + '.eps'
if len(sys.argv) == 4:
	figure_name = 'Z-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.eps'

plt.savefig(figure_name)
