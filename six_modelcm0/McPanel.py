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

def multi_Mc(snap_num, size):

    dir = ['81-hd-3Hs1', '91-hd-3Hs1', '101-hd-3Hs1', '80-hd-3Hs1', '90-hd-3Hs1', '100-hd-3Hs1']
    proc_num = [2, 8, 8, 2, 8, 8]

    vmin = 1.0E3
    vmax = 1.0E7

    snap_name = '%04d' % snap_num
    title = 't = %d Myr' % (10 * snap_num)

    base_name = 'dwarf'

    rc('font', size = 15)
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(6.5)
    fig.subplots_adjust(left = 0.10, right = 0.88, top = 0.92, bottom = 0.10, \
                        wspace = 0.0, hspace = 0.0)

#    plt.figtext(0.5, 0.94, title, ha = 'center', size = 'large')

    majorLocator = ticker.MultipleLocator(5)
    minorLocator = ticker.MultipleLocator(2.5)

    nullFormatter = ticker.NullFormatter()

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()

################### hdc-81 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[0], base_name, snap_name, proc_num[0])

    ax = fig.add_subplot(231)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#   plt.xlabel('X [kpc]')
    plt.ylabel('Z [kpc]')
    plt.scatter(x[idc], z[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

    ax.xaxis.set_major_formatter(nullFormatter)
#    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-91 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[1], base_name, snap_name, proc_num[1])

    ax = fig.add_subplot(232)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#   plt.xlabel('X [kpc]')
#   plt.ylabel('Z [kpc]')
    plt.scatter(x[idc], z[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-101 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[2], base_name, snap_name, proc_num[2])

    ax = fig.add_subplot(233)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
#    boolarr = np.logical_and(den > 5.0E-5, boolarr)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#   plt.xlabel('X [kpc]')
#   plt.ylabel('Z [kpc]')
    plt.scatter(x[idc], z[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-80 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[3], base_name, snap_name, proc_num[3])

    ax = fig.add_subplot(234)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.xlabel('X [kpc]')
    plt.ylabel('Z [kpc]')
    plt.scatter(x[idc], z[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

#    ax.xaxis.set_major_formatter(nullFormatter)
#    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-90 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[4], base_name, snap_name, proc_num[1])

    ax = fig.add_subplot(235)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.xlabel('X [kpc]')
#   plt.ylabel('Z [kpc]')
    plt.scatter(x[idc], z[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

#    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-100 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[5], base_name, snap_name, proc_num[2])

    ax = fig.add_subplot(236)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
#    boolarr = np.logical_and(den > 5.0E-5, boolarr)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.xlabel('X [kpc]')
#   plt.ylabel('Z [kpc]')
    plt.scatter(x[idc], z[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

#    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

######################### color bar ##################################
# [xcoord, ycoord, width, height]
    cbaxes = fig.add_axes([0.89, 0.10, 0.02, 0.82])
    cb = plt.colorbar(orientation='vertical', \
        ticks = ticker.LogLocator(base = 10.0), cax = cbaxes)
    cb.set_label('Cloud mass [M$_\odot$]')

######################## label ######################################
    label = '$2\\times10^8 \mathsf{M}_\odot$'
    plt.figtext(0.23, 0.87, label, ha = 'center', size = 'large')

    label = '$2\\times10^9 \mathsf{M}_\odot$'
    plt.figtext(0.49, 0.87, label, ha = 'center', size = 'large')

    label = '$2\\times10^{10} \mathsf{M}_\odot$'
    plt.figtext(0.75, 0.87, label, ha = 'center', size = 'large')


########################## save ######################################

    figure_name = 'McPanel-xz-' + snap_name + '.png'
    plt.savefig(figure_name)

######################### X - Y ######################################

    print "\n############## X - Y ###############\n"
    rc('font', size = 15)
    plt.clf()
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(6.5)
    fig.subplots_adjust(left = 0.10, right = 0.88, top = 0.92, bottom = 0.10, \
                        wspace = 0.0, hspace = 0.0)

#    plt.figtext(0.5, 0.94, title, ha = 'center', size = 'large')

################### hdc-81 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[0], base_name, snap_name, proc_num[0])

    ax = fig.add_subplot(231)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#   plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.scatter(x[idc], y[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

    ax.xaxis.set_major_formatter(nullFormatter)
#    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-91 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[1], base_name, snap_name, proc_num[1])

    ax = fig.add_subplot(232)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#   plt.xlabel('X [kpc]')
#   plt.ylabel('Y [kpc]')
    plt.scatter(x[idc], y[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-101 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[2], base_name, snap_name, proc_num[2])

    ax = fig.add_subplot(233)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
#    boolarr = np.logical_and(den > 5.0E-5, boolarr)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#   plt.xlabel('X [kpc]')
#   plt.ylabel('Y [kpc]')
    plt.scatter(x[idc], y[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-80 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[3], base_name, snap_name, proc_num[3])

    ax = fig.add_subplot(234)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.scatter(x[idc], y[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

#    ax.xaxis.set_major_formatter(nullFormatter)
#    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-90 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[4], base_name, snap_name, proc_num[1])

    ax = fig.add_subplot(235)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.xlabel('X [kpc]')
#   plt.ylabel('Y [kpc]')
    plt.scatter(x[idc], y[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

#    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

################### hdc-100 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir[5], base_name, snap_name, proc_num[2])

    ax = fig.add_subplot(236)

    arr = np.sort(rarr, order = 'mass')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    type = arr['type'][:]
    r = np.sqrt(x * x + y * y + z * z)

    mass = arr['mass'][:]

    boolarr = np.logical_and(type == mp.TYPE_WARM, r < 50.0)
#    boolarr = np.logical_and(den > 5.0E-5, boolarr)
    idw = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_COLD, r < 50.0)
    idc = np.where(boolarr)
    boolarr = np.logical_and(type == mp.TYPE_STAR_PARAL, r < 50.0)
    ids = np.where(boolarr)

    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.xlabel('X [kpc]')
#   plt.ylabel('Y [kpc]')
    plt.scatter(x[idc], y[idc], s = 1, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)

#    ax.xaxis.set_major_formatter(nullFormatter)
    ax.yaxis.set_major_formatter(nullFormatter)

    plt.xlim(-size, size * 0.99)
    plt.ylim(-size, size)

######################### color bar ##################################
# [xcoord, ycoord, width, height]
    cbaxes = fig.add_axes([0.89, 0.10, 0.02, 0.82])
    cb = plt.colorbar(orientation='vertical', \
        ticks = ticker.LogLocator(base = 10.0), cax = cbaxes)
    cb.set_label('Cloud mass [M$_\odot$]')

######################## label ######################################
    label = '$2\\times10^8 \mathsf{M}_\odot$'
    plt.figtext(0.23, 0.87, label, ha = 'center', size = 'large')

    label = '$2\\times10^9 \mathsf{M}_\odot$'
    plt.figtext(0.49, 0.87, label, ha = 'center', size = 'large')

    label = '$2\\times10^{10} \mathsf{M}_\odot$'
    plt.figtext(0.75, 0.87, label, ha = 'center', size = 'large')


########################## save ######################################

    figure_name = 'McPanel-xy-' + snap_name + '.png'
    plt.savefig(figure_name)


########################### main function ############################

if len(sys.argv) < 3:
    print 'McPanel.py: not enough parameter!'
    print '\tNote: this script only work for "six panel" run!'
    print '\tUsage: ./McPanel.py snap_num box_size'
    print '\tExample: ./McPanel.py 1 50.0'
    sys.exit(1)

snap_num = int(sys.argv[1])
size = float(sys.argv[2])

multi_Mc(snap_num, size)
