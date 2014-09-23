#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from mp import *
from matplotlib import *
from matplotlib import ticker, colors, colorbar, mpl
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 5:
    print 'obsOFe.py: not enough parameter!'
    print '\tUsage: obsOFe.py dir_name base_name nproc snap_num'
    print '\tExample: obsOFe.py MW-hd-2 MW 8 0006'
    sys.exit(0)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
snap_num = sys.argv[4]

rc('font', size = 15)

ntot = 0
ntot, time, arr = read_paral(prefix, dir_name, base_name, snap_num, nproc)

mass = arr['mass'][:]

Z0 = 5.0E-4

frac_O = 8.9 - 12.0 + np.log10(Z0 / 0.02)
frac_O = 16.0 * np.power(10.0, frac_O)

frac_Fe = 7.55 - 12.0 + np.log10(Z0 / 0.02)
frac_Fe = 56.0 * np.power(10.0, frac_N)

O = arr['mass_Z'][:, ID_O] + mass * 0.75 * frac_O
Fe = arr['mass_Z'][:, ID_Fe] + mass * 0.75 * frac_Fe


idw = np.where(arr['type'] == TYPE_WARM)
idc = np.where(arr['type'] == TYPE_COLD)
ids = np.where(arr['type'] == TYPE_STAR_PARAL)

mw = mass[idw]
mc = mass[idc]
ms = mass[ids]

Ow = O[idw]
Oc = O[idc]
Os = O[ids]

Ow = np.log10(Ow / (mw * 0.75) / 16.0) + 12.0
Oc = np.log10(Oc / (mc * 0.75) / 16.0) + 12.0
Os = np.log10(Os / (ms * 0.75) / 16.0) + 12.0

Few = Fe[idw]
Fec = Fe[idc]
Fes = Fe[ids]

Few = np.log10(Few / (mw * 0.75) / 56.0) + 12.0
Fec = np.log10(Fec / (mc * 0.75) / 56.0) + 12.0
Fes = np.log10(Fes / (ms * 0.75) / 56.0) + 12.0

OFew = Ow - Few
OFec = Oc - Fec
OFes = Os - Fes

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
r = np.sqrt(r)

rw = r[idw]
rc = r[idc]
rs = r[ids]

################################### figure #############################

fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(5)
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15, \
    hspace = 0.25)

############################# [O/Fe] ~ [Fe/H] ##########################

ax = plt.subplot(111)

plt.xlabel('12+log[Fe/H]')
plt.ylabel('log[O/Fe]')

ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

ssize = 0.5

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()

plt.his2d(OFec, Fec, bins = 50, cmap = cmap, )

plt.xlim(7.55 + np.log10(5.0E-4 / 0.02), 9.0)
plt.ylim(-3.0, 3.0)

figure_name = 'Obs-OFe-%s-%s.png' % (dir_name, snap_num)

plt.savefig(figure_name)

