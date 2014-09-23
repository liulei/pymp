#!/usr/bin/python

# Output is in nbody unit for nbody6++, and is read in the code with KZ(22) set
# to 2. RBAR and ZMBAR are printed out, should be set in the code.

from numpy import *
import numpy as np
import mp
import mp_snap_mc
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

# ZKIN in Msol * km/s * km/s, POT in 
def Energy(arr):
    
    ZKIN = 0.0
    POT = 0.0
    N = np.size(arr)
    for i in range(0, N):
        for j in range(i + 1, N):
            print i, j

            dx = arr['pos'][i, 0] - arr['pos'][j, 0]
            dy = arr['pos'][i, 1] - arr['pos'][j, 1]
            dz = arr['pos'][i, 2] - arr['pos'][j, 2]
            r = np.sqrt(dx * dx + dy * dy + dz * dz)
            r *= 1E3 # convert to pc
            POT += arr['mass'] / r

    for i in range(0, N):
        ZKIN += arr['mass'] * (arr['vel'][i, 0] * arr['vel'][i, 0] 
                + arr['vel'][i, 1] * arr['vel'][i, 1] 
                + arr['vel'][i, 2] * arr['vel'][i, 2])

    ZKIN *= 0.5
    return ZKIN, POT



if len(sys.argv) < 5:
	print 'con2nbody: not enough parameter!'
	print '\tUsage: con2nbody.py dir_name base_name nproc snap_num'
	print '\tExample: con2nbody MCT-7 dwarf 4 0015'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
snap_num = sys.argv[4]

ntot = 0
ntot, time, arr = mp_snap_mc.read_mc(mp.prefix, dir_name, base_name, snap_num, nproc)

id1 = (arr['type'] == mp.TYPE_STAR_PARAL)
id2 = (arr['t_dead'] > time)
id3 = (arr['ss_type'] >= 1) # exclude low mass type

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
	+ arr['pos'][:, 2] * arr['pos'][:, 2]
r = np.sqrt(r)
id4 = (r * 1000.0 < 100.0) # choose radius within 120 pc

ids = np.logical_and(id1, id2)
ids = np.logical_and(ids, id3)
ids = np.logical_and(ids, id4)
ids = np.where(ids)
arr = arr[ids]

cmr = np.zeros(3)
mtot = 0.0
for i in range(0, np.size(arr)):
    cmr[0] += arr['pos'][i, 0] * arr['mass'][i]
    cmr[1] += arr['pos'][i, 1] * arr['mass'][i]
    cmr[2] += arr['pos'][i, 2] * arr['mass'][i]
    mtot += arr['mass'][i]
cmr /= mtot
print 'Center of mass (pc):', cmr * 1000

for i in range(0, np.size(arr)):
    arr['pos'][i, 0] -= cmr[0] 
    arr['pos'][i, 1] -= cmr[1] 
    arr['pos'][i, 2] -= cmr[2]

cmv = np.zeros(3)
mtot = 0.0
for i in range(0, np.size(arr)):
    cmv[0] += arr['vel'][i, 0] * arr['mass'][i]
    cmv[1] += arr['vel'][i, 1] * arr['mass'][i]
    cmv[2] += arr['vel'][i, 2] * arr['mass'][i]
    mtot += arr['mass'][i]
cmv /= mtot

for i in range(0, np.size(arr)):
    arr['vel'][i, 0] -= cmv[0] 
    arr['vel'][i, 1] -= cmv[1] 
    arr['vel'][i, 2] -= cmv[2]

print 'Bulk velocity (km/s):', cmv

cmr = np.zeros(3)
mtot = 0.0
for i in range(0, np.size(arr)):
    cmr[0] += arr['pos'][i, 0] * arr['mass'][i]
    cmr[1] += arr['pos'][i, 1] * arr['mass'][i]
    cmr[2] += arr['pos'][i, 2] * arr['mass'][i]
    mtot += arr['mass'][i]
cmr /= mtot
print 'Center of mass after correction (pc):', cmr * 1000.0

print 'Total number of stars:', np.size(arr)
print 'Total stellar mass (Msol):', mtot
f = open('physical.10', 'w')
for i in range(0, np.size(arr)):
    f.write('%.5E\t%.5E\t%.5E\t%.5E\t%.5E\t%.5E\t%.5E\n' % \
    (arr['mass'][i], 
    arr['pos'][i, 0] * 1E3, arr['pos'][i, 1] * 1E3, arr['pos'][i, 2] * 1E3, \
    arr['vel'][i, 0], arr['vel'][i, 1], arr['vel'][i, 2]))
f.close()

ZKIN, POT = Energy(arr)

# nbody6 uses cgs, here we use SI
G = mp.G / (mp.pc * mp.pc * mp.pc / mp.Msol)
ZKIN = ZKIN * mp.km * mp.km / (mp.pc * mp.pc)
EPH = ZKIN - G * POT
print "EPH:", EPH
