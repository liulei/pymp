#!/usr/bin/python

import mp
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

ntot = 0
#ntot, arr = mp.read_paral(mp.prefix, '10-1.16', '10-1', '0005', 16)
#print 'total particles in file:', ntot

ntot, arr = mp.read_single(mp.prefix, 'PK-7', '0001')
print 'total particles in file:', ntot
