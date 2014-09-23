#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
from matplotlib import ticker
import matplotlib.pyplot as plt
import sys
import os
import mp


def calc_hist_Fe(rarr, zl, zh, nbin, time):

    id1 = (rarr['type'] == mp.TYPE_STAR_PARAL)
    id2 = (rarr['t_dead'] > time)
    id3 = (rarr['ss_type'] > 0)
    id = np.logical_and(id1, id2)
    id = np.logical_and(id, id3)
#    ids = np.where(rarr['type'] == mp.TYPE_STAR_PARAL)
    ids = np.where(id)
    mass = rarr['mass'][ids]
    Z = rarr['mass_Z'][:, mp.ID_Fe]
    mass_Fe = Z[ids]

    idmm = np.where(mass_Fe < 0.0)
    print 'total number with negative Fe:', np.size(idmm)
    print mass_Fe[idmm]
    print mass[idmm]

    frac_Fe = 0.75 * np.power(10.0, 7.55 - 12.0) * 56.0 * (2.0E-4 / 0.02)
    mass_Fe += mass * frac_Fe
    Fes = np.log10(mass_Fe / mass / 0.75 / 56.0) + 12.0
    
    dz = (zh - zl) / nbin
    count = np.zeros(nbin, dtype = float)
    xz = np.arange(nbin, dtype = float)
    xz = zl + (xz + 0.5) * dz

    mtot = 0.0
    for i in range(0, len(Fes)):

        v = Fes[i]
#        if(mass_Fe[i] < 0.0):
#            continue
        id = int((v - zl) / dz)
        
        if (id >= 0 and id < nbin):
            count[id] += 1.0
            mtot += mass[id]

    count /= dz

    return xz, count

if len(sys.argv) < 4:
	print 'compFeHistp: not enough parameter!'
	print '\tUsage: compFeHistp.py dir_name base_name nproc'
	print '\tExample: compFeHistp.py SS-5E7-iso-3 dwarf 16'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])

zl = 5.4
zh = 7.6
nbin = 50.0

rc('font', size = 15)
ax = plt.subplot(111)
plt.xlabel('12 + log(Fe/H)')
plt.ylabel('dN / Index')

majorLocator = ticker.MultipleLocator(0.5)

formatter = ticker.ScalarFormatter(useMathText = True)
formatter.set_powerlimits((-2,2))

ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_locator(majorLocator)

snap_num = '0005'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xz, count = calc_hist_Fe(rarr, zl, zh, nbin, time)
#count *= 16.0
plt.plot(xz, count, 'r-', label = 't = 0.5 Gyr', drawstyle = 'steps-mid')

snap_num = '0010'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xz, count = calc_hist_Fe(rarr, zl, zh, nbin, time)
plt.plot(xz, count, 'g-', label = 't = 1.0 Gyr', drawstyle = 'steps-mid')

snap_num = '0015'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xz, count = calc_hist_Fe(rarr, zl, zh, nbin, time)
plt.plot(xz, count, 'b-', label = 't = 1.5 Gyr', drawstyle = 'steps-mid')

plt.xlim(zl, zh)
plt.ylim(0.0, 10.0E6)

lg = plt.legend(loc = 1, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'comp-Fe-hist-' + dir_name + '.png'
plt.savefig(figure_name)

figure_name = 'comp-Fe-hist-' + dir_name + '.eps'
plt.savefig(figure_name)


######################### end of main function ###########################


