#!/export/home/liulei/local/bin/python

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


    zb = np.log10(mzarr / (marr * 0.75) / 16.0) + 12.0
    return rb, zb

def linear(xarray, a, b):
    return  a + b * xarray

if len(sys.argv) < 6:
    print 'obsRO.py: not enough parameter!'
    print '\tUsage: obsRO.py dir_name base_name snap_num nproc range'
    print '\tExample: obsRO.py MW-hd-2 MW 0006 8 10.0'
    sys.exit(0)

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])
rsize = float(sys.argv[5])

obs_name = ['NGC 2403', 'NGC 4395']
obs_ZC = [8.7, 8.48]
err_ZC = [0.07, 0.13]
obs_grad = [-0.074, -0.037]
err_grad = [0.013, 0.022]

data_name = 'R-Oxy-%s-%s.dat' % (dir_name, snap_num)
simu = np.loadtxt(data_name, dtype = float)

rc('font', size = 16)

plt.xlabel('Radius [kpc]')
plt.ylabel('12+log[O/H]')

rb = np.arange(0, rsize * 1.1, 0.1)

y0u = linear(rb, obs_ZC[0] + err_ZC[0], obs_grad[0] + err_grad[0])
y0l = linear(rb, obs_ZC[0] - err_ZC[0], obs_grad[0] - err_grad[0])

y1u = linear(rb, obs_ZC[1] + err_ZC[1], obs_grad[1] + err_grad[1])
y1l = linear(rb, obs_ZC[1] - err_ZC[1], obs_grad[1] - err_grad[1])

plt.fill_between(rb, y0u, y0l, facecolor = brown, edgecolor = 'none', alpha = 0.3)
plt.fill_between(rb, y1u, y1l, facecolor = 'm', edgecolor = 'none', alpha = 0.2)

plt.plot(simu[:, 0], simu[:, 2], 'g-', linewidth = 4, label = 'Model')
plt.plot(rb, linear(rb, obs_ZC[0], obs_grad[0]), c = brown, ls = '--', \
        linewidth = 2, label = obs_name[0])
plt.plot(rb, linear(rb, obs_ZC[1], obs_grad[1]), 'm--', linewidth = 2, \
        label = obs_name[1])

lg = plt.legend()
lg.get_frame().set_linewidth(0)

plt.xlim(0, rsize)
plt.ylim(7.8, 8.8)

figure_name = 'Obs-Oxygen-' + dir_name + '-' + snap_num + '.png'
plt.savefig(figure_name)

