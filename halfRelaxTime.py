#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

if len(sys.argv) < 4:
    print 'RelaxTime: not enough parameter!'
    print '\t Usage: RelaxTime.py par_numb total_m(Msol) rh(pc)'
    print '\t Example: RelaxTime.py 285402 4.58E5 19.4'
    sys.exit(1)

N = int(sys.argv[1])
M = float(sys.argv[2])
rh = float(sys.argv[3])
ma = M / N
print 'Average mass: %.3f Msol' % ma

sig2 = 0.4 * G * M * Msol / (rh * pc) # in (m/s)^2
sig2 /= 1E6 # convert to (km/s)^2
sig = np.sqrt(sig2)
print 'Estimated velocity dispersion: %.3f km/s' % sig

trelax = 6.5E2 / np.log(0.4 * N) * np.sqrt(M / 1E5) / ma * np.power(rh, 1.5)
print 'Relaxation time: %.3f Myr' % trelax
