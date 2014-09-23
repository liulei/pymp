#!/usr/bin/python

import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

def calc_bin(rp, vp, nbin, rsize):

    rbin = np.arange(nbin, dtype = float)
    vbin = np.zeros(nbin, dtype = float)
    count = np.zeros(nbin, dtype = float)
    dr = rsize / nbin
    rbin = (rbin + 0.5) * dr

    for i in range(0, len(rp)):
        
        index = int(rp[i] / dr)
        if(index < nbin):
            count[index] += 1.0
            vbin[index] += vp[i]

    vbin /= count
    return rbin, vbin

################################ collisional time scale ###################
rc('font', size = 15)

fig = plt.figure()
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.1)
ax = plt.subplot(111)

plt.xlabel('Radius [kpc]')
plt.ylabel('Collision time scale [Myr]')
#plt.xscale('log')
plt.yscale('log')

rsize = 20.0
nbin = 25

arr = np.loadtxt('cr0000.dat', dtype = float)
rb, cb = calc_bin(arr[:, 1], arr[:, 5], nbin, rsize)
plt.plot(rb, 1.0 / cb, 'k-', label = 't = 0')
 
arr = np.loadtxt('cr0003.dat', dtype = float)
rb, cb = calc_bin(arr[:, 1], arr[:, 5], nbin, rsize)
plt.plot(rb, 1.0 / cb, 'r-', label = 't = 0.3 Gyr')
 
arr = np.loadtxt('cr0005.dat', dtype = float)
rb, cb = calc_bin(arr[:, 1], arr[:, 5], nbin, rsize)
plt.plot(rb, 1.0 / cb, 'g-', label = 't = 0.5 Gyr')
 
arr = np.loadtxt('cr0010.dat', dtype = float)
rb, cb = calc_bin(arr[:, 1], arr[:, 5], nbin, rsize)
plt.plot(rb, 1.0 / cb, 'b-', label = 't = 1.0 Gyr')

plt.xlim(0.0, rsize)
plt.ylim(1.0, 1.0E8)
 
lg = plt.legend(loc = 4, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

plt.savefig('collision_time_scale.eps') 

################################ velocity dispersion ###################
rc('font', size = 15)

fig = plt.figure()
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.1)
ax = plt.subplot(111)

plt.xlabel('Radius [kpc]')
plt.ylabel('Velocity dispersion [km/s]')
#plt.xscale('log')
#plt.yscale('log')

rsize = 20.0
nbin = 25

arr = np.loadtxt('cr0000.dat', dtype = float)
rb, vb = calc_bin(arr[:, 1], arr[:, 4], nbin, rsize)
plt.plot(rb, vb, 'k-', label = 't = 0')
 
arr = np.loadtxt('cr0003.dat', dtype = float)
rb, vb = calc_bin(arr[:, 1], arr[:, 4], nbin, rsize)
plt.plot(rb, vb, 'r-', label = 't = 0.3 Gyr')
 
arr = np.loadtxt('cr0005.dat', dtype = float)
rb, vb = calc_bin(arr[:, 1], arr[:, 4], nbin, rsize)
plt.plot(rb, vb, 'g-', label = 't = 0.5 Gyr')
 
arr = np.loadtxt('cr0010.dat', dtype = float)
rb, vb = calc_bin(arr[:, 1], arr[:, 4], nbin, rsize)
plt.plot(rb, vb, 'b-', label = 't = 1.0 Gyr')

plt.xlim(0.0, rsize)
plt.ylim(0.0, 80.0)
 
lg = plt.legend(loc = 1, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

plt.savefig('cold_dispersion.eps') 

