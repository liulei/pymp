#!/usr/bin/python

# OFe_NO.py: plot [O/Fe] ~ [Fe/H] and [N/O] ~[O/H]

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'OFe_NO: not enough parameter!'
	print '\tUsage: ./OFe_NO.py file_name ending_time radius(optional)'
	print '\tExample: ./OFe_NO.py PKh-1 1000 1.0(optional)'
	sys.exit(0)

file_in = prefix + '/' + sys.argv[1] + '/mass.dat'
if len(sys.argv) == 4:
	file_in = prefix + '/' + sys.argv[1] + '/mass_%.1fkpc.dat' % \
		(float(sys.argv[3]))

rc('font', size = 16)

NH_sol = 7.86 # arXiv:0903.3406 [astro-ph]
OH_sol = 8.65 # Asplund (2005)
NO_sol = NH_sol - OH_sol

FeH_sol = 7.51 # McWilliam (1997)
OFe_sol = OH_sol - FeH_sol

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

# now can only do like this:
Z = array[:]['mass_Z']

O_warm = np.log10(Z[:, ID_O, 0] / Z[:, ID_H, 0] / 16.0) + 12.0
O_cold = np.log10(Z[:, ID_O, 1] / Z[:, ID_H, 1] / 16.0) + 12.0
O_star = np.log10(Z[:, ID_O, 2] / Z[:, ID_H, 2] / 16.0) + 12.0

N_warm = np.log10(Z[:, ID_N, 0] / Z[:, ID_H, 0] / 14.0) + 12.0
N_cold = np.log10(Z[:, ID_N, 1] / Z[:, ID_H, 1] / 14.0) + 12.0
N_star = np.log10(Z[:, ID_N, 2] / Z[:, ID_H, 2] / 14.0) + 12.0

Fe_warm = np.log10(Z[:, ID_Fe, 0] / Z[:, ID_H, 0] / 56.0) + 12.0
Fe_cold = np.log10(Z[:, ID_Fe, 1] / Z[:, ID_H, 1] / 56.0) + 12.0
Fe_star = np.log10(Z[:, ID_Fe, 2] / Z[:, ID_H, 2] / 56.0) + 12.0

OFe_warm = O_warm - Fe_warm
OFe_cold = O_cold - Fe_cold
OFe_star = O_star - Fe_star

NO_warm = N_warm - O_warm
NO_cold = N_cold - O_cold
NO_star = N_star - O_star

end_time = float(sys.argv[2])
iend = int(end_time)
if(len(Fe_warm) < iend):
    iend = len(Fe_warm)
iend -= 1

################################### figure #############################

fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(7)
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.97, bottom = 0.10, \
    hspace = 0.25)

lw = 2
############################# [O/Fe] ~ [Fe/H] ##########################
# using [Fe/H] instead of 12+log(Fe/H)
ax = plt.subplot(211)

plt.xlabel('[Fe/H]')
plt.ylabel('[O/Fe]')

ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

istart = 10

plt.plot(Fe_warm[istart:iend] - FeH_sol, OFe_warm[istart:iend] - OFe_sol, 'r-', hold = True)
plt.plot(Fe_cold[istart:iend] - FeH_sol, OFe_cold[istart:iend] - OFe_sol, 'g-', hold = True)
plt.plot(Fe_star[istart:iend] - FeH_sol, OFe_star[istart:iend] - OFe_sol, 'b-', hold = True)

# plot for PKlh-50:
arr = np.loadtxt('OFe_FeH_PKlh-50.dat', dtype = float)
#plt.plot(arr[:, 2] - FeH_sol, arr[:, 3] - OFe_sol, 'g--')
#plt.plot(arr[:, 4] - FeH_sol, arr[:, 5] - OFe_sol, 'b--')

# plot for single-1:
arr = np.loadtxt('OFe_FeH_single-1.dat', dtype = float)
plt.plot(arr[:, 0] - FeH_sol, arr[:, 1] - OFe_sol, color = 'r', linestyle = 'dotted', linewidth = lw)
plt.plot(arr[:, 4] - FeH_sol, arr[:, 5] - OFe_sol, color = 'b', linestyle = 'dotted', linewidth = lw)

plt.xlim(2.0 - FeH_sol, 8.0 - FeH_sol)
#plt.ylim(1.1 - OFe_sol, 3.2 - OFe_sol)
plt.ylim(0.0, 2.0)

############################# [N/O] ~ [O/H] ##########################

ax = plt.subplot(212)

plt.xlabel('12+log(O/H)')
plt.ylabel('log(N/O)')

ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 1.0))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

plt.plot(O_warm[istart:iend], NO_warm[istart:iend], 'r-', hold = True)
plt.plot(O_cold[istart:iend], NO_cold[istart:iend], 'g-', hold = True)
plt.plot(O_star[istart:iend], NO_star[istart:iend], 'b-', hold = True)

# plot for PKlh-50:
arr = np.loadtxt('NO_OH_PKlh-50.dat', dtype = float)
#plt.plot(arr[:, 0], arr[:, 1], 'r--')
plt.plot(arr[:, 2], arr[:, 3], 'g--')
plt.plot(arr[:, 4], arr[:, 5], 'b--')

# plot for single-1:
arr = np.loadtxt('NO_OH_single-1.dat', dtype = float)
plt.plot(arr[:, 0], arr[:, 1], color = 'r', linestyle = 'dotted', linewidth = lw)
plt.plot(arr[:, 4], arr[:, 5], color = 'b', linestyle = 'dotted', linewidth = lw)

ms = 6.0
# van Zee:
if True:
    obs = np.loadtxt('Obs/vanZee1997a_NO_All.dat', dtype = float)
    obs_NO = obs[:, 0] - obs[:, 2]
#    print obs_NO
    obs_OH = obs[:, 2]
    plt.plot(obs_OH, obs_NO, 'kx', ms = ms, mew = 2)
 
if True:
    obs = np.loadtxt('Obs/Israelian2004.txt', dtype = float)
    obs_NO = obs[:, 2] - obs[:, 3] + NO_sol
    obs_OH = obs[:, 3] + OH_sol
    plt.plot(obs_OH, obs_NO, 'sm', ms = ms, mew = 0)

if True:
    obs = np.loadtxt('Obs/Spite2005.txt', dtype = float)
    obs_NO = obs[:, 0] - obs[:, 1] + NO_sol
    obs_OH = obs[:, 1] + OH_sol
    plt.plot(obs_OH, obs_NO, '*c', ms = ms, mew = 0)

plt.plot(OH_sol, NO_sol, 'ok', ms = ms+2, mew = 2, fillstyle = 'none')

plt.xlim(4.0, 9.0)
plt.ylim(-2.5, 0.0)

figure_name = 'OFe_NO-' + sys.argv[1] + '.eps'
if len(sys.argv) == 4:
	figure_name = 'OFe_NO-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.eps'

plt.savefig(figure_name)

