#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import mp

Pi		=	3.141592654
G		=	6.6704E-11			# (m/s^2) * (m^2/kg)
R_gas	=	8.31447251			# J/(K*mol)
k_gas	=	1.380650424E-23		# J/K
N_A		=	6.022141510E+23  	# 1/mol
mu		=	1.6605388628E-27	# kg
mp		=	1.67262163783E-27 	# kg
me		=	9.1093821545E-31 	# kg
Msol	=	1.98892E+30			# kg
Rsol	=	6.960E+08			# m
AU		=	1.49597870691E+11	# m
pc		=	3.085677581305E+16	# m
kpc		=	(1.0E+03*pc)		# m
km		=	1.0E+03				# km   -> m
cm3		=	1.0E-06				# cm^3 -> m^3
Year	=	3.1556926E+07		# s
Myr		=	(1.0E+06*Year)		# s
Gyr		=	(1.0E+09*Year)		# s

GAMMA	=	1.66666666667
MJU		=	1.3E-03			# kg/mol

KB		=	1024
MB		=	(KB*KB)

MNORM = 1.0E10 # in solar mass
RNORM = 1.0 # in kpc

MNORM	*=	Msol;
RNORM	*= kpc;

VNORM = sqrt(G * MNORM / RNORM)
TNORM = RNORM / VNORM;
DNORM = MNORM / (RNORM * RNORM * RNORM)
ENORM = MNORM * VNORM * VNORM
UNORM = VNORM * VNORM
DUNORM = UNORM / TNORM
ANORM = VNORM / TNORM
PRESSNORM = DNORM * UNORM

print 'VNORM:', VNORM

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

def M_L(M): # M in Msol, return size in pc
    h = 50.0 * np.sqrt(M / 1.0E6)
    return h

T = 1000.0
n = arange(-2.0, 5.0, 0.01)
n = power(10.0, n)

rc('font', size = 16)

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
plt.plot(n, M_Jeans(n, 1.0E1), label = 'T = 10 K')

plt.legend()

#plt.show()
plt.savefig('n-MJ.eps')


plt.clf()
plt.xlim(n[0], n[-1])

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Density [cm$^{-3}$]')
plt.ylabel('Jeans Length [kpc]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(n, Length_Jeans(n, 1.0E4), label = 'T = 10000 K')
plt.plot(n, Length_Jeans(n, 1.0E3), label = 'T = 1000 K')
plt.plot(n, Length_Jeans(n, 1.0E2), label = 'T = 100 K')
plt.plot(n, Length_Jeans(n, 1.0E1), label = 'T = 10 K')

plt.legend()

plt.savefig('n-LJ.eps')

################################### M-n #################################
plt.clf()
M = arange(0, 8, 0.01)
M = power(10.0, M)

plt.xlim(M[0], M[-1])

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Mass [M$_\odot$]')
plt.ylabel('Number density [1/cm$^3$]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

n = n_M(M)
plt.plot(M, n)

plt.savefig('M-n.eps')

################################### M-n #################################
plt.clf()
M = arange(0, 8, 0.01)
M = power(10.0, M)

plt.xlim(M[0], M[-1])

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Mass [M$_\odot$]')
plt.ylabel('Cloud size [pc]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

L = M_L(M)
plt.plot(M, L)

plt.savefig('M-L.eps')

############################# M - MJ ##################################

plt.clf()
plt.xlim(M[0], M[-1])

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


