#!/export/home/liulei/local/bin/python

# Solar Nitrogen abundance: 7.86+-0.12
# arXiv:0903.3406

from numpy import *
import numpy as np
from mp import *
from matplotlib import *
#from matplotlib import ticker
import matplotlib.pyplot as plt
from math import *
import sys

def calc_bin(r, m, mz, nbin, rad):

    n = len(r)

    dr = rad / nbin
    rb = np.arange(nbin, dtype = float)
    rb = (rb + 0.5) * dr

    marr = np.zeros(nbin, dtype = float)
    mzarr = np.zeros(nbin, dtype = float)

    for i in range(0, n):

        id = int(r[i] / dr)

        if (id >= 0 and id < nbin):

            marr[id] += m[i]
            mzarr[id] += mz[i]

    zb = np.log10(mzarr / (marr * 0.75) / 14.0) + 12.0
    return rb, zb

def calc_r_N(arr, nbin, rad):

# assume initial nitrogen of -2 relative to solar value

    zini = 7.86 - 12.0 + np.log10(5.0E-4 / 0.02)
    zini = 14.0 * np.power(10.0, zini)

    Z = arr['mass_Z'][:, ID_N]
    mass = arr['mass'][:]
    Z += mass * 0.75 * zini

    idw = np.where(arr['type'] == TYPE_WARM)
    idc = np.where(arr['type'] == TYPE_COLD)
    ids = np.where(arr['type'] == TYPE_STAR_PARAL)

    r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
        + arr['pos'][:, 2] * arr['pos'][:, 2]  
    r = np.sqrt(r)

    rw = r[idw]
    rc = r[idc]
    rs = r[ids]

    mw = mass[idw]
    mc = mass[idc]
    ms = mass[ids]
    
    zw = Z[idw]
    zc = Z[idc]
    zs = Z[ids]

    rwb, zwb = calc_bin(rw, mw, zw, nbin, rad)
    rcb, zcb = calc_bin(rc, mc, zc, nbin, rad)
    rsb, zsb = calc_bin(rs, ms, zs, nbin, rad)

    return rwb, zwb, zcb, zsb

if len(sys.argv) < 5:
	print 'col_rN: not enough parameter!'
	print '\tUsage: col_rN.py dir_name base_name nproc size'
	print '\tExample: col_rN.py MW-11.1 MW 8 20.0'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
rsize = float(sys.argv[4])

rc('font', size = 15)
fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(6)
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.10, \
        hspace = 0.0)

nullFormatter = ticker.NullFormatter()
majorLocator = ticker.MultipleLocator(0.2)

nbin = 50
    
############################## t = 0.5 Gyr ###############################
snap_num = '0001'
ntot, time, arr = read_paral(prefix, dir_name, base_name, snap_num, nproc)

rb, zwb, zcb, zsb = calc_r_N(arr, nbin, rsize)

ax = fig.add_subplot(311)

plt.xlabel('Radius [kpc]')
plt.ylabel('12+log[N/H]')

plt.plot(rb, zwb, 'r-')
plt.plot(rb, zcb, 'g-')
plt.plot(rb, zsb, 'b-')

ax.xaxis.set_major_formatter(nullFormatter)
ax.yaxis.set_major_locator(majorLocator)

plt.xlim(0, rsize)
plt.ylim(6.2, 7.4)

############################## t = 1.0 Gyr ###############################
snap_num = '0002'
ntot, time, arr = read_paral(prefix, dir_name, base_name, snap_num, nproc)

rb, zwb, zcb, zsb = calc_r_N(arr, nbin, rsize)

ax = fig.add_subplot(312)

plt.xlabel('Radius [kpc]')
plt.ylabel('12+log[N/H]')

plt.plot(rb, zwb, 'r-')
plt.plot(rb, zcb, 'g-')
plt.plot(rb, zsb, 'b-')

ax.xaxis.set_major_formatter(nullFormatter)
ax.yaxis.set_major_locator(majorLocator)

plt.xlim(0, rsize)
plt.ylim(6.2, 7.4)

############################## t = 3.0 Gyr ###############################
snap_num = '0006'
ntot, time, arr = read_paral(prefix, dir_name, base_name, snap_num, nproc)

rb, zwb, zcb, zsb = calc_r_N(arr, nbin, rsize)

ax = fig.add_subplot(313)

plt.xlabel('Radius [kpc]')
plt.ylabel('12+log[N/H]')

plt.plot(rb, zwb, 'r-')
plt.plot(rb, zcb, 'g-')
plt.plot(rb, zsb, 'b-')

#ax.xaxis.set_major_formatter(nullFormatter)
ax.yaxis.set_major_locator(majorLocator)

plt.xlim(0, rsize)
plt.ylim(6.2, 7.4)

############################# label ######################################
label = 't = 0.5 Gyr'
plt.figtext(0.8, 0.91, label, ha = 'center', size = 15)

label = 't = 1.0 Gyr'
plt.figtext(0.8, 0.63, label, ha = 'center', size = 15)

label = 't = 3.0 Gyr'
plt.figtext(0.8, 0.35, label, ha = 'center', size = 15)

figure_name = 'r-N-' + dir_name + '.png'
plt.savefig(figure_name)
