#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

def IMF_Kroupa(m, A):

    mmin = 0.07999
    mmax = 100.0

    if m < mmin:
        return 0.0
    if m > mmax:
        return 0.0

    if (mmin <= m and m < 0.5):
        return A * np.power(2.0, 0.9) * np.power(m, -1.3)
    if (0.5 <= m and m < 1.0):
        return A * np.power(m, -2.2)
    if(1.0 <= m):
        return A * np.power(m, -2.7)

    return 0.0;

def N_Kroupa(ml, mu, A):

    mmin = 0.08
    mmax = 100.0

    if(ml < mmin):
        ml = mmin
    if(mu > mmax):
        mu = mmax

    if(ml > mu):
        return 0.0

    if(ml <= 0.5 and mu <= 0.5):
        tmp = -1.3 + 1.0
        tmp = np.power(2.0, 0.9) * A / tmp * (np.power(mu, tmp) - np.power(ml, tmp))

    if(ml <= 0.5 and mu > 0.5 and mu <= 1.0):
        tmp1 = -1.3 + 1.0
        tmp1 = np.power(2.0, 0.9) * A / tmp1 * (np.power(0.5, tmp1) - np.power(ml, tmp1))

        tmp2 = -2.2 + 1.0
        tmp2 = A / tmp2 * (np.power(mu, tmp2) - np.power(0.5, tmp2))
        
        tmp = tmp1 + tmp2

    if(ml <= 0.5 and mu > 1.0):
        tmp1 = -1.3 + 1.0
        tmp1 = np.power(2.0, 0.9) * A / tmp1 * (np.power(0.5, tmp1) - np.power(ml, tmp1))

        tmp2 = -2.2 + 1.0
        tmp2 = A / tmp2 * (np.power(1.0, tmp2) - np.power(0.5, tmp2))

        tmp3 = -2.7 + 1.0
        tmp3 = A / tmp3 * (np.power(mu, tmp3) - np.power(1.0, tmp3))

        tmp = tmp1 + tmp2 + tmp3

    if(ml > 0.5 and ml <= 1.0 and mu > 0.5 and mu <= 1.0):
        tmp = -2.2 + 1.0
        tmp = A / tmp * (np.power(mu, tmp) - np.power(ml, tmp))

    if(ml > 0.5 and ml <= 1.0 and mu > 1.0):
        tmp1 = -2.2 + 1.0
        tmp1 = A / tmp1 * (np.power(1.0, tmp1) - np.power(ml, tmp1))

        tmp2 = -2.7 + 1.0
        tmp2 = A / tmp2 * (np.power(mu, tmp2) - np.power(1.0, tmp2))

        tmp = tmp1 + tmp2

    if(ml > 1.0 and mu > 1.0):
        tmp = -2.7 + 1.0 
        tmp = A / tmp * (np.power(mu, tmp) - np.power(ml, tmp))

    return tmp

