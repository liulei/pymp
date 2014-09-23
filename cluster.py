#!/export/home/liulei/program/cp-cd-sph/python

# Output is in nbody unit for nbody6++, and is read in the code with KZ(22) set
# to 2. RBAR and ZMBAR are printed out, should be set in the code.

from numpy import *
import numpy as np
import mc
import mc_snap
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys
import os

if len(sys.argv) < 9:
	print 'cluster.py: not enough parameter!'
	print '\tUsage: cluster.py dir_name base_name nproc snap_num x y z rmax'
	print '\tExample: cluster.py MCT-7 dwarf 4 0008 -18.0 -25.0 -45.0 10.0'
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
ntot, time, arr = mc_snap.read_mc(mc.prefix, dir_name, base_name, snap_num, nproc)

id1 = (arr['type'] == mc.TYPE_STAR_PARAL)
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

print 'Total star particle inside:', np.size(arr)

mtot = 0.0
x0 = 0.0
y0 = 0.0
z0 = 0.0
vx0 = 0.0
vy0 = 0.0
vz0 = 0.0
vx20 = 0.0
vy20 = 0.0
vz20 = 0.0

mtot = np.sum(arr['mass'])

x0 = np.sum(arr['mass'] * arr['pos'][:, 0])
y0 = np.sum(arr['mass'] * arr['pos'][:, 1])
z0 = np.sum(arr['mass'] * arr['pos'][:, 2])

vx0 = np.sum(arr['mass'] * arr['vel'][:, 0])
vy0 = np.sum(arr['mass'] * arr['vel'][:, 1])
vz0 = np.sum(arr['mass'] * arr['vel'][:, 2])

vx20 += np.sum(arr['mass'] * arr['vel'][:, 0] * arr['vel'][:, 0])
vy20 += np.sum(arr['mass'] * arr['vel'][:, 1] * arr['vel'][:, 1])
vz20 += np.sum(arr['mass'] * arr['vel'][:, 2] * arr['vel'][:, 2])

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

r2 = dx * dx + dy * dy + dz * dz

idx = np.argsort(r2)
r2s = r2[idx]
ms = arr['mass'][idx]
mh = 0.0
rh = 0.0
for i in range(0, np.size(ms)):
    mh += ms[i]
    if(mh > mtot * 0.5):
        rh = np.sqrt(r2s[i])
        break

print 'Half mass radius:', rh

print 'Total number of stars:', np.size(arr)
print 'Total stellar mass (Msol):', mtot
f = open('physical.10', 'w')
for i in range(0, np.size(arr)):
    f.write('%.5E\t%.5E\t%.5E\t%.5E\t%.5E\t%.5E\t%.5E\n' % \
    (arr['mass'][i], 
    arr['pos'][i, 0], arr['pos'][i, 1], arr['pos'][i, 2], \
    arr['vel'][i, 0], arr['vel'][i, 1], arr['vel'][i, 2]))
f.close()

cmd = 'p2n %d' % (np.size(arr))
os.system(cmd)
