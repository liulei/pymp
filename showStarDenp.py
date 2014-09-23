#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp


def gen_star_den(arr, dir_name, base_name, snap_num, size, title_name = ''):

    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

    r = arr['pos'][ids, 0] * arr['pos'][ids, 0] \
        + arr['pos'][ids, 1] * arr['pos'][ids, 1] \
	    + arr['pos'][ids, 2] * arr['pos'][ids, 2]
    r = np.sqrt(r)

    mass = arr['mass'][ids]
   
    nbin = 50
    dr = size / nbin
    drh = 0.5 * dr
    rb = np.arange(nbin, dtype = float)
    rb = (rb + 0.5) * dr
    mb = np.zeros(nbin, dtype = float)
    countb = np.zeros(nbin, dtype = float)

    for i in range(0, len(mass)):

        id = int(r[i] / dr)
        if(id < nbin):
            mb[id] += mass[id]
            count[id] += 1.0

    dV = np.power(rb + drh, 3) - np.power(rb - drh, 3)
    dV *= 4.0 / 3.0 * np.pi
    
    rhob = mb / dV # Msol / kpc^3
    rhob *= 1.0E-9 # Msol / pc^3

    nb = countb / dV
    nb *= 1.0E-9

############################## mass density ##############################

    rc('font', size = 15)
    plt.clf()
    plt.title(title_name)
    plt.xlabel('Radius [kpc]')
    plt.ylabel('Stellar mass density [M$_\odot$/pc^\mathsf{3}]')

    plt.plot(rb, rhob, 'r-')

    plt.xlim(0, size)
    figure_name = 'Star-r-rho-' + dir_name + '-' + snap_num + '.eps'
    plt.savefig(figure_name)

############################## number density ##############################

    rc('font', size = 15)
    plt.clf()
    plt.title(title_name)
    plt.xlabel('Radius [kpc]')
    plt.ylabel('Stellar number density [pc^\mathsf{-3}]')

    plt.plot(rb, rhob, 'r-')

    plt.xlim(0, size)
    figure_name = 'Star-r-n-' + dir_name + '-' + snap_num + '.eps'
    plt.savefig(figure_name)


if len(sys.argv) < 7:
	print 'showStarDenp: not enough parameter!'
	print '\tUsage: showStarDenp.py dir_name base_name nproc size start end'
	print '\tExample: showStarDenp.py SS-5E7-1 dwarf 16 8.0 0 20'
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

    gen_star_den(rarr, dir_name, base_name, snap_num, size, title_name = title)

    print ' '
    if i < 20:
        i += 1
    else:
        i += 10

######################### end of main function ###########################


