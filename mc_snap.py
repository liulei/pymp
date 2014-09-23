#!/usr/bin/python

from numpy import *
import numpy as np
import mc
from matplotlib import *
from matplotlib import colors, ticker, colorbar, mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *
import sys

struct_mp_mc = np.dtype([('index', int), \
                ('mass', float), \
                ('pos', float, 3), \
                ('vel', float, 3), \
                ('den', float), \
                ('T', float), \
                ('mass_Z', float), \
                ('m0', float), \
                ('t_beg_sf', float), \
                ('type', int), \
                ('ss_type', int), \
                ('t_dead', float)])

def is_mc_exist(prefix, dir_name, base_name, snap_num, nproc):

    file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
    file_name = file_name + 'MP' + str(nproc) + '-0'
    return os.path.isfile(file_name)

def read_mc(prefix, dir_name, base_name, snap_num, nproc):

# read file header, get total number, time, bounding box, if necessary
    
    file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
#   if nproc > 1:
    file_name = file_name + 'MP' + str(nproc) + '-0'

    f = open(file_name, 'r')

    strlist = f.readline().split()
    step = int(strlist[0])
    time = float(strlist[1])

    strlist = f.readline().split()
    ntot = int(strlist[0])
    n = int(strlist[1])

    f.close()

# allocate space for array

    arr = np.zeros(ntot, dtype = struct_mp_mc)

# for every single file, read header again to get particle number in this 
# file, then use genfromtxt() load data to a temperatory array, assign 
# data from this array to global array
#   np.genfromtxt(fname, dtype = mp_paral, skip_header = head number)
    nread = 0
    for ifile in range(0, nproc):
#    for ifile in range(0, 1):
        
        file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
#       if nproc > 1:
        file_name = file_name + 'MP' + str(nproc) + '-' + str(ifile)

        print file_name
        
        f = open(file_name, 'r')
        strlist = f.readline().split()
        strlist = f.readline().split()
        n = int(strlist[1])
        f.close()

        atemp = np.loadtxt(file_name, dtype = struct_mp_mc, skiprows = 4)
#        atemp = np.loadtxt(file_name, dtype = float, skiprows = 4)
        
        if n != len(atemp):
            print 'wrong file parameter!'
            sys.exit(1);
        
        arr[nread: nread + n] = atemp[0:n]
        nread += n

    return ntot, time, arr

################### gen_snap_den ####################################

def gen_snap_den(rarr, dir_name, base_name, snap_num, size, title_name = ''):

    arr = np.sort(rarr, order = 'den')

    dmin = 1.0E6
    dmax = 1.0E9

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    den = arr['den'][:]

    r = np.sqrt(x * x + y * y + z * z)
    id1 = (arr['type'] == mp.TYPE_WARM)
#    id2 = (r < 150.0)
        
#    id3 = np.logical_and(id1, id2)

