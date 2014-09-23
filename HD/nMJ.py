#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

def M_Jeans(n, T): # n in 1/cm^3, T in K, return mass in Msol
	
	den = n / cm3 / N_A * MJU
	c_s = np.sqrt(R_gas * T / MJU)
	L_J = c_s * np.sqrt(Pi / den / G)
	M_J = Pi / 6.0 * L_J * L_J * L_J * den
	return M_J / Msol

def Length_Jeans(n, T): # n in 1/cm^3, T in K, return mass in Msol
	
	den = n / cm3 / N_A * MJU
	c_s = sqrt(R_gas * T / MJU)
	L_J = c_s * np.sqrt(Pi / den / G)
#	M_J = Pi / 6.0 * L_J * L_J * L_J * den
	return L_J / kpc

def n_M(M): # M in Msol, return density in 1/cm^3

    h = 50.0 * np.sqrt(M / 1.0E6) * pc
    rho = M * Msol / (4.0 / 3.0 * Pi * h * h * h)
    n = rho * N_A / MJU 
    return n * 1.0E-6

T = 1000.0
n = arange(-1.0, 5.0, 0.01)
n = power(10.0, n)

rc('font', size = 15)

plt.figure()

plt.xlim(n[0], n[-1])

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Density [cm$^{-3}$]')
plt.ylabel('Jeans Mass [M$_\odot$]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(n, M_Jeans(n, 1.0E4), label = 'T = 10000 K')
plt.plot(n, M_Jeans(n, 1.0E3), label = 'T = 1000 K')
plt.plot(n, M_Jeans(n, 1.0E2), label = 'T = 100 K')

print 'For 91-3.cm1:'
arr = np.loadtxt('hd_91-3.dat', dtype = float)
plt.scatter(arr[:, 3], arr[:, 2], s = 1, c = 'k', edgecolors = 'none')
MJp = M_Jeans(arr[:, 3], arr[:, 5])
id = np.where(MJp > arr[:, 2])
M = arr[id, 2]
print np.size(M)
print 'total mass:', np.sum(arr[:, 2])
print 'total below Jeans mass:', np.sum(arr[id, 2])

id = np.where(arr[:, 3] > 1.0E4)
M = arr[id, 2]
print 'total mass with n > 1.0E4:', np.sum(M)
print 'total number:', np.size(M)

plt.legend()

#plt.show()
plt.savefig('n-MJ.png')

