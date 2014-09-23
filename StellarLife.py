#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

# Raiteri (1996):
# M in Msol, Z in absolute (Z_sol = 0.02), return life in Myr
def Life_Time(M, Z):

    if Z < 7.0E-5:
        Z = 7.0E-5
    if Z > 0.03:
        Z = 0.03

    logZ = np.log10(Z)
    logZ2 = logZ * logZ

    a0 = 10.130 + 0.07547 * logZ - 0.008084 * logZ2
    a1 = 4.4240 + 0.7939 * logZ + 0.1187 * logZ2
    a2 = 1.2620 + 0.3385 * logZ + 0.05417 * logZ2

    logM = np.log10(M)
    logM2 = logM * logM
    
    logt = a0 - a1 * logM + a2 * logM2
    t = np.power(10.0, logt)

    return t / 1.0E6

rc('font', size = 16)

############################# M - MJ ##################################

plt.clf()

M = arange(-1.0, 2.5, 0.01)
M = np.power(10.0, M)

plt.xlim(0.6, 120.0)
plt.ylim(1.0, 1.0E5)
#plt.xlim(0.6, 8.0)
#plt.ylim(1.0, 2.0E4)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Stellar mass [M$_\odot$]')
plt.ylabel('Life time [Myr]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.plot(M, Life_Time(M, 1.0E-2), label = 'Z = 0.01')
plt.plot(M, Life_Time(M, 1.0E-3), label = 'Z = 0.001')
plt.plot(M, Life_Time(M, 1.0E-4), label = 'Z = 0.0001')

plt.legend()

plt.savefig('LifeTime.eps')
