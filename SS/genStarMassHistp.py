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

def gen_hist_star_mass(rarr, dir_name, base_name, snap_num, time, title_name = ''):

    ml = 0.8
    mh = 100.0

    boolarr = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, \
            rarr['ss_type'] != mp.SS_TYPE_LM)
    boolarr = np.logical_and(boolarr, rarr['t_dead'] > time)
    ids = np.where(boolarr)

    boolarr = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, \
            rarr['ss_type'] == mp.SS_TYPE_SNII)
    idsn2 = np.where(boolarr)

    boolarr = np.logical_and(rarr['type'] == mp.TYPE_STAR_PARAL, \
            rarr['ss_type'] == mp.SS_TYPE_PN)
    boolarr = np.logical_and(boolarr, rarr['t_dead'] > time)
    idpn = np.where(boolarr)

    mass = rarr['mass'][:]

#    ms = mass[idpn]
    ms = mass[ids]

    nbin = 50
    xm, count = calc_hist(ml, mh, ms, nbin)

    IMF = 3.0E6 * np.power(xm, -2.7)
#    nbin = 256
#    xm, count = calc_hist_linear(ml, mh, ms, nbin)

    rc('font', size = 15)
    plt.clf()
#    plt.title(title_name)
    plt.xlabel('Stellar mass [M$_\odot$]')
    plt.ylabel('dN / dlogM / M')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(xm, count, drawstyle = 'steps-mid')
    plt.plot(xm, IMF, 'r-')

    plt.xlim(ml, mh)
    figure_name = 'Star-hist-' + dir_name + '-' + snap_num + '.png'
    plt.savefig(figure_name)

if len(sys.argv) < 6:
	print 'genStarMassHistp: not enough parameter!'
	print '\tUsage: genStarMassHistp.py dir_name base_name nproc start end'
	print '\tExample: genStarMassHistp.py SS-5E7-iso-3 dwarf 16 100  100'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
start = int(sys.argv[4])
end = int(sys.argv[5])

i = start
while i <= end:
#for i in range(start, end + 1):

    snap_num = '%04d' % i

    print '##################### snap ', snap_num, ' ######################'

    ntot = 0
    ntot, time, rarr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

    title = 't = %04d Myr' % int(time + 0.1)

    gen_hist_star_mass(rarr, dir_name, base_name, snap_num, time, title_name = title)

    print ' '
    i += 50

######################### end of main function ###########################


