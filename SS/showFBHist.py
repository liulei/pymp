#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
from matplotlib import ticker
import matplotlib.pyplot as plt
import sys
import os
import mp

struct_record = np.dtype([('ss_type', int), \
                        ('t_dead', float), \
                        ('m0', float), \
                        ('m2', float), \
                        ('Z', float), \
                        ('x', float), \
                        ('y', float), \
                        ('z', float)])

def read_FB(prefix, dir_name, nproc):

    tmp = 'tmp_38fdaf'
    for i in range(0, nproc):

        file_name = prefix + '/' + dir_name + '/out/record_fb_' + str(i) + '.dat'
        print file_name
        cmd = 'cat ' + file_name + ' >> ' + tmp
        os.system(cmd)
    
    arr = np.loadtxt(tmp, dtype = struct_record)

    cmd = 'rm ' + tmp
    os.system(cmd)

    return arr

def calc_hist_FB(t, nbin, tmax):

    xt = np.arange(nbin, dtype = float)
    xt = (xt + 0.5) * tmax / nbin

    dt = tmax / nbin

    count = np.zeros(nbin, dtype = float)
    for i in range(0, len(t)):

        id = int(t[i] / dt)
        if (id >= 0 and id < nbin):

            count[id] += 1.0

    count /= dt
    return xt, count

if len(sys.argv) < 4:
	print 'showFBHist.py: not enough parameter!'
	print '\tUsage: showFBHist.py dir_name nproc tmax'
	print '\tExample: showFBHist.py SS-5E7-iso-4 16 3000.0'
	sys.exit(1)

dir_name = sys.argv[1]
nproc = int(sys.argv[2])
tmax = float(sys.argv[3])

rc('font', size = 15)
ax = plt.subplot(111)
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.12)
plt.xlabel('Time [Myr]')
plt.ylabel('Events / Myr')

majorLocator = ticker.MultipleLocator(0.5)

formatter = ticker.ScalarFormatter(useMathText = True)
formatter.set_powerlimits((-2,2))

#ax.yaxis.set_major_formatter(formatter)
#ax.xaxis.set_major_locator(majorLocator)

rarr = read_FB(mp.prefix, dir_name, nproc)

idsn2 = np.where(rarr['ss_type'] == mp.SS_TYPE_SNII)
idsn1 = np.where(rarr['ss_type'] == mp.SS_TYPE_SNIa)
idpn = np.where(rarr['ss_type'] == mp.SS_TYPE_PN)

t = rarr['t_dead'][:]
tsn2 = t[idsn2]
tsn1 = t[idsn1]
tpn = t[idpn]

nbin = 30

plt.yscale('log')

xt, count = calc_hist_FB(tsn2, nbin, tmax)
plt.plot(xt, count, 'b-', label = 'SNII', drawstyle = 'steps-mid')

xt, count = calc_hist_FB(tsn1, nbin, tmax)
plt.plot(xt, count, 'r-', label = 'SNIa', drawstyle = 'steps-mid')

xt, count = calc_hist_FB(tpn, nbin, tmax)
plt.plot(xt, count, 'g-', label = 'PN', drawstyle = 'steps-mid')

plt.xlim(0, tmax)

lg = plt.legend(loc = 0, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'comp-FB-hist-' + dir_name + '.png'
plt.savefig(figure_name)

######################### end of main function ###########################


