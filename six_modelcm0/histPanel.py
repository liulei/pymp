#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
import mp
import mp_snap
from matplotlib import *
from matplotlib import colors, ticker, colorbar, mpl
import matplotlib.pyplot as plt
from math import *
import sys

def multi_hist(snap_num):

    dir = ['81-hd-3Hs1', '80-hd-3Hs1', '91-hd-3Hs1', '90-hd-3Hs1', \
          '101-hd-3Hs1', '100-hd-3Hs1']

    proc_num = [2, 8, 8]

    ml = 1.0E3
    mh = 1.0E7

    logml = log10(ml)
    logmh = log10(mh)

    snap_name = '%04d' % snap_num
    title = 't = %d Myr' % (10 * snap_num)

    base_name = 'dwarf'

    rc('font', size = 15)
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    fig.subplots_adjust(left = 0.12, right = 0.95, top = 0.95, bottom = 0.08, \
                        wspace = 0.0, hspace = 0.0)

    plt.figtext(0.53, 0.96, title, ha = 'center', size = 'large')

#    majorLocator = ticker.MultipleLocator(5)
#    minorLocator = ticker.MultipleLocator(2.5)

    nullFormatter = ticker.NullFormatter()

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()

    nbin = 15

    ymin = 1.1E-7
    ymax = 1.0E1
################################# 81 #################################
    ntot, time, arr = mp.read_snap_paral(mp.prefix, dir[0], base_name, snap_name, proc_num[0])
    xm, count = mp.calc_hist(arr, ml, mh, nbin)

    ax = fig.add_subplot(321)

    plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
    plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(xm, count, drawstyle = 'steps-mid')

    plt.xlim(ml, mh)
    plt.ylim(ymin, ymax)

    ax.xaxis.set_major_formatter(nullFormatter)
#    ax.yaxis.set_major_formatter(nullFormatter)

################################# 80 #################################
    ntot, time, arr = mp.read_snap_paral(mp.prefix, dir[1], base_name, snap_name, proc_num[0])
    xm, count = mp.calc_hist(arr, ml, mh, nbin)

    ax = fig.add_subplot(322)

    plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
#    plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(xm, count, drawstyle = 'steps-mid')

    plt.xlim(ml * 1.01, mh)
    plt.ylim(ymin, ymax)

    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    ymin = 2.0E-7
    ymax = 9.0E1
################################# 91 #################################
    ntot, time, arr = mp.read_snap_paral(mp.prefix, dir[2], base_name, snap_name, proc_num[1])
    xm, count = mp.calc_hist(arr, ml, mh, nbin)

    ax = fig.add_subplot(323)

    plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
    plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(xm, count, drawstyle = 'steps-mid')

    plt.xlim(ml, mh)
    plt.ylim(ymin, ymax)

    ax.xaxis.set_major_formatter(nullFormatter)
#    ax.yaxis.set_major_formatter(nullFormatter)

################################# 90 #################################
    ntot, time, arr = mp.read_snap_paral(mp.prefix, dir[3], base_name, snap_name, proc_num[1])
    xm, count = mp.calc_hist(arr, ml, mh, nbin)

    ax = fig.add_subplot(324)

    plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
#    plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(xm, count, drawstyle = 'steps-mid')

    plt.xlim(ml * 1.01, mh)
    plt.ylim(ymin, ymax)

    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    ymin = 5.0E-6
    ymax = 9.0E1
################################# 101 #################################
    ntot, time, arr = mp.read_snap_paral(mp.prefix, dir[4], base_name, snap_name, 8)
    xm, count = mp.calc_hist(arr, ml, mh, nbin)

    ax = fig.add_subplot(325)

    plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
    plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(xm, count, drawstyle = 'steps-mid')

    plt.xlim(ml, mh)
    plt.ylim(ymin, ymax)

#    ax.xaxis.set_major_formatter(nullFormatter)
#    ax.yaxis.set_major_formatter(nullFormatter)

################################# 100 #################################
    ntot, time, arr = mp.read_snap_paral(mp.prefix, dir[5], base_name, snap_name, 8)
    xm, count = mp.calc_hist(arr, ml, mh, nbin)

    ax = fig.add_subplot(326)

    plt.xlabel('M$_\mathsf{COLD}$ [M$_\odot$]')
#    plt.ylabel('dN / d(log M$_\mathsf{COLD}$) / M$_\mathsf{COLD}$')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(xm, count, drawstyle = 'steps-mid')

    plt.xlim(ml * 1.01, mh)
    plt.ylim(ymin, ymax)

#    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    figure_name = 'histPanel-' + snap_name + '.png'
    plt.savefig(figure_name)

    figure_name = 'histPanel-' + snap_name + '.eps'
    plt.savefig(figure_name)

########################### main function ############################

if len(sys.argv) < 2:
    print 'histPanel.py: not enough parameter!'
    print '\tNote: this script only work for "six panel" run!'
    print '\tUsage: ./histPanel.py snap_num'
    print '\tExample: ./histPanel.py 1'
    sys.exit(1)

snap_num = int(sys.argv[1])

multi_hist(snap_num)
