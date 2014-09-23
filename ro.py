#!/usr/bin/python

from numpy import *
import numpy as np
from mp import *
from matplotlib import *
from matplotlib import ticker
import matplotlib.pyplot as plt
from math import *
import sys

def calc_r_z(r, m, mz, nbin, rad):

    n = len(r)

    dr = rad / nbin
    drh = dr / 2.0
    rb = np.arange(nbin, dtype = float)
    rb = (rb + 0.5) * dr

    marr = np.zeros(nbin, dtype = float)
    mzarr = np.zeros(nbin, dtype = float)

    count = np.zeros(nbin)

    for i in range(0, n):

        rr = r[i]

        for j in range(0, nbin):

            if rb[j] - drh < rr and rb[j] + drh >= rr:

#                print 'j:', j
                
                marr[j] += m[i]
                mzarr[j] += mz[i]
                count[j] += 1


    zb = np.log10(mzarr / (marr * 0.75) / 16.0) + 12.0 - 8.9
    return rb, zb


if len(sys.argv) < 4:
    print 'ro.py: not enough parameter!'
    print '\tUsage: ro.py dir_name snap_num range'
    print '\tExample: ro.py PKc-1 0001 5'
    sys.exit(0)

dir_name = sys.argv[1]
snap_num = sys.argv[2]
rsize = float(sys.argv[3])

ntot = 0
ntot, arr = read_single(prefix, dir_name, snap_num)

rc('font', size = 20)

Z = arr['mass_Z'][:, ID_O]
mass = arr['mass'][:]
idw = np.where(arr['type'] == TYPE_WARM)
idc = np.where(arr['type'] == TYPE_COLD)
ids = np.where(arr['type'] == TYPE_STAR_SINGLE)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
    + arr['pos'][:, 2] * arr['pos'][:, 2]  
r = np.sqrt(r)

nbin = 25
rad = rsize

rwb = np.zeros(nbin)
rcb = np.zeros(nbin)
rsb = np.zeros(nbin)

zwb = np.zeros(nbin)
zcb = np.zeros(nbin)
zsb = np.zeros(nbin)

rw = r[idw]
rc = r[idc]
rs = r[ids]

mw = mass[idw]
mc = mass[idc]
ms = mass[ids]

zw = Z[idw]
zc = Z[idc]
zs = Z[ids]

rwb, zwb = calc_r_z(rw, mw, zw, nbin, rad)
rcb, zcb = calc_r_z(rc, mc, zc, nbin, rad)
rsb, zsb = calc_r_z(rs, ms, zs, nbin, rad)

zw = np.log10(zw / (mw * 0.75) / 16.0) + 12.0 - 8.9
zc = np.log10(zc / (mc * 0.75) / 16.0) + 12.0 - 8.9
zs = np.log10(zs / (ms * 0.75) / 16.0) + 12.0 - 8.9

tit = dir_name + ' ' + snap_num
plt.title(tit)
plt.xlabel('Radius [kpc]')
plt.ylabel('Oxygen abundance [O/H]')

plt.plot(rwb, zwb, 'r-')
plt.plot(rcb, zcb, 'g-')
plt.plot(rsb, zsb, 'b-')
plt.scatter(rw, zw, c = 'r', s = 0.1, edgecolors = 'none')
plt.scatter(rc, zc, c = 'g', s = 1.0, edgecolors = 'none')
#plt.scatter(rs, zs, c = 'b', s = 1.0, edgecolors = 'none')

plt.xlim(0, rsize)
plt.ylim(-4.0, 1.0)

figure_name = 'r-Oxygen-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)

