#!/usr/bin/python

from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import colors, ticker, colorbar
import sys

if len(sys.argv) < 3:

	print 'contour: not enough parameter!'
	print '\tUsage: ./contour.py file_in File_out'
	sys.exit(0)

file_in = sys.argv[1]
file_out = sys.argv[2]

print file_in

size = 64.0
N = 128

x = arange(0, size, size / N)
y = arange(0, size, size / N)
x += size * 0.5 / N
y += size * 0.5 / N

X, Y = meshgrid(x, y)

array = loadtxt(file_in)

lv = arange(-2.0, 3.1, 0.05)
lv = power(10.0, lv)

plt.figure()
plt.subplot(1, 1, 1)
ct = plt.contourf(X, Y, array, lv, norm = colors.LogNorm())
cb = plt.colorbar(ticks = ticker.LogLocator(), format = '%.0e')
cb.set_label('Density')
plt.xlim(0, size)
plt.ylim(0, size)
plt.show()
#plt.savefig(file_out)
