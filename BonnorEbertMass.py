#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

#n = 1.0 # 1/cm^3
#u = R_gas * T / (GAMMA - 1.0) / MJU
#c_s = sqrt((GAMMA - 1.0) * u)

def M_BE(M, T): # M in Msol, T in k, return Bonnor-Ebert mass in Msol

    h = 50.0 * np.sqrt(M / 1.0E6) * pc
    rho = M * Msol / (4.0 / 3.0 * Pi * h * h * h)
    
    sigma = sqrt(R_gas * T / MJU)
    sigma3 = pow(sigma, 3)
    G3 = pow(G, 3)

    MBE = 1.182 * sigma3 / np.sqrt(G3 * rho)

    return MBE / Msol
    

def M_Jeans(n, T): # n in 1/cm^3, T in K, return mass in Msol
	
	den = n / cm3 / N_A * MJU / DNORM
	c_s = sqrt(R_gas * T / MJU) / VNORM
	L_J = c_s * np.sqrt(Pi / den)
	M_J = Pi / 6.0 * L_J * L_J * L_J * den
	return M_J * MNORM / Msol

def n_M(M): # M in Msol, return density in 1/cm^3

    h = 50.0 * np.sqrt(M / 1.0E6) * pc
    rho = M * Msol / (4.0 / 3.0 * Pi * h * h * h)
    n = rho * N_A / MJU 
    return n * 1.0E-6

rc('font', size = 16)

############################# M - MJ ##################################

plt.clf()

M = arange(0, 5, 0.01)
M = np.power(10.0, M)

plt.xlim(M[0], M[-1])
plt.ylim(1.0, 1.0E7)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Cloud mass [M$_\odot$]')
plt.ylabel('Jeans mass [M$_\odot$]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

n = n_M(M)
plt.plot(M, M_Jeans(n, 1.0E4), label = 'T = 10000 K')
plt.plot(M, M_Jeans(n, 1.0E3), label = 'T = 1000 K')
plt.plot(M, M_Jeans(n, 1.0E2), label = 'T = 100 K')
plt.plot(M, M_Jeans(n, 1.0E1), label = 'T = 10 K')

plt.legend()

plt.savefig('M-MJ.eps')

############################# M - Bonnor-Ebert ###############################

plt.clf()

plt.xlim(M[0], M[-1])
plt.ylim(1.0, 1.0E7)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Cloud mass [M$_\odot$]')
plt.ylabel('Bonnor-Ebert mass [M$_\odot$]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(M, M_BE(M, 1.0E4), label = 'T = 10000 K')
plt.plot(M, M_BE(M, 1.0E3), label = 'T = 1000 K')
plt.plot(M, M_BE(M, 1.0E2), label = 'T = 100 K')
plt.plot(M, M_BE(M, 1.0E1), label = 'T = 10 K')

plt.legend()

plt.savefig('M-MBE.eps')

################################## 


