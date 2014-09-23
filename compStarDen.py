#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp
import mp_snap_mc


def comp_star_den(arr, nbin, size, time):

    id1 = (arr['type'] == mp.TYPE_STAR_PARAL)
    id2 = (arr['t_dead'] > time)

    ids = np.logical_and(id1, id2)
    ids = np.where(ids)

    arr['pos'] *= 1E3 # convert to pc

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

    for i in range(0, len(mass)):

        id = int(r[0][i] / dr)
        if(id < nbin and id >= 0):
            mb[id] += mass[i]

    dV = np.power(rb + drh, 3) - np.power(rb - drh, 3)
    dV *= np.pi * (4. / 3.)
    
    denb = mb / dV # Msol / pc^3

    return rb, denb

############################## mass density ##############################


if len(sys.argv) < 6:
    print 'compStarDen: not enough parameter!'
    print '\tUsage: compStarDen.py dir_name base_name nproc size'
    print '\tExample: compStarDen.py MCT-13 dwarf 4 0060 50.0'
    sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
snap_num = sys.argv[4]
size = float(sys.argv[5])

rc('font', size = 15)
plt.clf()
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.12)
plt.xlabel('Radius [pc]')
plt.ylabel('Stellar mass density [M$_\odot$/pc$^\mathsf{3}$]')

plt.yscale('log')

nbin = 50

ntot, time, rarr = mp_snap_mc.read_mc(mp.prefix, dir_name, base_name, snap_num, nproc)
rb, denb = comp_star_den(rarr, nbin, size, time)
plt.plot(rb, denb, 'r-')

plt.xlim(0, size)
#plt.ylim(1.0E-5, 1.0E2)

#lg = plt.legend(loc = 0, prop = {'size': 15}) 
#lg.get_frame().set_linewidth(0)
    
figure_name = 'Star-den-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)

######################### end of main function ###########################
