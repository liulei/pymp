#!/usr/bin/python

# mass.py: plot mass loss as a function of time

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'mass_loss.py: not enough parameter!'
	print '\tUsage: ./mass_loss.py file_name ending_time'
	print '\tExample: ./mass.py PKlh-1 1000'
	sys.exit(0)

prefix = '/home/liulei/program/mp-cd-sph/run'

file_in = prefix + '/' + sys.argv[1] + '/mass_loss.dat'

rc('font', size = 15)

array = np.loadtxt(file_in, dtype = float)

fig = plt.figure()
plt.yscale('log')
plt.xlabel('Time [Myr]')
#plt.ylabel('Mass [M$_\odot$]')
plt.ylabel('Mass loss [M$_\odot$]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.13)
plt.plot(array[:, 0], array[:, 1], '-', color = 'k', hold = True)
plt.xlim(0, float(sys.argv[2]))
plt.ylim(1.0e6, 1.0e10)

#lg = plt.legend(('HOT/WARM', 'COLD', 'STAR'), loc = 4, prop = {'size': 12})
#lg.get_frame().set_linewidth(0)

figure_name = 'mass-loss-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)


