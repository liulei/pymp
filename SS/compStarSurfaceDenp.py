#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp


def comp_star_surface_den(arr, nbin, size):

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
            mb[id] += mass[i]

    dV = np.power(rb + drh, 2) - np.power(rb - drh, 2)
    dV *= np.pi
    
    denb = mb / dV # Msol / kpc^2
    denb *= 1.0E-6 # Msol / pc^2

    return rb, denb

############################## mass density ##############################


if len(sys.argv) < 5:
    print 'compStarSurfaceDenp: not enough parameter!'
    print '\tUsage: compStarSurfaceDenp.py dir_name base_name nproc size'
    print '\tExample: showStarSurfaceDenp.py SS-5E7-iso-4 dwarf 16 4.0'
    sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
size = float(sys.argv[4])

rc('font', size = 15)
plt.clf()
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.12)
plt.xlabel('Radius [kpc]')
plt.ylabel('Surface stellar mass density [M$_\odot$/pc$^\mathsf{2}$]')

plt.yscale('log')

nbin = 50

snap_num = '0050'
ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
rb, denb = comp_star_surface_den(rarr, nbin, size)
plt.plot(rb, denb, 'r-', label = 't = 0.5 Gyr')

snap_num = '0100'
ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
rb, denb = comp_star_surface_den(rarr, nbin, size)
plt.plot(rb, denb, 'g-', label = 't = 1.0 Gyr')

snap_num = '0150'
ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
rb, denb = comp_star_surface_den(rarr, nbin, size)
plt.plot(rb, denb, 'b-', label = 't = 1.5 Gyr')

plt.xlim(0, size)
plt.ylim(1.0E-5, 1.0E2)

lg = plt.legend(loc = 0, prop = {'size': 15}) 
lg.get_frame().set_linewidth(0)
    
figure_name = 'comp-Star-surface-den-' + dir_name + '.png'
plt.savefig(figure_name)

figure_name = 'comp-Star-surface-den-' + dir_name + '.eps'
plt.savefig(figure_name)


######################### end of main function ###########################


