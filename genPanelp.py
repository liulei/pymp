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


	rc('font', size = 15)
	fig = plt.figure()
	fig.set_figwidth(10)
	fig.set_figheight(8.05)
	fig.subplots_adjust(left = 0.08, right = 0.96, top = 0.95, bottom = 0.06)
	plt.figtext(0.5, 0.97, title_name, ha = 'center', size = 'large')

	majorLocator = ticker.MultipleLocator(10)
	minorLocator = ticker.MultipleLocator(5)

################### snap_den ####################################

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

	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Density [cm$^{-3}$]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)


######################## gen_snap_T ####################################
	ax = fig.add_subplot(222)
	ax.apply_aspect()

	pos = ax.get_position().get_points()
	x4 = pos[0][0]
	width = pos[1][0] - pos[0][0]
	height = pos[1][1] - pos[0][1]

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

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)


	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Temperature [K]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)

################### gen_snap_cold_mass ####################################
	
	ax = fig.add_subplot(223)
	ax.apply_aspect()
	pos = ax.get_position().get_points()
	y4 = pos[0][1]

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

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)


	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Cold Cloud Mass [M$_\odot$]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)

################### dm_star ####################################

	ax = fig.add_subplot(224, aspect = 'equal')
	ax.set_anchor('W')
#	ax = fig.add_axes([x4, y4, width, height])

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

	plt.scatter(x[idm], z[idm], s = 1, c = 'k', marker = 'o', \
		edgecolors = 'none')
	if(np.size(ids) > 0):
		plt.scatter(x[ids], z[ids], s = 2, c = 'r', marker = 'o', \
			edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)

	plt.xlim(-size, size)
	plt.ylim(-size, size)

########################## save ######################################

	print 'writing xz...'
	figure_name = 'Panel-xz-' + dir_name + '-' + base_name + '-' \
					+ snap_num + '.png'
	plt.savefig(figure_name)

######################################################################
################################## X Y ###############################
######################################################################

	plt.clf()

	fig = plt.figure()
	fig.set_figwidth(10)
	fig.set_figheight(8.05)
	fig.subplots_adjust(left = 0.08, right = 0.96, top = 0.95, bottom = 0.06)
	plt.figtext(0.5, 0.97, title_name, ha = 'center', size = 'large')

################### snap_den ####################################

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
	plt.ylabel('Y [kpc]')
	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idw], y[idw], s = 1, c = den[idw], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e-7, vmax = 10, edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)

	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Density [cm$^{-3}$]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)


######################## gen_snap_T ####################################
	ax = fig.add_subplot(222)
	ax.apply_aspect()

	pos = ax.get_position().get_points()
	x4 = pos[0][0]
	width = pos[1][0] - pos[0][0]
	height = pos[1][1] - pos[0][1]

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
	plt.scatter(x[idw], y[idw], s = 1, c = T[idw], marker = 'o', cmap = cmap, \
		norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)


	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Temperature [K]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)

################### gen_snap_cold_mass ####################################
	
	ax = fig.add_subplot(223)
	ax.apply_aspect()
	pos = ax.get_position().get_points()
	y4 = pos[0][1]

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
	plt.ylabel('Y [kpc]')
#	plt.subplots_adjust(left = 0.13, right = 0.93, top = 0.93, bottom = 0.13)

	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	plt.scatter(x[idc], y[idc], s = 2, c = mass[idc], marker = 'o', \
		cmap = cmap, norm = norm, vmin = 1e3, vmax = 1e7, edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)


	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10.0))
	cb.set_label('Cold Cloud Mass [M$_\odot$]')

	plt.xlim(-size, size)
	plt.ylim(-size, size)

################### dm_star ####################################

	ax = fig.add_subplot(224, aspect = 'equal')
	ax.set_anchor('W')
#	ax = fig.add_axes([x4, y4, width, height])

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

	plt.scatter(x[idm], y[idm], s = 1, c = 'k', marker = 'o', \
		edgecolors = 'none')
	if(np.size(ids) > 0):
		plt.scatter(x[ids], y[ids], s = 2, c = 'r', marker = 'o', \
			edgecolors = 'none')

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_minor_locator(minorLocator)
	ax.yaxis.set_major_locator(majorLocator)
	ax.yaxis.set_minor_locator(minorLocator)

	plt.xlim(-size, size)
	plt.ylim(-size, size)

########################## save ######################################

	figure_name = 'Panel-xy-' + dir_name + '-' + base_name + '-' \
					+ snap_num + '.png'
	plt.savefig(figure_name)




if len(sys.argv) < 7:
	print 'genPanelp.py: not enough parameter!'
	print '\tUsage: genPanelp.py dir_name base_name nproc range start end'
	print '\tExample: genPanelp.py hd-1 1E3 1 20.0 0 100'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
size = float(sys.argv[4])
start = int(sys.argv[5])
end = int(sys.argv[6])

for i in range(start, end + 1):

	snap_num = '%04d' % i

	print '####################### snap ', snap_num, '######################'
	title = 't = %04d Myr' % (i * 10)

	ntot, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, \
		snap_num, nproc)

	gen_snap_all(rarr, dir_name, base_name, snap_num, size, title_name = title)
	
	print ' '