#    idw = np.where(id3)
#   print idw

    idw = np.where(arr['type'] == mp.TYPE_WARM)
    idc = np.where(arr['type'] == mp.TYPE_COLD)
    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.title(title_name)
    #plt.figure(figsize = (sz, sz))
    plt.xlabel('X [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idw] * 1E3, z[idw] * 1E3, s = 1, c = den[idw], marker = 'o', \
        cmap = cmap, norm = norm, vmin = dmin, vmax = dmax, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Density [cm$^{-3}$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Dsort-xz-' + dir_name + '-' + base_name + '-' \
        + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Dsort-xz-' + dir_name + '-' + base_name + '-' \
        + snap_num + '.png'
    plt.savefig(figure_name)

######################## X-Y #################################################
    print 'X - Y'
    
    plt.clf()
    #plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [pc]')
    plt.ylabel('Y [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    
    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idw] * 1E3, y[idw] * 1E3, s = 1, c = den[idw], marker = 'o', \
        cmap = cmap, norm = norm, vmin = dmin, vmax = dmax, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Density [cm$^{-3}$]')
    
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    
    figure_name = 'Dsort-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#    plt.savefig(figure_name)
    
    figure_name = 'Dsort-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

######################## Y-Z #################################################
    print 'Y - Z'
    
    plt.clf()
    #plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('Y [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    
    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(y[idw] * 1E3, z[idw] * 1E3, s = 1, c = den[idw], marker = 'o', \
        cmap = cmap, norm = norm, vmin = dmin, vmax = dmax, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Density [cm$^{-3}$]')
    
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    
    figure_name = 'Dsort-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#    plt.savefig(figure_name)
    
    figure_name = 'Dsort-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

############################# 3-D #########################################
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    ax.set_xlabel('X [pc]')
    ax.set_ylabel('Y [pc]')
    ax.set_zlabel('Z [pc]')
#    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    plt.subplots_adjust(left = 0.03, right = 0.97, top = 0.97, bottom = 0.03)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    sc = ax.scatter(x[idw] * 1E3, y[idw] * 1E3, z[idw] * 1E3, s = 0.5, \
        c = den[idw], marker = 'o', cmap = cmap, norm = norm, 
        vmin = dmin, vmax = dmax, edgecolors = 'none')
    cb = plt.colorbar(sc, ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Density [cm$^{-3}$]')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 25))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 25))
    ax.zaxis.set_major_locator(ticker.MultipleLocator(base = 25))

    ax.set_xlim3d(-size, size)
    ax.set_ylim3d(-size, size)
    ax.set_zlim3d(-size, size)

    figure_name = 'Dsort-3D-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)


######################## gen_snap_T ####################################

def gen_snap_T(rarr, dir_name, base_name, snap_num, size, title_name = ''):
    
    arr = np.sort(rarr, order = 'T')
#   arr = arr[::-1]

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    T = arr['T'][:]

    idw = np.where(arr['type'] == mp.TYPE_WARM)
    idc = np.where(arr['type'] == mp.TYPE_COLD)
    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.title(title_name)
    #plt.figure(figsize = (sz, sz))
    plt.xlabel('X [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idw], z[idw], s = 1, c = T[idw], marker = 'o', cmap = cmap, \
        norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Temperature [K]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Tsort-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Tsort-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

######################## X-Y #################################################

    plt.clf()

    plt.title(title_name)
    #plt.figure(figsize = (sz, sz))
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idw], y[idw], s = 1, c = T[idw], marker = 'o', cmap = cmap, \
    norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Temperature [K]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Tsort-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Tsort-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

######################## Y-Z #################################################

    plt.clf()

    plt.title(title_name)
    #plt.figure(figsize = (sz, sz))
    plt.xlabel('Y [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(y[idw], z[idw], s = 1, c = T[idw], marker = 'o', cmap = cmap, \
    norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Temperature [K]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Tsort-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Tsort-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)


################### gen_snap_cold_mass ####################################

def gen_snap_cold_mass(rarr, dir_name, base_name, snap_num, size, \
    title_name = ''):

    vmin = 1.0E1
    vmax = 1.0E5

    arr = np.sort(rarr, order = 'mass')
#   arr = rarr

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    mass = arr['mass'][:]

    idw = np.where(arr['type'] == mp.TYPE_WARM)
    idc = np.where(arr['type'] == mp.TYPE_COLD)
    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

    if np.size(idc) == 0:
        return
    
    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.title(title_name)

    #plt.figure(figsize = (sz, sz))
    plt.xlabel('X [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idc] * 1E3, z[idc] * 1E3, s = 2, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Cold Cloud Mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Mc-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Mc-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)


######################## X-Y #################################################

    plt.clf()
    plt.title(title_name)
    #plt.figure(figsize = (sz, sz))
    plt.xlabel('X [pc]')
    plt.ylabel('Y [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idc] * 1E3, y[idc] * 1E3, s = 2, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Cold Cloud Mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Mc-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Mc-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

######################## Y-Z #################################################

    plt.clf()
    plt.title(title_name)
    #plt.figure(figsize = (sz, sz))
    plt.xlabel('Y [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(y[idc] * 1E3, z[idc] * 1E3, s = 2, c = mass[idc], marker = 'o', \
        cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Cold Cloud Mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Mc-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Mc-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

################### gen_snap_sn ####################################

def gen_snap_sn(rarr, time, dir_name, base_name, snap_num, size, \
    title_name = ''):

    print 'time: ', time

    vmin = 0.8
    vmax = 100

    arr = np.sort(rarr, order = 'mass')
#   arr = rarr

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    mass = arr['m0'][:]

    idw = np.where(arr['type'] == mp.TYPE_WARM)
    idc = np.where(arr['type'] == mp.TYPE_COLD)
#    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)
#    idm = np.where(arr['type'] == mp.TYPE_DM_PARAL)
    id1 = (arr['type'] == mp.TYPE_STAR_PARAL)
# only pickup those still alive:
    id2 = (arr['t_dead'] < time)
    id3 = (arr['t_dead'] > time - 0.1)
# two SN types:
    id4 = (arr['ss_type'] >= 2)
    ids = np.logical_and(id1, id2)
    ids = np.logical_and(ids, id3)
    ids = np.logical_and(ids, id4)
    ids = np.where(ids)

    size_sn = 14

    if np.size(ids) == 0:
       return
    
    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    print ids

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[ids] * 1E3, z[ids] * 1E3, s = size_sn, c = mass[ids], \
        marker = 'o', cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, \
        edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Stellar mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'SN-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

######################## X-Y #################################################

    plt.clf()
#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [pc]')
    plt.ylabel('Y [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[ids] * 1E3, y[ids] * 1E3, s = size_sn, c = mass[ids], \
        marker = 'o', cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, \
        edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Stellar mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'SN-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

########################### Y - Z ###################################
    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('Y [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(y[ids] * 1E3, z[ids] * 1E3, s = size_sn, c = mass[ids], \
        marker = 'o', cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, \
        edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Stellar mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'SN-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)



################### gen_snap_star ####################################

def gen_snap_star(rarr, dir_name, base_name, snap_num, size, \
    title_name = ''):

    vmin = 0.8
    vmax = 100

    arr = np.sort(rarr, order = 'mass')
#   arr = rarr

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    mass = arr['mass'][:]

    idw = np.where(arr['type'] == mp.TYPE_WARM)
    idc = np.where(arr['type'] == mp.TYPE_COLD)
    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)
#    idm = np.where(arr['type'] == mp.TYPE_DM_PARAL)

    if np.size(ids) == 0:
        print ids
        return
    
    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[ids] * 1E3, z[ids] * 1E3, s = 2, c = mass[ids], \
        marker = 'o', cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, \
        edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Stellar mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'STAR-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

######################## X-Y #################################################

    plt.clf()
#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [pc]')
    plt.ylabel('Y [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[ids] * 1E3, y[ids] * 1E3, s = 2, c = mass[ids], \
        marker = 'o', cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, \
        edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Stellar mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'STAR-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

########################### Y - Z ###################################
    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('Y [pc]')
    plt.ylabel('Z [pc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(y[ids] * 1E3, z[ids] * 1E3, s = 2, c = mass[ids], \
        marker = 'o', cmap = cmap, norm = norm, vmin = vmin, vmax = vmax, \
        edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Stellar mass [M$_\odot$]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'STAR-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

############################# 3-D #########################################
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

#    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    ax.set_xlabel('X [pc]')
    ax.set_ylabel('Y [pc]')
    ax.set_zlabel('Z [pc]')
#    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    plt.subplots_adjust(left = 0.03, right = 0.97, top = 0.97, bottom = 0.03)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    sc = ax.scatter(x[ids] * 1E3, y[ids] * 1E3, z[ids] * 1E3, s = 0.5, \
        c = mass[ids], marker = 'o', cmap = cmap, norm = norm, 
        vmin = vmin, vmax = vmax, edgecolors = 'none')
    cb = plt.colorbar(sc, ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Stellar mass [M$_\odot$]')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 25))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 25))
    ax.zaxis.set_major_locator(ticker.MultipleLocator(base = 25))

    ax.set_xlim3d(-size, size)
    ax.set_ylim3d(-size, size)
    ax.set_zlim3d(-size, size)

    figure_name = 'STAR-3D-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

################### gen_snap_Fe ####################################

def gen_snap_Fe(rarr, dir_name, base_name, snap_num, size, title_name = ''):

    frac_Fe = 0.75 * np.power(10.0, 7.55 - 12.0) * 56.0 * (1.0E-5 / 0.02)

    rarr['mass_Fe'] += rarr['mass'] * frac_Fe
    Fe = np.log10(rarr['mass_Fe'] / rarr['mass'] / 0.75 / 56.0) - 7.55 + 12.0
#    idx = np.argsort(Fe)
    rarr['mass_Fe'] = Fe
    arr = np.sort(rarr, order = 'mass_Fe')
    Fe = arr['mass_Fe']

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    r = np.sqrt(x * x + y * y + z * z)
    id1 = (arr['type'] == mp.TYPE_WARM)
    id2 = (r < 50.0)
        
    id3 = np.logical_and(id1, id2)

    idw = np.where(id3)
#   print idw

#   idw = np.where(arr['type'] == mp.TYPE_WARM)
    idc = np.where(arr['type'] == mp.TYPE_COLD)
    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.title(title_name)
    #plt.figure(figsize = (sz, sz))
    plt.xlabel('X [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.Normalize()
    plt.scatter(x[idw], z[idw], s = 1, c = Fe[idw], marker = 'o', \
        cmap = cmap, norm = norm, vmin = -4, vmax = 0, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.MultipleLocator(base = 1))
    cb.set_label('Iron abundance [Fe/H]')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'Fe-xz-' + dir_name + '-' + base_name + '-' \
        + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'Fe-xz-' + dir_name + '-' + base_name + '-' \
        + snap_num + '.png'
    plt.savefig(figure_name)

######################## X-Y #################################################
    print 'X - Y'
    
    plt.clf()
    #plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    
    cmap = mpl.cm.jet
    norm = mpl.colors.Normalize()
    plt.scatter(x[idw], y[idw], s = 1, c = Fe[idw], marker = 'o', \
        cmap = cmap, norm = norm, vmin = -4, vmax = 0, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.MultipleLocator(base = 1))
    cb.set_label('Iron abundance [Fe/H]')
    
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    
    figure_name = 'Fe-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#    plt.savefig(figure_name)
    
    figure_name = 'Fe-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)


############################## gen_slice_den ############################
def gen_slice_den(rarr, dir_name, base_name, snap_num, size, title_name = ''):

    arr = np.sort(rarr, order = 'den')

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    den = arr['den'][:]

#    r = np.sqrt(x * x + y * y + z * z)
    zabs = np.abs(z)
    id1 = (arr['type'] == mp.TYPE_WARM)
    id2 = (zabs < 0.01) # a thick of 0.2 kpc
        
    id3 = np.logical_and(id1, id2)

    idw = np.where(id3)
#   print idw

#   idw = np.where(arr['type'] == mp.TYPE_WARM)
#   idc = np.where(arr['type'] == mp.TYPE_COLD)
#   ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

######################## X-Y #################################################
    print 'X - Y'
    
    plt.clf()
    #plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    
    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idw], y[idw], s = 1, c = den[idw], marker = 'o', \
        cmap = cmap, norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')
    cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
    cb.set_label('Density [cm$^{-3}$]')
    
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    
    figure_name = 'Dslice-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#    plt.savefig(figure_name)
    
    figure_name = 'Dslice-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)


