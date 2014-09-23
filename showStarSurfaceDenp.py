#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp


def gen_star_surface_den(arr, dir_name, base_name, snap_num, size, title_name = ''):

    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

    r = arr['pos'][ids, 0] * arr['pos'][ids, 0] \
        + arr['pos'][ids, 1] * arr['pos'][ids, 1]
    r = np.sqrt(r)

    mass = arr['mass'][ids]
   
    nbin = 50
    dr = size / nbin
    drh = 0.5 * dr
    rb = np.arange(nbin, dtype = float)
    rb = (rb + 0.5) * dr
    mb = np.zeros(nbin, dtype = float)

    for i in range(0, len(mass)):

        id = int(r[0][i] / dr)
        if(id < nbin):
            mb[id] += mass[id]

    dV = np.power(rb + drh, 2) - np.power(rb - drh, 2)
    dV *= 4.0 * np.pi
    
    rhob = mb / dV # Msol / kpc^2
    rhob *= 1.0E-6 # Msol / pc^2

############################## mass density ##############################

    rc('font', size = 15)
    plt.clf()
    plt.title(title_name)
    plt.xlabel('Radius [kpc]')
    plt.ylabel('Surface stellar mass density [M$_\odot$/pc$^\mathsf{2}$]')

    plt.plot(rb, rhob, 'r-')

    plt.xlim(0, size)
    figure_name = 'Star-R-surface-rho-' + dir_name + '-' + snap_num + '.png'
    plt.savefig(figure_name)


if len(sys.argv) < 7:
    print 'showStarSurfaceDenp: not enough parameter!'
    print '\tUsage: showStarSurfaceDenp.py dir_name base_name nproc size start end'
    print '\tExample: showStarSurfaceDenp.py SS-5E7-1 dwarf 16 8.0 0 20'
    sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
size = float(sys.argv[4])
start = int(sys.argv[5])
end = int(sys.argv[6])

i = start
while i <= end:
#for i in range(start, end + 1):

    snap_num = '%04d' % i

    print '##################### snap ', snap_num, ' ######################'

    ntot = 0
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

    title = 't = %04d Myr' % int(time + 0.1)

    gen_star_surface_den(rarr, dir_name, base_name, snap_num, size, title_name = title)

    print ' '
    i += 10

######################### end of main function ###########################


