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

def multi_cold_mass(dir_name, base_name, nproc, size, snap_num):

    title = dir_name

#    plt.figtext(0.5, 0.94, title, ha = 'center', size = 'large')

    majorLocator = ticker.MultipleLocator(20)
    minorLocator = ticker.MultipleLocator(4)

    nullFormatter = ticker.NullFormatter()

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()

    vmin = 1.0E4
    vmax = 2.0E7

    rc('font', size = 18)
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(9)
    fig.subplots_adjust(left = 0.10, right = 0.85, top = 0.95, bottom = 0.10, \
                        wspace = 0.0, hspace = 0.0)

############################### snap 0 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[0], nproc)

    ax = fig.add_subplot(221)

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

################################# snap 1 ####################################
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[1], nproc)

    ax = fig.add_subplot(222)

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

################################# snap 2 ####################################
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[2], nproc)

    ax = fig.add_subplot(223)

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

################################ snap 3 ####################################
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[3], nproc)

    ax = fig.add_subplot(224)

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

######################### color bar ##################################
# [xcoord, ycoord, width, height]
    cbaxes = fig.add_axes([0.87, 0.10, 0.03, 0.85])
    cb = plt.colorbar(orientation='vertical', \
        ticks = ticker.LogLocator(base = 10.0), cax = cbaxes)
    cb.set_label('Cold cloud mass [M$_\odot$]')

######################## label ######################################
    label = 't = 0.5 Gyr'
    plt.figtext(0.28, 0.9, label, ha = 'center', size = 20)

    label = 't = 1 Gyr'
    plt.figtext(0.68, 0.9, label, ha = 'center', size = 20)

    label = 't = 2 Gyr'
    plt.figtext(0.28, 0.47, label, ha = 'center', size = 20)

    label = 't = 3 Gyr'
    plt.figtext(0.68, 0.47, label, ha = 'center', size = 20)


########################## save ######################################

    figure_name = 'McPanel-xz-' + dir_name + '.png'
    plt.savefig(figure_name)

######################################################################
############################## X - Y #################################
######################################################################

    rc('font', size = 18)
    plt.clf()
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(9)
    fig.subplots_adjust(left = 0.10, right = 0.85, top = 0.95, bottom = 0.10, \
        wspace = 0.0, hspace = 0.0)

############################### snap 0 ####################################
    
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[0], nproc)

    ax = fig.add_subplot(221)

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

################################# snap 1 ####################################
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[1], nproc)

    ax = fig.add_subplot(222)

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

################################# snap 2 ####################################
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[2], nproc)

    ax = fig.add_subplot(223)

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

################################ snap 3 ####################################
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, snap_num[3], nproc)

    ax = fig.add_subplot(224)

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

######################### color bar ##################################
# [xcoord, ycoord, width, height]
    cbaxes = fig.add_axes([0.87, 0.10, 0.03, 0.85])
    cb = plt.colorbar(orientation='vertical', \
        ticks = ticker.LogLocator(base = 10.0), cax = cbaxes)
    cb.set_label('Cold cloud mass [M$_\odot$]')

######################## label ######################################
    label = 't = 0.5 Gyr'
    plt.figtext(0.28, 0.9, label, ha = 'center', size = 20)

    label = 't = 1 Gyr'
    plt.figtext(0.68, 0.9, label, ha = 'center', size = 20)

    label = 't = 2 Gyr'
    plt.figtext(0.28, 0.47, label, ha = 'center', size = 20)

    label = 't = 3 Gyr'
    plt.figtext(0.68, 0.47, label, ha = 'center', size = 20)

########################## save ######################################

    figure_name = 'McPanel-xy-' + dir_name + '.png'
    plt.savefig(figure_name)

########################### main function ############################

if len(sys.argv) < 5:
    print 'fourPanelMc.py: not enough parameter!'
    print '\tUsage: ./fourPanelMc.py dir_name base_name nproc box_size'
    print '\tExample: ./DPanel.py MW-8 MW 8 50.0'
    sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
size = float(sys.argv[4])

snap_num = ['0050', '0100', '0200', '0300']

multi_cold_mass(dir_name, base_name, nproc, size, snap_num)
