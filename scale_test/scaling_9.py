#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib import ticker
import sys
from mp import *
from math import *

rc('font', size = 17)

dirs = ['hdt-91.1', 'hdt-91.2', 'hdt-91.4', 'hdt-91.8', 'hdt-91.16']
nnode = len(dirs)
nodes = [1, 2, 4, 8, 16]
times = np.zeros(nnode, dtype = float)
speedup_pred = np.zeros(nnode)
times_pred = np.zeros(nnode)

for i in range(0, nnode):
    file_in = prefix + '/' + dirs[i] + '/benchmark.dat'
    array = np.loadtxt(file_in, dtype = float)
    times[i] = array[90:98, TM_ALL].sum()

base = times[0]
speedup = base / times

for i in range(0, nnode):
    times_pred[i] = base / power(2.0, i)
    speedup_pred[i] = power(2.0, i)

fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(6)
fig.subplots_adjust(left = 0.18, right = 0.95, top = 0.93, bottom = 0.10, \
    hspace = 0.0)
nullFormatter = ticker.NullFormatter()

label = '$2\\times 10^9 \mathsf{M}_\odot$, $100$ Myr'
plt.figtext(0.55, 0.95, label, ha = 'center')

############################# timing ###################################
ax = plt.subplot(211)

plt.xscale('log')
#plt.xlabel('Node number')
plt.yscale('log')
plt.ylabel('Timing [ms]')

ax.xaxis.set_major_locator(ticker.LogLocator(base = 2))
ax.xaxis.set_minor_locator(ticker.NullLocator())
ax.xaxis.set_major_formatter(ticker.NullFormatter())


plt.plot(nodes, times, 'ro-', hold = True, label = 'Real run')
plt.plot(nodes, times_pred, '-', hold = True, label = 'Theory')

plt.xlim(0.9, 17)
plt.ylim(2.0E3, 1.0E6)

############################# speedup ###################################
ax = plt.subplot(212)

plt.xscale('log')
plt.xlabel('Node number')
plt.yscale('log')
plt.ylabel('Speedup')

ax.xaxis.set_major_locator(ticker.LogLocator(base = 2))
ax.xaxis.set_minor_locator(ticker.NullLocator())
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

ax.yaxis.set_major_locator(ticker.LogLocator(base = 2))
ax.yaxis.set_minor_locator(ticker.NullLocator())
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%5d'))

plt.plot(nodes, speedup, 'ro-', hold = True, label = 'Real run')
plt.plot(nodes, speedup_pred, '-', hold = True, label = 'Theory')

plt.xlim(0.9, 17)
plt.ylim(0.9, 24)

lg = plt.legend(loc = 4, prop = {'size': 14})
lg.get_frame().set_linewidth(0)

figure_name = 'Scaling-9.eps'

plt.savefig(figure_name)


