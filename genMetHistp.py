#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp


def gen_hist_Fe(rarr, dir_name, base_name, snap_num, title_name = ''):

    zl = -4.0
    zh = 0.0

    ids = np.where(rarr['type'] == mp.TYPE_STAR_PARAL)
    mass = rarr['mass'][ids]
    mass_Fe = rarr['mass_Fe'][ids]

    idmm = np.where(mass_Fe < 0.0)
    print 'total number with negative Fe:', np.size(idmm)
    print mass_Fe[idmm]
    print mass[idmm]

    frac_Fe = 0.75 * np.power(10.0, 7.55 - 12.0) * 56.0 * (1.0E-5 / 0.02)
    mass_Fe += mass * frac_Fe
    Fes = np.log10(mass_Fe / mass / 0.75 / 56.0) - 7.55 + 12.0
    
    mass_Fe -= mass * frac_Fe
    
    nbin = 50
    dz = (zh - zl) / nbin
    count = np.zeros(nbin, dtype = float)
    xz = np.arange(nbin, dtype = float)
    xz = zl + (xz + 0.5) * dz

    mtot = 0.0
    for i in range(0, len(Fes)):

        v = Fes[i]
        if(mass_Fe[i] < 0.0):
            continue
        id = int((v - zl) / dz)
        
        if (id >= 0 and id < nbin):
            count[id] += 1.0
            mtot += mass[id]

    count /= (dz * mtot)

    rc('font', size = 15)
    plt.clf()
    plt.title(title_name)
    plt.xlabel('Iron abundance [Fe/H]')
    plt.ylabel('dN / index / M$_\odot$')

    plt.plot(xz, count, drawstyle = 'steps-mid')

    plt.xlim(zl, zh)
    figure_name = 'Fe-hist-' + dir_name + '-' + snap_num + '.eps'
    plt.savefig(figure_name)

if len(sys.argv) < 6:
	print 'genMetHistp: not enough parameter!'
	print '\tUsage: genMetHistp.py dir_name base_name nproc start end'
	print '\tExample: genMetHistp.py int-1 INT 32 0 20'
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
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

    title = 't = %04d Myr' % int(time + 0.1)

    gen_hist_Fe(rarr, dir_name, base_name, snap_num, title_name = title)

    print ' '
    if i < 20:
        i += 1
    else:
        i += 10

######################### end of main function ###########################


