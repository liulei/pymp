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

def multi_den(dir_name, base_name, nproc, size):

	ntot, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, \
		'0020', nproc)

	rc('font', size = 15)
	fig = plt.figure()
	fig.set_figwidth(9)
	fig.set_figheight(8)
	fig.subplots_adjust(left = 0.10, right = 0.88, top = 0.95, bottom = 0.07, \
						wspace = 0.0, hspace = 0.0)
	plt.figtext(0.5, 0.97, 'Multi density', ha = 'center', size = 'large')
	

	majorLocator = ticker.MultipleLocator(10)
	minorLocator = ticker.MultipleLocator(5)

	nullFormatter = ticker.NullFormatter()

################### DEN 1 ####################################

	ax = fig.add_subplot(221)

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
	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idw], z[idw], s = 1, c = den[idw], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)

	ax.xaxis.set_major_formatter(nullFormatter)

#	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
#	cb.set_label('Density [cm$^{-3}$]')

	plt.xlim(-size, size * 0.99)
	plt.ylim(-size, size)

################### DEN 2 ####################################

	ax = fig.add_subplot(222)

#	arr = np.sort(rarr, order = 'den')

	x = arr['pos'][:, 0]
	y = arr['pos'][:, 1]
	z = arr['pos'][:, 2]

	den = arr['den'][:]

	idw = np.where(arr['type'] == mp.TYPE_WARM)
	idc = np.where(arr['type'] == mp.TYPE_COLD)
	ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

#	plt.xlabel('X [kpc]')
#	plt.ylabel('Z [kpc]')
	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idw], z[idw], s = 1, c = den[idw], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)

	ax.xaxis.set_major_formatter(nullFormatter)
	ax.yaxis.set_major_formatter(nullFormatter)

#	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
#	cb.set_label('Density [cm$^{-3}$]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)

################### DEN 3 ####################################

	ax = fig.add_subplot(223)

#	arr = np.sort(rarr, order = 'den')

	x = arr['pos'][:, 0]
	y = arr['pos'][:, 1]
	z = arr['pos'][:, 2]

	den = arr['den'][:]

	idw = np.where(arr['type'] == mp.TYPE_WARM)
	idc = np.where(arr['type'] == mp.TYPE_COLD)
	ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)


	width, height = rcParams['figure.figsize']
	sz = min(width, height)

	plt.xlabel('X [kpc]')
	plt.ylabel('Z [kpc]')
	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idw], z[idw], s = 1, c = den[idw], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)

#	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
#	cb.set_label('Density [cm$^{-3}$]')

	plt.xlim(-size, size * 0.99)
	plt.ylim(-size, size)


################### DEN 4 ####################################

	ax = fig.add_subplot(224)

#	arr = np.sort(rarr, order = 'den')

	x = arr['pos'][:, 0]
	y = arr['pos'][:, 1]
	z = arr['pos'][:, 2]

	den = arr['den'][:]

	idw = np.where(arr['type'] == mp.TYPE_WARM)
	idc = np.where(arr['type'] == mp.TYPE_COLD)
	ids = np.where(arr['type'] == mp.TYPE_STAR_PARAL)

	plt.xlabel('X [kpc]')
#	plt.ylabel('Z [kpc]')
	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	mapable = plt.scatter(x[idw], z[idw], s = 1, c = den[idw], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)

	ax.yaxis.set_major_formatter(nullFormatter)

	plt.xlim(-size, size)
	plt.ylim(-size, size)
	
#	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))

	cbaxes = fig.add_axes([0.89, 0.07, 0.02, 0.88])
	cb = plt.colorbar(orientation='vertical', \
		ticks = ticker.LogLocator(base = 10.0), cax = cbaxes)
	cb.set_label('Density [cm$^{-3}$]')

########################## save ######################################

	figure_name = 'MultiDen-xz-' + dir_name + '.png'
	plt.savefig(figure_name)

########################### main function ############################

if len(sys.argv) < 5:
	print 'genPanelp.py: not enough parameter!'
	print '\tUsage: genPanelp.py dir_name base_name nproc range'
	print '\tExample: genPanelp.py hd-1 1E3 1 20.0'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
size = float(sys.argv[4])

multi_den(dir_name, base_name, nproc, size)
