#!/home/liulei/local/bin/python

from numpy import *
import numpy as np
import mp
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys

if len(sys.argv) < 6:
	print 'langrangep: not enough parameter!'
	print '\tUsage: langrangep.py dir_name base_name nproc start end'
	print '\tExample: langrangep.py hd-1 1E3 1 0 200'
	sys.exit(0)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
start = int(sys.argv[4])
end = int(sys.argv[5])

r01 = np.zeros(end - start + 1, dtype = float)
r03 = np.zeros(end - start + 1, dtype = float)
r05 = np.zeros(end - start + 1, dtype = float)
r07 = np.zeros(end - start + 1, dtype = float)
r09 = np.zeros(end - start + 1, dtype = float)

for isnap in range(start, end + 1):

    snap_num = '%04d' % isnap

    print '###################### snap ', snap_num, ' ###############'

    ntot = 0
    ntot, arr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num, nproc)
    
    idm = np.where(arr['type'] == mp.TYPE_DM_PARAL)
    
    r2 = arr['pos'][:, 0] * arr['pos'][:, 0] + arr['pos'][:, 1] * arr['pos'][:, 1] \
        + arr['pos'][:, 2] * arr['pos'][:, 2]
    r = np.sqrt(r2)
    
    mdm = arr[idm]['mass']
    ntot = len(mdm)
    mdm_tot = mdm.sum()
    mdm /= mdm_tot
    rdm = r[idm]

    idx_sort = np.argsort(rdm)
    rsort = rdm[idx_sort]
    msort = mdm[idx_sort]
    
    for i in range(1, ntot):

        msort[i] += msort[i - 1]

        if(msort[i - 1] < 0.1 and msort[i] >= 0.1):
            r01[isnap] = rsort[i]

        if(msort[i - 1] < 0.3 and msort[i] >= 0.3):
            r03[isnap] = rsort[i]

        if(msort[i - 1] < 0.5 and msort[i] >= 0.5):
            r05[isnap] = rsort[i]

        if(msort[i - 1] < 0.7 and msort[i] >= 0.7):
            r07[isnap] = rsort[i]

        if(msort[i - 1] < 0.9 and msort[i] >= 0.9):
            r09[isnap] = rsort[i]

time = np.arange(start, end + 1, dtype = float) * 10.0

rc('font', size = 17)

plt.xlabel('Time [Myr]')
plt.ylabel('Cumulative fraction')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.93, bottom = 0.12)

plt.plot(time, r01, 'b-')
plt.plot(time, r03, 'g-')
plt.plot(time, r05, 'r-')
plt.plot(time, r07, 'c-')
plt.plot(time, r09, 'm-')

lg = plt.legend(('0.1', '0.3', '0.5', '0.7', '0.9'), ncol = 5, \
        prop = {'size': 13})
lg.get_frame().set_linewidth(0)

plt.xlim(time[start], time[end])
plt.ylim(0.0, 20.0)

figure_name = 'Langrange-' + dir_name + '.eps'
plt.savefig(figure_name)
