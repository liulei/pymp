#!/usr/bin/python
# wc.py: plot energy component of warm and cold as a function of time.
# compare the result with supernova feedback

import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 2:
	print 'wcin: not enough parameter!'
	print '\t usage: wcin.py dir_name'
	print '\t example: wcin.py PK-7'
	sys.exit(0)

file_wc = prefix + '/' + sys.argv[1] + '/energy_wc.dat'

arr = np.loadtxt(file_wc, dtype = struct_wc)

time = arr['time'] * (TNORM / Myr)
ek_w = arr['ek_w'] * ENORM
eu_w = arr['eu_w'] * ENORM
ep_w = arr['ep_w'] * ENORM
epe_w = arr['epe_w'] * ENORM
ek_c = arr['ek_c'] * ENORM
eu_c = arr['eu_c'] * ENORM
ep_c = arr['ep_c'] * ENORM
epe_c = arr['epe_c'] * ENORM

file_e_trans = prefix + '/' + sys.argv[1] + '/energy_trans.dat'
earr = np.loadtxt(file_e_trans, dtype = float)

dt = earr[1, 0] - earr[0, 0]
te = earr[:, 0]
sn2 = dt * earr[:, 1]
sn1 = dt * earr[:, 3]

for i in range(1, len(earr)):
	sn2[i] += sn2[i - 1]
	sn1[i] += sn1[i - 1]

rc('font', size = 17)

plt.title(sys.argv[1])
plt.xlabel('Time [Myr]')
plt.ylabel('Energy [J]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.91, bottom = 0.12)
plt.yscale('log')
plt.plot(te, sn2, 'b-')
plt.plot(te, sn1, 'b--')
plt.plot(time, ek_w, 'r--')
plt.plot(time, eu_w, 'r-')
plt.plot(time, ek_c, 'g--')
plt.plot(time, eu_c, 'g-')
plt.xlim(0, 50.0)
plt.ylim(1E45, 1E51)

lg = plt.legend(('SNII Feedback', 'SNI Feedback', 'Kinetic Warm', \
	'Thermal Warm', 'Kinetic Cold', 'Thermal Cold'), loc = 0, ncol = 3, \
	prop = {'size': 12})
lg.get_frame().set_linewidth(0)

figure_name = 'wcin-' + sys.argv[1] + '.eps'
plt.savefig(figure_name)

