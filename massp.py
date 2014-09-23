#!/usr/bin/python

# mass.py: plot oxygen abundance as a function of time for different radius 
# and [O/Fe] as a function of [Fe/H]

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'mass: not enough parameter!'
	print '\tUsage: ./mass.py file_name ending_time radius(optional)'
	print '\tExample: ./mass.py PK-7 1000 1.0(optional)'
	sys.exit(0)

#prefix = '/home/liulei/program/mp-cd-sph/run'

file_in = prefix + '/' + sys.argv[1] + '/mass.dat'
if len(sys.argv) == 4:
	file_in = prefix + '/' + sys.argv[1] + '/mass_%.1fkpc.dat' % \
		(float(sys.argv[3]))

rc('font', size = 20)

array = np.loadtxt(file_in, dtype = struct_mass_paral)

#time = array['time'] * TNORM / Myr

#warm = array[:]['m_warm'] * MNORM / Msol
#cold = array[:]['m_cold'] * MNORM / Msol
#star = array[:]['m_star'] * MNORM / Msol

time = array['time']

warm = array[:]['m_warm']
cold = array[:]['m_cold']
star = array[:]['m_star']


if len(sys.argv) == 3:
	plt.title(sys.argv[1])
if len(sys.argv) == 4:
	plt.title(sys.argv[1] + ' within ' + sys.argv[3] + ' kpc')

plt.yscale('log')
plt.xlabel('Time [Myr]')
plt.ylabel('Mass [M$_\odot$]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.plot(time, warm, '-', color = 'r', hold = True)
plt.plot(time, cold, '-', color = 'g', hold = True)
plt.plot(time, star, '-', color = 'b', hold = True)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(1.0e4, 1.0e8)
figure_name = 'mass-' + sys.argv[1] + '.eps'

lg = plt.legend(('HOT/WARM', 'COLD', 'STAR'), loc = 4)
lg.get_frame().set_linewidth(0)

if len(sys.argv) == 4:
	figure_name = 'mass-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.eps'

plt.savefig(figure_name)


