#!/usr/bin/python

from numpy import *
import numpy as np
from mp import *
from matplotlib import *
from matplotlib import ticker
import matplotlib.pyplot as plt
from math import *
import sys

def calc_r_O(r, m, mz, nbin, rad):

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


    zb = np.log10(mzarr / (marr * 0.75) / 16.0) + 12.0
    return rb, zb

def calc_r_N(r, m, mz, nbin, rad):

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

    zb = np.log10(mzarr / (marr * 0.75) / 14.0) + 12.0
    return rb, zb

def mid_r_z(r, z, nbin, rad):

    dr = rad / nbin
    drh = dr / 2.0
    rb = np.arange(nbin, dtype = float)
    rb = (rb + 0.5) * dr
    zb = np.zeros(nbin, dtype = float)

    for i in range(0, nbin):

        id1 = (r >  rb[i] - drh)
        id2 = (r <= rb[i] + drh)
        
        id3 = np.logical_and(id1, id2)
        idx = np.where(id3)
        
        rarr = z[idx]
        arr = np.sort(rarr)
        
        zb[i] = arr[len(arr) / 2]

    return rb, zb


if len(sys.argv) < 4:
    print 'ron.py: not enough parameter!'
    print '\tUsage: ron.py dir_name snap_num range'
    print '\tExample: ron.py PKc-1 0001 5'
    sys.exit(0)

NH_sol = 7.86 # arXiv:0903.3406 [astro-ph]
OH_sol = 8.65 # Asplund (2005)
FeH_sol = 7.51 # McWilliam (1997)

dir_name = sys.argv[1]
snap_num = sys.argv[2]
rsize = float(sys.argv[3])

ntot = 0
ntot, time, arr = read_single(prefix, dir_name, snap_num)

rc('font', size = 16)

O = arr['mass_Z'][:, ID_O]
N = arr['mass_Z'][:, ID_N]

mass = arr['mass'][:]
idw = np.where(arr['type'] == TYPE_WARM)
idc = np.where(arr['type'] == TYPE_COLD)
ids = np.where(arr['type'] == TYPE_STAR_SINGLE)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
    + arr['pos'][:, 2] * arr['pos'][:, 2]  
r = np.sqrt(r)

nbin = 20
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

Ow = O[idw]
Oc = O[idc]
Os = O[ids]

rwb, Owb = calc_r_O(rw, mw, Ow, nbin, rad)
rcb, Ocb = calc_r_O(rc, mc, Oc, nbin, rad)
rsb, Osb = calc_r_O(rs, ms, Os, nbin, rad)

Ow = np.log10(Ow / (mw * 0.75) / 16.0) + 12.0
Oc = np.log10(Oc / (mc * 0.75) / 16.0) + 12.0
Os = np.log10(Os / (ms * 0.75) / 16.0) + 12.0

#rwb, Owb = mid_r_z(rw, Ow, nbin, rad)
#rcb, Ocb = mid_r_z(rc, Oc, nbin, rad)
#rsb, Osb = mid_r_z(rs, Os, nbin, rad)

Nw = N[idw]
Nc = N[idc]
Ns = N[ids]

rwb, Nwb = calc_r_N(rw, mw, Nw, nbin, rad)
rcb, Ncb = calc_r_N(rc, mc, Nc, nbin, rad)
rsb, Nsb = calc_r_N(rs, ms, Ns, nbin, rad)

Nw = np.log10(Nw / (mw * 0.75) / 14.0) + 12.0
Nc = np.log10(Nc / (mc * 0.75) / 14.0) + 12.0
Ns = np.log10(Ns / (ms * 0.75) / 14.0) + 12.0

#rwb, Nwb = mid_r_z(rw, Nw, nbin, rad)
#rcb, Ncb = mid_r_z(rc, Nc, nbin, rad)
#rsb, Nsb = mid_r_z(rs, Ns, nbin, rad)

############################ figure ####################################

fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(6)
fig.subplots_adjust(left = 0.14, right = 0.95, top = 0.96, bottom = 0.10, \
    hspace = 0.0)

############################ r - [O/H] ##################################

ax = plt.subplot(211)
#tit = dir_name + ' ' + snap_num
#plt.title(tit)
#plt.xlabel('Radius [kpc]')
plt.ylabel('[O/H]')
#ax.xaxis.set_major_locator(ticker.NullLocator())
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

#plt.scatter(rw, Ow, c = 'r', s = 1.0 ,edgecolors = 'none')
#plt.scatter(rc, Oc, c = 'g', s = 1.0 ,edgecolors = 'none')
#plt.scatter(rs, Os, c = 'b', s = 1.0 ,edgecolors = 'none')

plt.plot(rwb, Owb - OH_sol, 'r-')
plt.plot(rcb, Ocb - OH_sol, 'g-')
plt.plot(rsb, Osb - OH_sol, 'b-')

plt.xlim(0, rsize)
#plt.ylim(4.1, 9.0)
plt.ylim(4.1 - OH_sol, 9.0 - OH_sol)

############################ r - [N/H] ##################################

ax = plt.subplot(212)

plt.xlabel('Radius [kpc]')
plt.ylabel('[N/H]')

ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

#plt.scatter(rw, Nw, c = 'r', s = 1.0 ,edgecolors = 'none')
#plt.scatter(rc, Nc, c = 'g', s = 1.0 ,edgecolors = 'none')
#plt.scatter(rs, Ns, c = 'b', s = 1.0 ,edgecolors = 'none')

plt.plot(rwb, Nwb - NH_sol, 'r-')
plt.plot(rcb, Ncb - NH_sol, 'g-')
plt.plot(rsb, Nsb - NH_sol, 'b-')

plt.xlim(0, rsize)
#plt.ylim(5.6, 7.1)
plt.ylim(5.6 - NH_sol, 7.1 - NH_sol)

figure_name = 'r-ON-' + dir_name + '-' + snap_num + '.eps'
plt.savefig(figure_name)

