#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
from matplotlib import ticker
import matplotlib.pyplot as plt
import sys
import os
import mp


def select_SNII(rarr, time):

    ba = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, \
            rarr['ss_type'] == mp.SS_TYPE_SNII)
    ba = np.logical_and(ba, rarr['t_dead'] < time)
    id = np.where(ba)

    m0all = rarr['m0'][:]
    mall = rarr['mass'][:]

    m0 = m0all[id]
    m = mall[id]
    idd = where(m < 0.9 * m0)

    return m0[idd], m[idd]

def select_SNIa(rarr, time):

    ba = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, \
            rarr['ss_type'] == mp.SS_TYPE_SNIa)
    ba = np.logical_and(ba, rarr['t_dead'] < time)
    id = np.where(ba)

    m0all = rarr['m0'][:]
    mall = rarr['mass'][:]

    m0 = m0all[id]
    m = mall[id]

    idd = where(m < 0.95 * m0)

    return m0[idd], m[idd]

def select_PN(rarr, time):

    ba = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, \
            rarr['ss_type'] == mp.SS_TYPE_PN)
    ba = np.logical_and(ba, rarr['t_dead'] < time)
    id = np.where(ba)

    m0all = rarr['m0'][:]
    mall = rarr['mass'][:]

    m0 = m0all[id]
    m = mall[id]
    
    idd = where(m < 0.9 * m0)
    modd = m[idd]
    print 'Total PN: ', len(m)

    return m0[idd], m[idd]

if len(sys.argv) < 4:
	print 'showM0M: not enough parameter!'
	print '\tUsage: showM0M.py dir_name base_name nproc snap_num'
	print '\tExample: showM0M.py SS-5E7-iso-3 dwarf 16 0010'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
snap_num = sys.argv[4]

rc('font', size = 15)
ax = plt.subplot(111)
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.12)
plt.xlabel('Original mass [M$_\odot$]')
plt.ylabel('After feedback [M$_\odot$]')

majorLocator = ticker.MultipleLocator(0.5)

formatter = ticker.ScalarFormatter(useMathText = True)
formatter.set_powerlimits((-2,2))

#ax.yaxis.set_major_formatter(formatter)
#ax.xaxis.set_major_locator(majorLocator)

plt.xscale('log')
plt.yscale('log')

ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
print 'time:', time
time *= 0.9999
m0, m = select_SNII(rarr, time)
plt.scatter(m0, m, c = 'b', marker = 'o', s = 1, edgecolor = 'none', label = 'SNII')

m0, m = select_SNIa(rarr, time)
plt.scatter(m0, m, c = 'r', marker = 'o', s = 1, edgecolor = 'none', label = 'SNIa')

m0, m = select_PN(rarr, time)
plt.scatter(m0, m, c = 'g', marker = 'o', s = 1, edgecolor = 'none', label = 'PN')

plt.xlim(0.8, 100.0)

lg = plt.legend(loc = 2, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'show-M0M-' + dir_name + '-' + snap_num + '.png'
plt.savefig(figure_name)

######################### end of main function ###########################


