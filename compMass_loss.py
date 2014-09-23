#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

rc('font', size = 15)

fig = plt.figure()
plt.yscale('log')
plt.xlabel('Time [Myr]')
#plt.ylabel('Mass [M$_\odot$]')
plt.ylabel('Mass loss [M$_\odot$]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.13)

prefix = '/home/liulei/program/mp-cd-sph/run'
file_in = prefix + '/' + 'PKlh-1' + '/mass_loss.dat'
array = np.loadtxt(file_in, dtype = float)
plt.plot(array[:, 0], array[:, 1], '-', color = 'k', \
        label = 'E$_\mathsf{SN}=$10$^\mathsf{51}$erg')

prefix = '/home/liulei/program/mp-cd-sph/run'
file_in = prefix + '/' + 'PKlh-50' + '/mass_loss.dat'
array = np.loadtxt(file_in, dtype = float)
plt.plot(array[:, 0], array[:, 1], '--', color = 'k', \
        label = 'E$_\mathsf{SN}=$10$^\mathsf{50}$erg')

plt.xlim(0, 1000.0)
plt.ylim(1.0e6, 1.0e10)

lg = plt.legend(loc = 4, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'comp-mass-loss' + '.eps'
plt.savefig(figure_name)


