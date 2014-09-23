#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp

def calc_hist_linear(ml, mh, ms, nbin):

    dm = (mh - ml) / nbin
    xm = np.arange(nbin, dtype = float)
    xm = ml + (xm + 0.5) * dm

    count = np.zeros(nbin, dtype = float)

    for i in range(0, len(ms)):

        id = int((ms[i] - ml) / dm)
        
        if (id >= 0 and id < nbin):
            count[id] += 1.0

    count /= dm

    return xm, count


def calc_hist(ml, mh, ms, nbin):
    
    logml = np.log10(ml)
    logmh = np.log10(mh)

    dm = (logmh - logml) / nbin
    count = np.zeros(nbin, dtype = float)
    xlogm = np.arange(nbin, dtype = float)
    xlogm = logml + (xlogm + 0.5) * dm
    xm = np.power(10.0, xlogm)

    for i in range(0, len(ms)):

        logm = np.log10(ms[i])

        id = int((logm - logml) / dm)
        
        if (id >= 0 and id < nbin):
            count[id] += 1.0

    count /= dm
    count /= xm

    return xm, count

if len(sys.argv) < 4:
	print 'compStarMassHistp: not enough parameter!'
	print '\tUsage: compStarMassHistp.py dir_name base_name nproc'
	print '\tExample: compStarMassHistp.py SS-5E7-iso-3 dwarf 16'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])

ml = 0.8
mh = 100.0
nbin = 25

rc('font', size = 15)
plt.clf()
plt.xlabel('Stellar mass [M$_\odot$]')
plt.ylabel('dN / dlogM / M')

plt.xscale('log')
plt.yscale('log')

snap_num = '0005'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
boolarr = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, rarr['ss_type'] != mp.SS_TYPE_LM)
boolarr = np.logical_and(boolarr, rarr['t_dead'] > time)
ids = np.where(boolarr)
ms = rarr['mass'][ids]
xm, count = calc_hist(ml, mh, ms, nbin)
plt.plot(xm, count, 'r-', drawstyle = 'steps-mid', label = 't = 0.5 Gyr')

snap_num = '0010'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
boolarr = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, rarr['ss_type'] != mp.SS_TYPE_LM)
boolarr = np.logical_and(boolarr, rarr['t_dead'] > time)
ids = np.where(boolarr)
ms = rarr['mass'][ids]
xm, count = calc_hist(ml, mh, ms, nbin)
plt.plot(xm, count, 'g-', drawstyle = 'steps-mid', label = 't = 1.0 Gyr')

snap_num = '0030'
ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
boolarr = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, rarr['ss_type'] != mp.SS_TYPE_LM)
boolarr = np.logical_and(boolarr, rarr['t_dead'] > time)
ids = np.where(boolarr)
ms = rarr['mass'][ids]
xm, count = calc_hist(ml, mh, ms, nbin)
plt.plot(xm, count, 'b-', drawstyle = 'steps-mid', label = 't = 3.0 Gyr')

IMF = 3.0E6 * np.power(xm, -2.7)
plt.plot(xm, IMF, 'k-', label = 'Slope = -2.7')

plt.xlim(ml, mh)

lg = plt.legend(loc = 0, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'comp-Mass-hist-' + dir_name + '-' + snap_num + '.png'
plt.savefig(figure_name)


######################### end of main function ###########################


