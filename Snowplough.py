#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

# E51 in units of 10^51 erg, n0 in 1/cm^3, t in year, return Rs in pc
def Rs(E51, n0, t):
    return 1.13 * np.power(E51, 115./511.) * np.power(n0, -135./511.) * \
        np.power(t, 2./7.)

# E51 in units of 10^51 erg, n0 in 1/cm^3, t in year, return Ts in K
def Ts(E51, n0, t):
    return 2.82E8 * np.power(E51, 134./511.) * np.power(n0, -24./511.) * \
        np.power(t, -4./7.)

# E51 in units of 10^51 erg, n0 in 1/cm^3, t in year, return Vs in km/s
def Vs(E51, n0, t):

    ksi = 1.0
    t_PDS = 3.61E4 / 2.718 * np.power(E51, 3./14.) / np.power(ksi, 5./14.) / \
            np.power(n0, 4./7.)
    t_star = t / t_PDS
    return 413. * np.power(n0, 1./7.) * np.power(ksi, 3./4.) * \
        np.power(E51, 1./14.) * np.power(4./3. * t_star - 1./3., -7./10.)

Mtot = 5.0E7 # in Msol
bsize = 100.0 # in pc
n0 = Mtot * Msol / np.power(bsize * pc, 3)
n0 = n0 / MJU * N_A * 1.0E-6 # switch to 1/cm^3
print 'Mtot (Msol):', Mtot
print 'bsize (pc):', bsize
print 'n0 (1/cm^3):', n0

nbin = 100
t_beg = 1.0E2
t_end = 1.0E5
t = np.arange(0, nbin, dtype = float) / nbin
t = np.power(10.0, (log10(t_end) - log10(t_beg)) * t) * t_beg

############################## Rs #######################################
rc('font', size = 15)

plt.clf()

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.xlabel('Time [kyr]')
plt.ylabel('Radius [pc]')

plt.xscale('log')
#plt.yscale('log')

value = Rs(1.0, 1.0E1, t)
plt.plot(t / 1E3, value, 'm-', label = 'E51 = 1.0, n0 = 1E1/cm$^3$')

value = Rs(1.0, 1.0E3, t)
plt.plot(t / 1E3, value, 'r-', label = 'E51 = 1.0, n0 = 1E3/cm$^3$')

value = Rs(1.0, 1.0E5, t)
plt.plot(t / 1E3, value, 'c-', label = 'E51 = 1.0, n0 = 1E5/cm$^3$')

plt.xlim(t_beg / 1E3, t_end / 1E3)
#plt.ylim(1, 1E4)

lg = plt.legend(loc = 2, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

plt.savefig('Rs_t.eps')
plt.savefig('Rs_t.png')

############################## Ts #######################################
rc('font', size = 15)

plt.clf()

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.xlabel('Time [kyr]')
plt.ylabel('Temperature [K]')

plt.xscale('log')
plt.yscale('log')

value = Ts(1.0, 1.0E1, t)
plt.plot(t / 1E3, value, 'm-', label = 'E51 = 1.0, n0 = 1E1/cm$^3$')

value = Ts(1.0, 1.0E3, t)
plt.plot(t / 1E3, value, 'r-', label = 'E51 = 1.0, n0 = 1E3/cm$^3$')

value = Ts(1.0, 1.0E5, t)
plt.plot(t / 1E3, value, 'c-', label = 'E51 = 1.0, n0 = 1E5/cm$^3$')

plt.xlim(t_beg / 1E3, t_end / 1E3)
#plt.ylim(1, 1E4)

lg = plt.legend(prop = {'size': 15})
lg.get_frame().set_linewidth(0)

plt.savefig('Ts_t.eps')
plt.savefig('Ts_t.png')

############################## Vs #######################################
rc('font', size = 15)

plt.clf()

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.xlabel('Time [kyr]')
plt.ylabel('Velocity [km/s]')

plt.xscale('log')
plt.yscale('log')

value = Vs(1.0, 1.0E1, t)
plt.plot(t / 1E3, value, 'm-', label = 'E51 = 1.0, n0 = 1E1/cm$^3$')

value = Vs(1.0, 1.0E3, t)
plt.plot(t / 1E3, value, 'r-', label = 'E51 = 1.0, n0 = 1E3/cm$^3$')

value = Vs(1.0, 1.0E5, t)
plt.plot(t / 1E3, value, 'c-', label = 'E51 = 1.0, n0 = 1E5/cm$^3$')

plt.xlim(t_beg / 1E3, t_end / 1E3)
#plt.ylim(1, 1E4)

lg = plt.legend(loc = 1, prop = {'size': 15})
lg.get_frame().set_linewidth(0)

plt.savefig('Vs_t.eps')
plt.savefig('Vs_t.png')


