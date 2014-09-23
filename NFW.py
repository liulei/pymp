#!/usr/bin/python

import sys
import os
import numpy as np
from mp import *

if len(sys.argv) < 4:
	print 'NFW: not enough parameter!'
	print '\tUsage: NFW.py rho_0(Msol/pc^3) R_s(kpc) r(kpc)'
	print '\tExample: NFW.py 0.00846 20.2 10.0'
	sys.exit(1)

rho_0 = float(sys.argv[1])
R_s = float(sys.argv[2])
r = float(sys.argv[3])

rho_0 *= (Msol / (pc * pc * pc))
R_s *= kpc
r *= kpc
M0 = 4.0 * Pi * rho_0 * R_s * R_s * R_s

xx = r / R_s
M = M0 * (np.log(1.0 + xx) - xx / (1.0 + xx))

print 'Total mass with in %g kpc: %E Msol' % (r / kpc, M / Msol)
