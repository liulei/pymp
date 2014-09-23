#!/usr/bin/python

# timing.py: plot timing of various components

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'timing: not enough parameter!'
	print '\tUsage: timing.py dir_name ending_time(Myr)'
	print '\tExample: timing.py 10-1.16 500'
	sys.exit(0)

dir_name = sys.argv[1]

file_in = prefix + '/' + dir_name + '/benchmark.dat'

rc('font', size = 17)

array = np.loadtxt(file_in, dtype = float)

print 'number of col: ', size(array[0][:])

time = array[:, TM_TIME]

plt.title(dir_name)

ax = plt.subplot(111)
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1E'))
plt.xlabel('Time [Myr]')
plt.ylabel('Timing [ms]')
plt.subplots_adjust(left = 0.18, right = 0.95, top = 0.91, bottom = 0.12)

print array[:, TM_ALL]

plt.plot(time, array[:, TM_ALL], hold = True)
plt.plot(time, array[:, TM_DIVISION], hold = True)
plt.plot(time, array[:, TM_EXCH_PARTICLES], hold = True)
plt.plot(time, array[:, TM_CALC_GRAV], hold = True)
plt.plot(time, array[:, TM_NB_LOCAL] + array[:, TM_NB_GLOBAL], hold = True)
plt.plot(time, array[:, TM_SPH], hold = True)
#plt.plot(time, array[:, TM_CE], hold = True)
#plt.plot(time, array[:, TM_COAGULATION], hold = True)
#plt.plot(time, array[:, TM_FB], hold = True)
plt.plot(time, array[:, TM_EXCH_MP], hold = True)
plt.plot(time, array[:, TM_HD], hold = True)
plt.plot(time, array[:, TM_OTHER], hold = True)
plt.xlim(0, float(sys.argv[2]))
#plt.ylim(0, 4E4)
lg = plt.legend(('All', 'Division', 'Exch particles', 'Gravity', \
	'Neighbour', 'SPH', 'MP comm', 'Hot dump',\
	'Other (I/O)'), loc = 0, ncol = 2, prop = {'size': 14})
lg.get_frame().set_linewidth(0)

figure_name = 'timing-' + dir_name + '.eps'

plt.savefig(figure_name)


