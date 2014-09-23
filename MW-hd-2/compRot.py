#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

def calc_vel_bins(r, v, nbins, rsize):

    dr = rsize / nbins
    rb = np.arange(0, nbins, dtype = float) + 0.5
    rb *= dr

    va = np.zeros(nbins, dtype = float)
    vdisp = np.zeros(nbins, dtype = float)
    count = np.zeros(nbins, dtype = float)

    for i in range(0, len(r)):

        id = int(r[i] / dr)
        if id < nbins:
            va[id] += v[i]
            vdisp[id] += v[i] * v[i]
            count[id] += 1.0

    va /= count
    vdisp = np.sqrt(vdisp / count - va * va)

    return rb, va, vdisp

if len(sys.argv) < 5:
    print 'rrotp: not enough parameter!'
    print '\tUsage: rrotp.py dir_name base_name nproc rsize'
    print '\tExample: rrotp.py MW-hd-2 MW 8 20.0'
    sys.exit(0)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
rsize = float(sys.argv[4])

nbins = 60
lw = 2

rc('font', size = 15)

plt.xlabel('Radius [kpc]')
plt.ylabel('Circular velocity [km/s]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

################################# 0.5 Gyr  ############################
snap_num = '0001'

ntot = 0
ntot, time, arr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
R = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
R = np.sqrt(R)
z = arr['pos'][:, 2]
Rtan = -arr['pos'][:, 1] * arr['vel'][:, 0] + arr['pos'][:, 0] * arr['vel'][:, 1]
v_tan = Rtan / R
v_z = arr['vel'][:, 2]

id1 = arr['type'] == mp.TYPE_STAR_PARAL
id2 = np.fabs(z < 10.0)
id3 = np.logical_and(id1, id2)
ids = np.where(id3)
r = R[ids]
v = v_tan[ids]
rb, va, vdisp = calc_vel_bins(r, v, nbins, rsize)

plt.plot(rb, va, 'r-', linewidth = lw, label = 't = 0.5 Gyr')
plt.plot(rb, vdisp, 'r--', linewidth = lw)

################################# 1.0 Gyr  ############################
snap_num = '0002'

ntot = 0
ntot, time, arr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
R = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
R = np.sqrt(R)
z = arr['pos'][:, 2]
Rtan = -arr['pos'][:, 1] * arr['vel'][:, 0] + arr['pos'][:, 0] * arr['vel'][:, 1]
v_tan = Rtan / R
v_z = arr['vel'][:, 2]

id1 = arr['type'] == mp.TYPE_STAR_PARAL
id2 = np.fabs(z < 10.0)
id3 = np.logical_and(id1, id2)
ids = np.where(id3)
r = R[ids]
v = v_tan[ids]
rb, va, vdisp = calc_vel_bins(r, v, nbins, rsize)

plt.plot(rb, va, 'c-', linewidth = lw, label = 't = 1.0 Gyr')
plt.plot(rb, vdisp, 'c--', linewidth = lw)

################################# 3.0 Gyr  ############################
snap_num = '0006'

ntot = 0
ntot, time, arr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
R = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
R = np.sqrt(R)
z = arr['pos'][:, 2]
Rtan = -arr['pos'][:, 1] * arr['vel'][:, 0] + arr['pos'][:, 0] * arr['vel'][:, 1]
v_tan = Rtan / R
v_z = arr['vel'][:, 2]

id1 = arr['type'] == mp.TYPE_STAR_PARAL
id2 = np.fabs(z < 10.0)
id3 = np.logical_and(id1, id2)
ids = np.where(id3)
r = R[ids]
v = v_tan[ids]
rb, va, vdisp = calc_vel_bins(r, v, nbins, rsize)

plt.plot(rb, va, 'm-', linewidth = lw, label = 't = 3.0 Gyr')
plt.plot(rb, vdisp, 'm--', linewidth = lw)

plt.xlim(0, rsize)
plt.ylim(0.0, 200.0)

lg = plt.legend(prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'Comp-rot-star-' + dir_name + '.png'
plt.savefig(figure_name)

############################# cold #################################

plt.clf()

plt.xlabel('Radius [kpc]')
plt.ylabel('Circular velocity [km/s]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

################################# 0.5 Gyr  ############################
snap_num = '0001'

ntot = 0
ntot, time, arr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
R = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
R = np.sqrt(R)
z = arr['pos'][:, 2]
Rtan = -arr['pos'][:, 1] * arr['vel'][:, 0] + arr['pos'][:, 0] * arr['vel'][:, 1]
v_tan = Rtan / R
v_z = arr['vel'][:, 2]

id1 = arr['type'] == mp.TYPE_COLD
id2 = np.fabs(z < 10.0)
id3 = np.logical_and(id1, id2)
ids = np.where(id3)
r = R[ids]
v = v_tan[ids]
rb, va, vdisp = calc_vel_bins(r, v, nbins, rsize)

plt.plot(rb, va, 'r-', linewidth = lw, label = 't = 0.5 Gyr')
plt.plot(rb, vdisp, 'r--', linewidth = lw)

################################# 1.0 Gyr  ############################
snap_num = '0002'

ntot = 0
ntot, time, arr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
R = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
R = np.sqrt(R)
z = arr['pos'][:, 2]
Rtan = -arr['pos'][:, 1] * arr['vel'][:, 0] + arr['pos'][:, 0] * arr['vel'][:, 1]
v_tan = Rtan / R
v_z = arr['vel'][:, 2]

id1 = arr['type'] == mp.TYPE_COLD
id2 = np.fabs(z < 10.0)
id3 = np.logical_and(id1, id2)
ids = np.where(id3)
r = R[ids]
v = v_tan[ids]
rb, va, vdisp = calc_vel_bins(r, v, nbins, rsize)

plt.plot(rb, va, 'c-', linewidth = lw, label = 't = 1.0 Gyr')
plt.plot(rb, vdisp, 'c--', linewidth = lw)

################################# 3.0 Gyr  ############################
snap_num = '0006'

ntot = 0
ntot, time, arr = mp.read_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
R = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
R = np.sqrt(R)
z = arr['pos'][:, 2]
Rtan = -arr['pos'][:, 1] * arr['vel'][:, 0] + arr['pos'][:, 0] * arr['vel'][:, 1]
v_tan = Rtan / R
v_z = arr['vel'][:, 2]

id1 = arr['type'] == mp.TYPE_COLD
id2 = np.fabs(z < 10.0)
id3 = np.logical_and(id1, id2)
ids = np.where(id3)
r = R[ids]
v = v_tan[ids]
rb, va, vdisp = calc_vel_bins(r, v, nbins, rsize)

plt.plot(rb, va, 'm-', linewidth = lw, label = 't = 3.0 Gyr')
plt.plot(rb, vdisp, 'm--', linewidth = lw)

plt.xlim(0, rsize)
plt.ylim(0.0, 200.0)

lg = plt.legend(prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'Comp-rot-cold-' + dir_name + '.png'
plt.savefig(figure_name)


