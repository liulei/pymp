#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import mp

if len(sys.argv) < 2:
	print 'cs.py: not enough parameter!'
	print '\tUsage: ./cs.py T[K]'
	sys.exit(0)

T = float(sys.argv[1])
mproton = 1.67E-27
result = np.sqrt(mp.k_gas * T / 1.3 / mproton) / 1.E3
print 'Sound speed: %.3e km/s' % result
