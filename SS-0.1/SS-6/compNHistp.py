#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
from matplotlib import ticker
import matplotlib.pyplot as plt
import sys
import os
import mp


def calc_hist_N(rarr, zl, zh, nbin):

    ids = np.where(rarr['type'] == mp.TYPE_STAR_PARAL)
    mass = rarr['mass'][ids]
    Z = rarr['mass_Z'][:, mp.ID_N]
    mass_N = Z[ids]

    frac = 0.75 * np.power(10.0, 7.86 - 12.0) * 14.0 * (1.0E-5 / 0.02)
    mass_N += mass * frac
    N = np.log10(mass_N / mass / 0.75 / 14.0) + 12.0
    
    dz = (zh - zl) / nbin
    count = np.zeros(nbin, dtype = float)
    xz = np.arange(nbin, dtype = float)
    xz = zl + (xz + 0.5) * dz

    mtot = 0.0
    for i in range(0, len(N)):

        v = N[i]
#        if(mass_Fe[i] < 0.0):
#            continue
        id = int((v - zl) / dz)
        
        if (id >= 0 and id < nbin):
            count[id] += 1.0
            mtot += mass[id]

    count /= dz

    return xz, count

if len(sys.argv) < 4:
	print 'compNHistp: not enough parameter!'
	print '\tUsage: compNHistp.py dir_name base_name nproc'
	print '\tExample: compNHistp.py SS-5E7-iso-3 dwarf 16'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])

zl = 4.1
zh = 8.0
nbin = 50

rc('font', size = 15)
ax = plt.subplot(111)
plt.xlabel('12 + log[N/H]')
plt.ylabel('dN / Index')

majorLocator = ticker.MultipleLocator(0.5)

formatter = ticker.ScalarFormatter(useMathText = True)
formatter.set_powerlimits((-2,2))

ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_locator(majorLocator)

snap_num = '0005'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xz, count = calc_hist_N(rarr, zl, zh, nbin)
#count *= 16.0
plt.plot(xz, count, 'r-', label = 't = 0.5 Gyr', drawstyle = 'steps-mid')

snap_num = '0010'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xz, count = calc_hist_N(rarr, zl, zh, nbin)
plt.plot(xz, count, 'g-', label = 't = 1.0 Gyr', drawstyle = 'steps-mid')

snap_num = '0030'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xz, count = calc_hist_N(rarr, zl, zh, nbin)
plt.plot(xz, count, 'b-', label = 't = 3.0 Gyr', drawstyle = 'steps-mid')

plt.xlim(zl, zh)
#plt.ylim(0, 3.0E6)

lg = plt.legend(loc = 0, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'comp-N-hist-' + dir_name + '.png'
plt.savefig(figure_name)

######################### end of main function ###########################


