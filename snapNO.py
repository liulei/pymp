#!/usr/bin/python

from numpy import *
import numpy as np
from mp import *
from matplotlib import *
from matplotlib import ticker
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 3:
    print 'snapNO.py: not enough parameter!'
    print '\tUsage: snapNO.py dir_name snap_num'
    print '\tExample: snapNO.py PKc-1 0001'
    sys.exit(0)

dir_name = sys.argv[1]
snap_num = sys.argv[2]

ntot = 0
ntot, time, arr = read_single(prefix, dir_name, snap_num)

rc('font', size = 16)

O = arr['mass_Z'][:, ID_O]
N = arr['mass_Z'][:, ID_N]


mass = arr['mass'][:]
idw = np.where(arr['type'] == TYPE_WARM)
idc = np.where(arr['type'] == TYPE_COLD)
ids = np.where(arr['type'] == TYPE_STAR_SINGLE)

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
    + arr['pos'][:, 2] * arr['pos'][:, 2]  
r = np.sqrt(r)

rw = r[idw]
rc = r[idc]
rs = r[ids]

mw = mass[idw]
mc = mass[idc]
ms = mass[ids]

Ow = O[idw]
Oc = O[idc]
Os = O[ids]

Ow = np.log10(Ow / (mw * 0.75) / 16.0) + 12.0
Oc = np.log10(Oc / (mc * 0.75) / 16.0) + 12.0
Os = np.log10(Os / (ms * 0.75) / 16.0) + 12.0

Nw = N[idw]
Nc = N[idc]
Ns = N[ids]

Nw = np.log10(Nw / (mw * 0.75) / 14.0) + 12.0
Nc = np.log10(Nc / (mc * 0.75) / 14.0) + 12.0
Ns = np.log10(Ns / (ms * 0.75) / 14.0) + 12.0

NOw = Nw - Ow
NOc = Nc - Oc
NOs = Ns - Os

################################### figure #############################

fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(5)
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15, \
    hspace = 0.25)

############################# [N/O] ~ [O/H] ##########################

ax = plt.subplot(111)

plt.xlabel('12+log(O/H)')
plt.ylabel('log(N/O)')

ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 1))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 1.0))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

plt.scatter(Ow, NOw, c = 'r', s = 1.0, edgecolors = 'none')
plt.scatter(Oc, NOc, c = 'g', s = 1.0, edgecolors = 'none')
plt.scatter(Os, NOs, c = 'b', s = 1.0, edgecolors = 'none')

# include observation results (van Zee 1997):
if True:
    obs = np.loadtxt('Obs/vanZee1997a_NO_All.dat', dtype = float)
    obs_NO = obs[:, 0] - obs[:, 2]
#    print obs_NO
    obs_OH = obs[:, 2]
    plt.plot(obs_OH, obs_NO, 'k1', ms = 6.0, mew = 2)
    
plt.xlim(2.0, 10.0)
plt.ylim(-3.0, 4.0)

figure_name = 'snap-NO-' + sys.argv[1] + '-' + sys.argv[2] + '.png'

plt.savefig(figure_name)



