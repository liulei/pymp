#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
from mp import *

# M_cl in Msol, n_hot in 1/cm^3, v_rel in km/s, output time scale in Myr
# M_hot in Msol, NGB_cold is the cold neighbour number sourounding hot
def time_scale_hot(C_drag, M_cl, n_hot, v_rel_in, M_hot, NGB_cold):

# mass radius relation: h_cl = 50 \sqrt{M_cl / 10^6 Msol} (pc)
    h_cl = 50.0 * sqrt(M_cl / 1.0E6) * pc
    print h_cl / pc

# for hot gas density, first convert to 1/m^3, then kg/m^3
    rho_hot = n_hot * 1.0E6 * MJU / N_A

# v_rel convert to m/s
    v_rel = v_rel_in * 1.0E3

    print v_rel_in

# divided by 50 neighbours
    F = 0.5 * C_drag * Pi * h_cl * h_cl * rho_hot * v_rel * v_rel / 50.0

    M_hot *= Msol
    a = F / M_hot * NGB_cold 

# time scale: v_rel / a
    t = v_rel / a / Myr

    return t

# M_cl in Msol, n_hot in 1/cm^3, v_rel in km/s, output time scale in Myr
def time_scale_cold(C_drag, M_cl, n_hot, v_rel_in):

# mass radius relation: h_cl = 50 \sqrt{M_cl / 10^6 Msol} (pc)
    h_cl = 50.0 * sqrt(M_cl / 1.0E6) * pc

# for hot gas density, first convert to 1/m^3, then kg/m^3
    rho_hot = n_hot * 1.0E6 * MJU / N_A

# v_rel convert to m/s
    v_rel = v_rel_in * 1.0E3

    F = 0.5 * C_drag * Pi * h_cl * h_cl * rho_hot * v_rel * v_rel

    M_cl *= Msol
    a = F / M_cl

# time scale: v_rel / a
    t = v_rel / a / Myr

    return t


rc('font', size = 16)

plt.figure()

plt.xlabel('Relative velocity [km/s]')
plt.ylabel('Drag force time scale [Myr]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.xscale('log')
plt.yscale('log')

# hot gas:
M_cl = 1.0E5 # in Msol
C_drag = 1.0
vel_min = 20.0
vel_max = 500.0
v_rel = np.arange(log10(vel_min), log10(vel_max), 0.1, dtype = float)
v_rel = np.power(10.0, v_rel)

M_hot = 2.0E3 # in Msol
n_hot = 0.1 # in 1/cm^3
NGB_cold = 100
t_hot = time_scale_hot(C_drag, M_cl, n_hot, v_rel, M_hot, NGB_cold)
plt.plot(v_rel, t_hot, '-', label = 'n_hot = 0.1/cm$^3$, M_hot = 2000 M$_\odot$ (initial)')

M_hot = 2.0E3 # in Msol
n_hot = 0.01 # in 1/cm^3
NGB_cold = 100
t_hot = time_scale_hot(C_drag, M_cl, n_hot, v_rel, M_hot, NGB_cold)
plt.plot(v_rel, t_hot, '-', label = 'n_hot = 0.01/cm$^3$, M_hot = 2000 M$_\odot$ (initial)')

M_hot = 1.0E2 # in Msol
n_hot = 0.001 # in 1/cm^3
NGB_cold = 100
t_hot = time_scale_hot(C_drag, M_cl, n_hot, v_rel, M_hot, NGB_cold)
plt.plot(v_rel, t_hot, '-', label = 'n_hot = 0.001/cm$^3$, M_hot = 100 M$_\odot$(small, FB created)')

#plt.xlim(10, 1000)
plt.ylim(1, 1E4)

lg = plt.legend(ncol = 1, prop = {'size': 14})
lg.get_frame().set_linewidth(0)

plt.savefig('drag_hot.eps')

############################ cold drag ###################################
plt.clf()

plt.xlabel('Relative velocity [km/s]')
plt.ylabel('Drag force time scale [Myr]')

plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.15)

plt.xscale('log')
plt.yscale('log')


t_cold = time_scale_cold(C_drag, M_cl, n_hot, v_rel)
plt.plot(v_rel, t_cold, label = 'n_hot = 0.01/cm$^3$, M_cold = $10^5$ M$_\odot$')

lg = plt.legend(ncol = 1)
lg.get_frame().set_linewidth(0)

plt.savefig('drag_cold.eps')