def M_Kroupa(ml, mu, A):

    mmin = 0.08
    mmax = 100.0

    if(ml < mmin):
        ml = mmin
    if(mu > mmax):
        mu = mmax

    if(ml > mu):
        return 0.0

    if(ml <= 0.5 and mu <= 0.5):
        tmp = -1.3 + 2.0
        tmp = np.power(2.0, 0.9) * A / tmp * (np.power(mu, tmp) - np.power(ml, tmp))

    if(ml <= 0.5 and mu > 0.5 and mu <= 1.0):
        tmp1 = -1.3 + 2.0
        tmp1 = np.power(2.0, 0.9) * A / tmp1 * (np.power(0.5, tmp1) - np.power(ml, tmp1))

        tmp2 = -2.2 + 2.0
        tmp2 = A / tmp2 * (np.power(mu, tmp2) - np.power(0.5, tmp2))
        
        tmp = tmp1 + tmp2

    if(ml <= 0.5 and mu > 1.0):
        tmp1 = -1.3 + 2.0
        tmp1 = np.power(2.0, 0.9) * A / tmp1 * (np.power(0.5, tmp1) - np.power(ml, tmp1))

        tmp2 = -2.2 + 2.0
        tmp2 = A / tmp2 * (np.power(1.0, tmp2) - np.power(0.5, tmp2))

        tmp3 = -2.7 + 2.0
        tmp3 = A / tmp3 * (np.power(mu, tmp3) - np.power(1.0, tmp3))

        tmp = tmp1 + tmp2 + tmp3

    if(ml > 0.5 and ml <= 1.0 and mu > 0.5 and mu <= 1.0):
        tmp = -2.2 + 2.0
        tmp = A / tmp * (np.power(mu, tmp) - np.power(ml, tmp))

    if(ml > 0.5 and ml <= 1.0 and mu > 1.0):
        tmp1 = -2.2 + 2.0
        tmp1 = A / tmp1 * (np.power(1.0, tmp1) - np.power(ml, tmp1))

        tmp2 = -2.7 + 2.0
        tmp2 = A / tmp2 * (np.power(mu, tmp2) - np.power(1.0, tmp2))

        tmp = tmp1 + tmp2

    if(ml > 1.0 and mu > 1.0):
        tmp = -2.7 + 2.0 
        tmp = A / tmp * (np.power(mu, tmp) - np.power(ml, tmp))

    return tmp


rc('font', size = 16)

mlow = 0.08
mup = 100.0

m = np.arange(log10(mlow), log10(mup), 0.01)
m = np.power(10.0, m)

A = 1.0 / M_Kroupa(mlow, mup, 1.0)
print 'A = ', A

mave = M_Kroupa(0.8, 8.0, 1.0) / N_Kroupa(0.8, 8.0, 1.0)
print 'Average mass between 0.8 and 8.0:', mave

ntot = N_Kroupa(mlow, mup, A)
print 'total star per Msol:', ntot

nSNII = N_Kroupa(8.0, 100.0, A)
print 'total SNII per Msol:', nSNII

nmid = N_Kroupa(0.8, 8.0, A)
print 'total number between 0.8 and 8.0 Msol:', nmid

ncumu = np.zeros(len(m))
for i in range(0, len(m)):
    mu = m[i]
    ncumu[i] = N_Kroupa(mlow, mu, A) / ntot

plt.figure()

plt.xscale('log')
#plt.yscale('log')

plt.xlabel('Stellar mass [M$_\odot$]')
plt.ylabel('Cumulative number fraction')


plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(m, ncumu)

plt.xlim(mlow, mup)
plt.ylim(0.0, 1.0)

#plt.legend()

plt.savefig('cumu_N_Kroupa.eps')

################################# Cumulative mass ######################
plt.clf()
mtot = M_Kroupa(mlow, mup, A)

mcumu = np.zeros(len(m))
for i in range(0, len(m)):
    mu = m[i]
    mcumu[i] = M_Kroupa(mlow, mu, A) / mtot

plt.figure()

plt.xscale('log')
#plt.yscale('log')

plt.xlabel('Stellar mass [M$_\odot$]')
plt.ylabel('Cumulative mass fraction')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(m, mcumu)

plt.xlim(mlow, mup)
plt.ylim(0.0, 1.0)

#plt.legend()

plt.savefig('cumu_M_Kroupa.eps')

################################# IMF ######################
plt.clf()

pp = np.zeros(len(m))
A = 1.0 / IMF_Kroupa(0.08, 1.0)

for i in range(0, len(m)):
    mu = m[i]
    pp[i] = IMF_Kroupa(mu, A)

plt.figure()

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Stellar mass [M$_\odot$]')
plt.ylabel('Relative probability')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(m, pp)

plt.xlim(mlow, mup)
#plt.ylim(1.0E-5, 1.0)

#plt.legend()

plt.savefig('IMF_Kroupa.eps')


