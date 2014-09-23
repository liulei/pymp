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

def gen_snap_all(rarr, dir_name, base_name, snap_num, size, title_name = ''):


#	rc('font', size = 17)
	fig = plt.figure()
	fig.set_figwidth(10)
	fig.set_figheight(8)

################### snap_den ####################################

	ax = plt.subplot(221)

	plt.tight_layout(w_pad = 4)

	arr = np.sort(rarr, order = 'den')

	x = arr['pos'][:, 0]
	y = arr['pos'][:, 1]
	z = arr['pos'][:, 2]

	den = arr['den'][:]

	idw = np.where(arr['type'] == mp.TYPE_WARM)
	idc = np.where(arr['type'] == mp.TYPE_COLD)
	ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)


	width, height = rcParams['figure.figsize']
	sz = min(width, height)

#	plt.xlabel('X [kpc]')
	plt.ylabel('Z [kpc]')
#	plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idw], z[idw], s = 1, c = den[idw], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')

	majorLocator = ticker.MultipleLocator(10)
	minorLocator = ticker.MultipleLocator(5)

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)

	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Density [cm$^{-3}$]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)


######################## gen_snap_T ####################################
	sp = plt.subplot(2, 2, 2)

	arr = np.sort(rarr, order = 'T')
	arr = arr[::-1]

	x = arr['pos'][:, 0]
	y = arr['pos'][:, 1]
	z = arr['pos'][:, 2]

	T = arr['T'][:]

	idw = np.where(arr['type'] == mp.TYPE_WARM)
	idc = np.where(arr['type'] == mp.TYPE_COLD)
	ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

#	plt.xlabel('X [kpc]')
#	plt.ylabel('Z [kpc]')

	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idw], z[idw], s = 1, c = T[idw], marker = 'o', cmap = cmap, \
		norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')
	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Temperature [K]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)

################### gen_snap_cold_mass ####################################
	
	plt.subplot(2, 2, 3)

	arr = np.sort(rarr, order = 'mass')
#	arr = rarr

	x = arr['pos'][:, 0]
	y = arr['pos'][:, 1]
	z = arr['pos'][:, 2]

	mass = arr['mass'][:]

	idw = np.where(arr['type'] == mp.TYPE_WARM)
	idc = np.where(arr['type'] == mp.TYPE_COLD)
	ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

	if np.size(idc) == 0:
		return
	
	plt.xlabel('X [kpc]')
	plt.ylabel('Z [kpc]')
#	plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idc], z[idc], s = 2, c = mass[idc], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')
	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Cold Cloud Mass [M$_\odot$]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)

################### dm_star ####################################

	plt.subplot(2, 2, 4)

	arr = np.sort(rarr, order = 'mass')

	x = arr['pos'][:, 0]
	y = arr['pos'][:, 1]
	z = arr['pos'][:, 2]

	mass = arr['mass'][:]

	idw = np.where(arr['type'] == mp.TYPE_WARM)
	idc = np.where(arr['type'] == mp.TYPE_COLD)
	ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)
	idm = np.where(arr['type'] == mp.TYPE_DM_PARAL)

#	if np.size(idc) == 0:
#		return

	plt.xlabel('X [kpc]')
#	plt.ylabel('Z [kpc]')
#	plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()

	plt.scatter(x[idm], z[idm], s = 1, c = 'k', marker = 'o', \
		edgecolors = 'none')
	if(np.size(ids) > 0):
		sp.scatter(x[ids], z[ids], s = 2, c = 'r', marker = 'o', \
			edgecolors = 'none')
	plt.xlim(-size, size)
	plt.ylim(-size, size)

########################## save ######################################

	figure_name = 'All-xz-' + dir_name + '-' + base_name + '-' \
					+ snap_num + '.png'
	plt.savefig(figure_name)



if len(sys.argv) < 6:
	print 'panelp.py: not enough parameter!'
	print '\tUsage: panelp.py dir_name base_name snap_num nproc range'
	print '\tExample: panelp.py hd-1 1E3 0001 1 20.0'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])
size = float(sys.argv[5])

ntot = 0
ntot, rarr = mp.read_dump_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

gen_snap_all(rarr, dir_name, base_name, snap_num, size, title_name = 'hd-1')


