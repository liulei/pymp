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

def M_Jeans(n, T): # n in 1/cm^3, T in K, return mass in Msol
	
	den = n / cm3 / N_A * MJU / DNORM
	c_s = sqrt(R_gas * T / MJU) / VNORM
	L_J = c_s * np.sqrt(Pi / den)
	M_J = Pi / 6.0 * L_J * L_J * L_J * den
	return M_J * MNORM / Msol

def Length_Jeans(n, T): # n in 1/cm^3, T in K, return mass in Msol
	
	den = n / cm3 / N_A * MJU / DNORM
	c_s = sqrt(R_gas * T / MJU) / VNORM
	L_J = c_s * np.sqrt(Pi / den)
#	M_J = Pi / 6.0 * L_J * L_J * L_J * den
	return L_J * RNORM / kpc

def n_M(M): # M in Msol, return density in 1/cm^3

    h = 50.0 * np.sqrt(M / 1.0E6) * pc
    rho = M * Msol / (4.0 / 3.0 * Pi * h * h * h)
    n = rho * N_A / MJU 
    return n * 1.0E-6

# n in 1/cm^3, return time in Myr
def calc_dyn(n): 
    rho = n / cm3 / N_A * MJU
#    t = np.sqrt(3.0 * Pi / (32.0 * G * rho))
    t = np.sqrt(1.0 / (G * rho))
    return t / Myr

# n in 1/cm^3, L in standard, T in K, return time in Myr
def calc_cool(T, L, n):
    n_SI = n / cm3 # convert to 1/m^3
    rho = n / cm3 / N_A * MJU
    u = R_gas * T / (GAMMA - 1.0) / MJU
    rate = L * n_SI * n_SI / rho
    t = u / rate
    return t / Myr

Xi = 1.0E-4
# Z = 2E-4
# cooling at 1000K, including molecular cooling:
L1 = 3.503316E-27 * Xi + 6.266656E-31 + 1.271003E-30 + 6.918628E-32
print 'Lambda at Z = 2.0E-4, T = 1000 K, Xi = 1E-4:', L1
# convert to SI unit:
L1 *= 1.0E-13

Xi = 1.0E-2
# Z = 2E-4
# cooling at 1000K, including molecular cooling:
L2 = 3.503316E-27 * Xi + 6.266656E-31 + 1.271003E-30 + 6.918628E-32
# convert to SI unit:
L2 *= 1.0E-13

Xi = 1.0E-2
# Z = 2E-3
# cooling at 1000K, including molecular cooling:
L3 = 3.503316E-26 * Xi + 6.266656E-30 + 1.271003E-30 + 6.918628E-32
# convert to SI unit:
L3 *= 1.0E-13

# n in 1/cm^3, rho in kg/m^3 
n = arange(-1.0, 4.0, 0.01)
n = power(10.0, n)

t_dyn = calc_dyn(n)
t_cool1 = calc_cool(1000.0, L1, n)
t_cool2 = calc_cool(1000.0, L2, n)
t_cool3 = calc_cool(1000.0, L3, n)

rc('font', size = 15)

plt.figure()

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Density [cm$^{-3}$]')
plt.ylabel('Time scale [Myr]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(n, t_dyn, label = 'Dynamical time')
plt.plot(n, t_cool1, label = 'Cooling time (T = 1000 K, Z = 0.0002, Xi = 0.0001)')
plt.plot(n, t_cool2, label = 'Cooling time (T = 1000 K, Z = 0.0002, Xi = 0.01)')
plt.plot(n, t_cool3, label = 'Cooling time (T = 1000 K, Z = 0.002, Xi = 0.01)')

plt.xlim(n[0], n[-1])

lg = plt.legend(prop = {'size': 12})
lg.get_frame().set_linewidth(0)

#plt.show()
plt.savefig('time_scale.png')

