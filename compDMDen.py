#!/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os
import mp

# rho0 in Msol/pc^3, r0 in kpc, r in kpc, return rho in Msol/pc^3
def den_Burkert(rho0, r0, r):
    
    r02 = r0 * r0
    r03 = r02 * r0
    rho = rho0 * r03 / (r + r0) / (r * r + r02)
    return rho

############################## mass density ##############################

dir_name = 'SS-relax-2'
    
rc('font', size = 15)
plt.clf()
plt.title('Dark matter density evolution')
plt.xlabel('Radius [kpc]')
plt.ylabel('Dark matter mass density [M$_\odot$/pc$^\mathsf{3}$]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.90, bottom = 0.15)

arr = np.loadtxt('r-rho-0000.dat', dtype = float)
plt.plot(arr[:, 0], arr[:, 1], 'r-', label = 't = 0')

arr = np.loadtxt('r-rho-0005.dat', dtype = float)
plt.plot(arr[:, 0], arr[:, 1], 'g-', label = 't = 0.5 Gyr')

arr = np.loadtxt('r-rho-0010.dat', dtype = float)
plt.plot(arr[:, 0], arr[:, 1], 'b-', label = 't = 1.0 Gyr')

arr = np.loadtxt('r-rho-0020.dat', dtype = float)
plt.plot(arr[:, 0], arr[:, 1], 'c-', label = 't = 2.0 Gyr')

arr = np.loadtxt('r-rho-0030.dat', dtype = float)
plt.plot(arr[:, 0], arr[:, 1], 'm-', label = 't = 3.0 Gyr')

rho = den_Burkert(0.045, 1.0, arr[:, 0])
plt.plot(arr[:, 0], rho, 'k-', label = 'Burkert (1995)')

plt.xlim(0.1, 10.0)
plt.ylim(1.0E-5, 1.0E-1)
#plt.ylim(0.0, 0.05)
plt.xscale('log')
plt.yscale('log')

lg = plt.legend(loc = 0, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

figure_name = 'Comp-DM-r-rho-' + dir_name + '.eps'
plt.savefig(figure_name)
