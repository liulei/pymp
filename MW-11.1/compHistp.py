#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 4:
	print 'compHistp: not enough parameter!'
	print '\tUsage: compHistp.py dir_name base_name nproc'
	print '\tExample: compHistp.py MW-11.1 MW 8'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])

rc('font', size = 14)
fig = plt.figure()
#fig.set_figwidth(6)
#fig.set_figheight(6)
fig.subplots_adjust(left = 0.17, right = 0.95, top = 0.97, bottom = 0.12, \
        hspace = 0.0)

nullFormatter = ticker.NullFormatter()

ml = 1.0E3
mh = 1.0E7

nbin = 30
    
ax = fig.add_subplot(111)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

############################## t = 0.5 Gyr ###############################
snap_num = '0050'
ntot, time, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xm, count = mp.calc_hist(arr, ml, mh, nbin)
plt.plot(xm, count, 'r-', label = 't = 0.5 Gyr', drawstyle = 'steps-mid')

############################## t = 1.0 Gyr ###############################
snap_num = '0100'
ntot, time, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xm, count = mp.calc_hist(arr, ml, mh, nbin)
plt.plot(xm, count, 'g-', label = 't = 1.0 Gyr', drawstyle = 'steps-mid')

############################## t = 3.0 Gyr ###############################
snap_num = '0300'
ntot, time, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
xm, count = mp.calc_hist(arr, ml, mh, nbin)
plt.plot(xm, count, 'b-', label = 't = 3.0 Gyr', drawstyle = 'steps-mid')

plt.xlim(ml, mh)
plt.ylim(5E-5, 2E2)

lg = plt.legend(loc = 0, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'comp-hist-' + dir_name + '.png'
plt.savefig(figure_name)
