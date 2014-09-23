#!/usr/bin/python

from numpy import *
import numpy as np
import mp
import mp_snap
from matplotlib import *
from matplotlib import colors, ticker, colorbar, mpl
import matplotlib.pyplot as plt
from math import *
import sys

################### gen_snap_den ####################################

def gen_snap_den(rarr, dir_name, base_name, snap_num, size, title_name = ''):

    arr = np.sort(rarr, order = 'den')

    dmin = 1.0E-3
    dmax = 1.0E2

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    den = arr['den'][:]

    r = np.sqrt(x * x + y * y + z * z)
    id1 = (arr['type'] == mp.TYPE_WARM)
    id2 = (r < 150.0)
        
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
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idw], z[idw], s = 1, c = den[idw], marker = 'o', \
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
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    
    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idw], y[idw], s = 1, c = den[idw], marker = 'o', \
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
    plt.xlabel('Y [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)
    
    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(y[idw], z[idw], s = 1, c = den[idw], marker = 'o', \
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

    vmin = 1.0E4
    vmax = 2.0E7

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
    plt.xlabel('X [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idc], z[idc], s = 2, c = mass[idc], marker = 'o', \
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
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(x[idc], y[idc], s = 2, c = mass[idc], marker = 'o', \
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
    plt.xlabel('Y [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()
    plt.scatter(y[idc], z[idc], s = 2, c = mass[idc], marker = 'o', \
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


################### gen_snap_dm_star ####################################

def gen_snap_star_dm(rarr, dir_name, base_name, snap_num, size, \
    title_name = ''):

    arr = np.sort(rarr, order = 'mass')
#   arr = rarr

    x = arr['pos'][:, 0]
    y = arr['pos'][:, 1]
    z = arr['pos'][:, 2]

    mass = arr['mass'][:]

    idw = np.where(arr['type'] == mp.TYPE_WARM)
    idc = np.where(arr['type'] == mp.TYPE_COLD)
    ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)
    idm = np.where(arr['type'] == mp.TYPE_DM_PARAL)

#   if np.size(idc) == 0:
#       return
    
    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()

    if(np.size(idm) > 0):
        plt.scatter(x[idm], z[idm], s = 1, c = 'k', marker = 'o', \
            edgecolors = 'none')
    if(np.size(ids) > 0):
        plt.scatter(x[ids], z[ids], s = 1, c = 'r', marker = 'o', \
            edgecolors = 'none')
    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'DM-STAR-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'DM-STAR-xz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)


######################## X-Y #################################################

    plt.clf()
    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()

    if(np.size(idm) > 0):
        plt.scatter(x[idm], y[idm], s = 1, c = 'k', marker = 'o', \
            edgecolors = 'none')

    if(np.size(ids) > 0):
        plt.scatter(x[ids], y[ids], s = 2, c = 'r', marker = 'o', \
            edgecolors = 'none')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'DM-STAR-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'DM-STAR-xy-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.png'
    plt.savefig(figure_name)

########################### Y - Z ###################################
    plt.clf()

    rc('font', size = 17)
    width, height = rcParams['figure.figsize']
    sz = min(width, height)

    plt.figure(figsize = (sz, sz))
    plt.title(title_name)
    plt.xlabel('Y [kpc]')
    plt.ylabel('Z [kpc]')
    plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

    cmap = mpl.cm.jet
    norm = mpl.colors.LogNorm()

    if(np.size(idm) > 0):
        plt.scatter(y[idm], z[idm], s = 1, c = 'k', marker = 'o', \
            edgecolors = 'none')
    if(np.size(ids) > 0):
        plt.scatter(y[ids], z[ids], s = 2, c = 'r', marker = 'o', \
            edgecolors = 'none')
    plt.xlim(-size, size)
    plt.ylim(-size, size)

    figure_name = 'DM-STAR-yz-' + dir_name + '-' + base_name + '-' \
                    + snap_num + '.eps'
#   plt.savefig(figure_name)

    figure_name = 'DM-STAR-yz-' + dir_name + '-' + base_name + '-' \
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


