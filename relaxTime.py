#!/usr/bin/python

from numpy import *
import numpy as np
import mp
import mp_snap_mc
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys
import os

if len(sys.argv) < 9:
	print 'relaxTime.py: not enough parameter!'
	print '\tUsage: relaxTime.py dir_name base_name nproc snap_num x y z rmax'
	print '\tExample: relaxTime.py MCT-7 dwarf 4 0008 -18.0 -25.0 -45.0 10.0'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
snap_num = sys.argv[4]
x = float(sys.argv[5])
y = float(sys.argv[6])
z = float(sys.argv[7])
rmax = float(sys.argv[8])

ntot = 0
ntot, time, arr = mp_snap_mc.read_mc(mp.prefix, dir_name, base_name, snap_num, nproc)

id1 = (arr['type'] == mp.TYPE_STAR_PARAL)
id2 = (arr['t_dead'] > time)
id3 = (arr['ss_type'] >= 0)

ids = np.logical_and(id1, id2)
ids = np.logical_and(ids, id3)
ids = np.where(ids)
arr = arr[ids]

arr['pos'] *= 1E3 # convert to pc

dx = arr['pos'][:, 0] - x
dy = arr['pos'][:, 1] - y
dz = arr['pos'][:, 2] - z

r2 = dx * dx + dy * dy + dz * dz
id5 = np.where(r2 < rmax * rmax)
arr = arr[id5]
r2 = r2[id5]

mtot = np.sum(arr['mass'])

x0 = np.sum(arr['mass'] * arr['pos'][:, 0])
y0 = np.sum(arr['mass'] * arr['pos'][:, 1])
z0 = np.sum(arr['mass'] * arr['pos'][:, 2])

vx0 = np.sum(arr['mass'] * arr['vel'][:, 0])
vy0 = np.sum(arr['mass'] * arr['vel'][:, 1])
vz0 = np.sum(arr['mass'] * arr['vel'][:, 2])

vx20 = np.sum(arr['mass'] * arr['vel'][:, 0] * arr['vel'][:, 0])
vy20 = np.sum(arr['mass'] * arr['vel'][:, 1] * arr['vel'][:, 1])
vz20 = np.sum(arr['mass'] * arr['vel'][:, 2] * arr['vel'][:, 2])

x0 /= mtot
y0 /= mtot
z0 /= mtot

vx0 /= mtot
vy0 /= mtot
vz0 /= mtot

vx20 = vx20 / mtot - vx0 * vx0
vy20 = vy20 / mtot - vy0 * vy0
vz20 = vz20 / mtot - vz0 * vz0

print 'Total mass:', mtot
print 'Position:', x0, y0, z0
print 'Velocity (bulk):', vx0, vy0, vz0
print 'Velocity (dispersion):', np.sqrt(vx20), np.sqrt(vy20), np.sqrt(vz20)

dx = arr['pos'][:, 0] - x0
dy = arr['pos'][:, 1] - y0
dz = arr['pos'][:, 2] - z0

print 'Total number of stars:', np.size(arr)
print 'Total stellar mass (Msol):', mtot

N = np.size(arr)
ma = mtot / N
print 'Average mass (Msol): ', ma
rho = mtot / (4. / 3. * mp.Pi * rmax * rmax * rmax)
print 'Average density (Msol/pc^3): ', rho

sig = np.sqrt(vx20 + vy20 + vz20)
print 'Velocity dispersion (km/s): ', sig

#trelax = 1.8E1 / np.log(0.4 * N) * np.power(sig / np.sqrt(3.0) / 10.0, 3) / ma * (1E3 / rho)
trelax = 0.65 / np.log(0.4 * N * 2) * np.power(mtot * 2 / 1E5, 0.5) / ma * np.power(rmax, 1.5)
print 'Relaxation time (Gyr): ', trelax
