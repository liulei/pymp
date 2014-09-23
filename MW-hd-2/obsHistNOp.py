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
    print 'obsHistNOp.py: not enough parameter!'
    print '\tUsage: obsHistNOp.py dir_name base_name nproc snap_num'
    print '\tExample: obsHistNOp.py MW-hd-2 MW 8 0006'
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

frac_N = 7.86 - 12.0 + np.log10(Z0 / 0.02)
frac_N = 14.0 * np.power(10.0, frac_N)

O = arr['mass_Z'][:, ID_O] + mass * 0.75 * frac_O
N = arr['mass_Z'][:, ID_N] + mass * 0.75 * frac_N

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

plt.xlabel('12+log[O/H]')
plt.ylabel('log[N/O]')

ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

ssize = 0.5

cmap = mpl.cm.jet
#cmap = mpl.cm.winter
norm = mpl.colors.LogNorm()


plt.hist2d(Oc, NOc, bins = 100, cmap = cmap, norm = norm)
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
#cb.set_label('Count')


ms = 10.0
mew = 2.0
# observation of dwarf galaxies (van Zee 1997):
if True:
    obs = np.loadtxt('vanZee1997a_NO_All.dat', dtype = float)
    obs_NO = obs[:, 0] - obs[:, 2]
#    print obs_NO
    obs_OH = obs[:, 2]
    plt.plot(obs_OH, obs_NO, 'k1', ms = ms, mew = mew, label = 'Dwarfs')

# NGC 2403:
if True:
    obs = np.loadtxt('NO_NGC2403.dat', dtype = float)
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(obs_OH, obs_NO, '^', color = brown, ms = ms, mew = mew, \
            fillstyle = 'none', label = 'NGC 2403')

# NGC 4395:
if True:
    obs = np.loadtxt('NO_NGC4395.dat', dtype = float)
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(obs_OH, obs_NO, 'mx', ms = ms, mew = mew, label = 'NGC 4395')

# NGC 1637:
if True:
    obs = np.loadtxt('NO_NGC1637.dat', dtype = float)
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(obs_OH, obs_NO, 'rD', ms = ms, mew = mew, fillstyle = 'none', \
            label = 'NGC 1637')

# NGC 3184:
if True:
    obs = np.loadtxt('NO_NGC3184.dat', dtype = float)
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(obs_OH, obs_NO, 'kH', ms = ms, mew = mew, fillstyle = 'none', \
            label = 'NGC 3184')

plt.xlim(8.9 + np.log10(5.0E-4 / 0.02), 9.5)
plt.ylim(-2.5, 1.0)

lg = plt.legend(loc = 1, numpoints = 1, prop = {'size': 14})
#lg.get_frame().set_linewidth(0)

plt.errorbar(9.2, -1.5, yerr = 0.25, xerr = 0.15, elinewidth = mew)

figure_name = 'Obs-Hist-NO-%s-%s.png' % (dir_name, snap_num)

plt.savefig(figure_name)

