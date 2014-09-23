#!/usr/bin/python

from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors, ticker, colorbar, mpl
from GAMER import *
import sys


def gen_den(file_base, snap_num, boxsize):

	file_in = file_base + '_' + snap_num
	file_out = file_in + '.png'

	file_temp = 'gtemp'
	cmd = 'GAMER_Uniform2D2gnuplot -i ' + file_in + ' -o ' + file_temp + ' -n 1'
	print cmd
	os.system(cmd)

	nlv = 6 # nlevel
	ninterval = pow(2, nlv - 1)

	array = loadtxt(file_temp, dtype = float, skiprows = 1)
	
	cmd = 'rm ' + file_temp
	os.system(cmd)

	size = len(array)
	size = sqrt(size)

	rho = array[:, 2]
	rho = rho.reshape(size, size).transpose()

	rho *= (DNORM / MJU * N_A)
	rho *= 1.0E-6 # convert to 1/cm^3

	# this lv is for color, different from nlv in GAMER

	rc('font', size = 17)
	width, height = rcParams['figure.figsize']
	size = min(width, height)

	cmap = mpl.cm.jet
	norm = mpl.colors.LogNorm()
	extent = (0, boxsize, 0, boxsize)

	loc = ticker.MultipleLocator(8)

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	im = plt.imshow(rho, extent = extent, cmap = cmap, norm = norm, 
		interpolation='none', vmin = 1.0E-6, vmax = 1.0E2)
	#ax = im.get_axes()
	ax.xaxis.set_major_locator(loc)
	ax.yaxis.set_major_locator(loc)
	cb = plt.colorbar(ticks = ticker.LogLocator(base = 10))
	cb.set_label('Density [cm$^{-3}$]')
	plt.xlim(0, boxsize)
	plt.ylim(0, boxsize)
	plt.savefig(file_out)

if len(sys.argv) < 5:

	print 'GAMER_den.py: not enough parameter!'
	print '\tUsage: GAMER_den.py file_base boxsize start end'
	print '\tExample: GAMER_den.py BaseXZslice_y32 64.0 0 100'
	sys.exit(0)

file_base	=	sys.argv[1]
boxsize		=	float(sys.argv[2])
start		=	int(sys.argv[3])
end			=	int(sys.argv[4])

for i in range(start, end + 1):

	snap_num = '%06d' % i
	
	print '##################### snap ', snap_num, '#######################'

	gen_den(file_base, snap_num, boxsize)
