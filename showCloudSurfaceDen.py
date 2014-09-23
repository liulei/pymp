#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp


def gen_cloud_surface_den(arr, dir_name, size, title_name = ''):

    idc = np.where(arr['type'] == mp.TYPE_COLD)

    r = arr['pos'][idc, 0] * arr['pos'][idc, 0] \
        + arr['pos'][idc, 1] * arr['pos'][idc, 1]
    r = np.sqrt(r)

    print r

    mass = arr['mass'][idc]
   
    nbin = 50
    dr = size / nbin
    drh = 0.5 * dr
    rb = np.arange(nbin, dtype = float)
    rb = (rb + 0.5) * dr
    mb = np.zeros(nbin, dtype = float)

    for i in range(0, len(mass)):

        id = int(r[0][i] / dr)
        if(id < nbin):
            mb[id] += mass[i]

    dV = np.power(rb + drh, 2) - np.power(rb - drh, 2)
    dV *= 4.0 * np.pi
    
    rhob = mb / dV # Msol / kpc^2
    rhob *= 1.0E-6 # Msol / pc^2

############################## mass density ##############################

    rc('font', size = 15)
    plt.clf()
    plt.title(title_name)
    plt.xlabel('Radius [kpc]')
    plt.ylabel('Surface cloud mass density [M$_\odot$/pc$^\mathsf{2}$]')

    plt.yscale('log')
    plt.ylim(0.1, 1000.0)

    plt.plot(rb, rhob, 'r-')

    plt.xlim(0, size)
    figure_name = 'Cloud-R-surface-rho-' + dir_name + '-' + snap_num + '.png'
    plt.savefig(figure_name)


if len(sys.argv) < 5:
    print 'showCloudSurfaceDen: not enough parameter!'
    print '\tUsage: showCloudSurfaceDen.py dir_name size start end'
    print '\tExample: showStarSurfaceDen.py PKhn-1 10.0 0 10'
    sys.exit(1)

dir_name = sys.argv[1]
size = float(sys.argv[2])
start = int(sys.argv[3])
end = int(sys.argv[4])

i = start
while i <= end:
#for i in range(start, end + 1):

    snap_num = '%04d' % i

    print '##################### snap ', snap_num, ' ######################'

    ntot = 0
    ntot, time, rarr = mp.read_single(mp.prefix, dir_name, snap_num)

    title = 't = %04d Myr' % int(time + 0.1)

    gen_cloud_surface_den(rarr, dir_name, size, title_name = title)

    print ' '
    i += 1

######################### end of main function ###########################


