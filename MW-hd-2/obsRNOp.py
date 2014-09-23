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
    print 'obsRNOp.py: not enough parameter!'
    print '\tUsage: obsRNOp.py dir_name base_name nproc snap_num rsize'
    print '\tExample: obsRNOp.py MW-hd-2 MW 8 0006 10.0'
    sys.exit(0)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
snap_num = sys.argv[4]
rsize = float(sys.argv[5])

rc('font', size = 15)

ymin = -2.5
ymax = 1.0


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

############################# [N/O] ~ [O/H] ##########################

ax = plt.subplot(111)

plt.xlabel('Radius [kpc]')
plt.ylabel('log[N/O]')

#ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

ssize = 0.5

cmap = mpl.cm.jet
#cmap = mpl.cm.winter
norm = mpl.colors.LogNorm()

range = [[0.0, rsize], [-2.5, 0.0]]
plt.hist2d(rc, NOc, bins = 100, range = range, cmap = cmap, norm = norm)
cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
#cb.set_label('Count')


ms = 10.0
mew = 2.0

if True:

    fac = 1.0 / 3600.0 * Pi / 180.0

# NGC 2403:
    obs = np.loadtxt('NO_NGC2403.dat', dtype = float)
    dist = 3.25E3 # in kpc
    r0 = obs[:, 0] * fac * dist
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(r0, obs_NO, '^', color = brown, ms = ms, mew = mew, \
            fillstyle = 'none', label = 'NGC 2403')

# NGC 4395:
    obs = np.loadtxt('NO_NGC4395.dat', dtype = float)
    dist = 4.5E3 # in kpc
    r0 = obs[:, 0] * fac * dist
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(r0, obs_NO, 'mx', ms = ms, mew = mew, label = 'NGC 4395')

# NGC 1637:
    obs = np.loadtxt('NO_NGC1637.dat', dtype = float)
    dist = 8.6E3 # in kpc
    r0 = obs[:, 0] * fac * dist
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(r0, obs_NO, 'rD', ms = ms, mew = mew, fillstyle = 'none', \
            label = 'NGC 1637')

# NGC 3184:
    obs = np.loadtxt('NO_NGC3184.dat', dtype = float)
    dist = 8.7E3 # in kpc
    r0 = obs[:, 0] * fac * dist
    obs_NO = obs[:, 3]
    obs_OH = obs[:, 1]
    plt.plot(r0, obs_NO, 'kH', ms = ms, mew = mew, fillstyle = 'none', \
            label = 'NGC 3184')


plt.xlim(0.0, rsize)
plt.ylim(ymin, ymax)

lg = plt.legend(loc = 1, numpoints = 1, prop = {'size': 14})
#lg.get_frame().set_linewidth(0)

plt.errorbar(2.0, 0.2, yerr = 0.25, fmt = 'o', elinewidth = mew)

figure_name = 'Obs-R-NO-%s-%s.png' % (dir_name, snap_num)

plt.savefig(figure_name)

