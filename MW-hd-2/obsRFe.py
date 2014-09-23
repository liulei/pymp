#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from mp import *
from matplotlib import *
from matplotlib import ticker, colors, colorbar, mpl
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 6:
    print 'obsRFe.py: not enough parameter!'
    print '\tUsage: obsRFe.py dir_name base_name nproc snap_num rsize'
    print '\tExample: obsRFe.py MW-hd-2 MW 8 0006 10.0'
    sys.exit(0)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
snap_num = sys.argv[4]
rsize = float(sys.argv[5])

rc('font', size = 15)

ntot = 0
ntot, time, arr = read_paral(prefix, dir_name, base_name, snap_num, nproc)

mass = arr['mass'][:]

Z0 = 5.0E-4

lZ_Fe_sol = np.log10(Z0 / 0.02) - 0.8
lZ_O_sol = np.log10(Z0 / 0.02)

frac_O = 8.9 - 12.0 + lZ_O_sol
frac_O = 16.0 * np.power(10.0, frac_O)

frac_Fe = 7.55 - 12.0 + lZ_Fe_sol
frac_Fe = 56.0 * np.power(10.0, frac_Fe)

O = arr['mass_Z'][:, ID_O] + mass * 0.75 * frac_O
Fe = arr['mass_Z'][:, ID_Fe] + mass * 0.75 * frac_Fe

#O = arr['mass_Z'][:, ID_O]
#Fe = arr['mass_Z'][:, ID_Fe]

idw = np.where(arr['type'] == TYPE_WARM)
idc = np.where(arr['type'] == TYPE_COLD)
ids = np.where(arr['type'] == TYPE_STAR_PARAL)

O = np.log10(O / (mass * 0.75) / 16.0) + 12.0
Fe = np.log10(Fe / (mass * 0.75) / 56.0) + 12.0

OFe = O - Fe

#OFe -= (8.9 - 7.55)
#Fe -= 7.55

r = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1]
r = np.sqrt(r)

################################### figure #############################

fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(5)
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15, \
    hspace = 0.25)

############################# [Fe/H] ~ R ##########################
############################## cold ####################################
ax = plt.subplot(111)

plt.xlabel('Radius [kpc]')
plt.ylabel('12 + log[Fe/H]')

"""
ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.1))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
"""

ymin = 7.55 + np.log10(Z0 / 0.02) - 0.8
ymax = 7.55

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()
range = [[0.0, rsize], [ymin, ymax]]

plt.hist2d(r[idc], Fe[idc], bins = 100, cmap = cmap, norm = norm, range = range)
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))

plt.xlim(0.0, rsize)
plt.ylim(ymin, ymax)

figure_name = 'Obs-R-Fe-cold-%s-%s.png' % (dir_name, snap_num)

plt.savefig(figure_name)

############################## star ####################################
plt.clf()
ax = plt.subplot(111)

plt.xlabel('Radius [kpc]')
plt.ylabel('12 + log[Fe/H]')

"""
ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.1))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
"""

ymin = 7.55 + np.log10(Z0 / 0.02) - 0.8
ymax = 7.55

cmap = mpl.cm.jet
norm = mpl.colors.LogNorm()
range = [[0.0, rsize], [ymin, ymax]]

plt.hist2d(r[ids], Fe[ids], bins = 100, cmap = cmap, norm = norm, range = range)
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))

plt.xlim(0.0, rsize)
plt.ylim(ymin, ymax)

figure_name = 'Obs-R-Fe-star-%s-%s.png' % (dir_name, snap_num)

plt.savefig(figure_name)


