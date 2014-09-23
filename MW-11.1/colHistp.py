#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 4:
	print 'colHistp: not enough parameter!'
	print '\tUsage: colHistp.py dir_name base_name nproc'
	print '\tExample: colHistp.py MW-8 MW 8'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])

rc('font', size = 14)
fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(6)
fig.subplots_adjust(left = 0.17, right = 0.95, top = 0.97, bottom = 0.12, \
        hspace = 0.0)

nullFormatter = ticker.NullFormatter()

ml = 1.0E3
mh = 1.0E7

nbin = 30
    
############################## t = 0.5 Gyr ###############################
snap_num = '0050'
ntot, time, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

xm, count = mp.calc_hist(arr, ml, mh, nbin)

ax = fig.add_subplot(311)

plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
#plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

plt.xscale('log')
plt.yscale('log')

plt.plot(xm, count, drawstyle = 'steps-mid')

plt.xlim(ml, mh)
plt.ylim(5E-5, 5E0)

ax.xaxis.set_major_formatter(nullFormatter)

############################## t = 1.0 Gyr ###############################
snap_num = '0100'
ntot, time, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

xm, count = mp.calc_hist(arr, ml, mh, nbin)

ax = fig.add_subplot(312)

plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

plt.xscale('log')
plt.yscale('log')

plt.plot(xm, count, drawstyle = 'steps-mid')

plt.xlim(ml, mh)
plt.ylim(5E-5, 2.0E1)

ax.xaxis.set_major_formatter(nullFormatter)

############################## t = 3.0 Gyr ###############################
snap_num = '0300'
ntot, time, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

xm, count = mp.calc_hist(arr, ml, mh, nbin)

ax = fig.add_subplot(313)

plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
#plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

plt.xscale('log')
plt.yscale('log')

plt.plot(xm, count, drawstyle = 'steps-mid')

plt.xlim(ml, mh)
plt.ylim(5.0E-5, 2E2)

#ax.xaxis.set_major_formatter(nullFormatter)

############################# label ######################################
label = 't = 0.5 Gyr'
plt.figtext(0.8, 0.92, label, ha = 'center', size = 14)

label = 't = 1.0 Gyr'
plt.figtext(0.8, 0.64, label, ha = 'center', size = 14)

label = 't = 3.0 Gyr'
plt.figtext(0.8, 0.36, label, ha = 'center', size = 14)

figure_name = 'hist-' + dir_name + '.png'
plt.savefig(figure_name)
