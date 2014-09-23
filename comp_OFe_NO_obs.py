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

array = np.loadtxt(file_in, dtype = struct_mass)

time = array['time'] * TNORM / Myr

# now can only do like this:
Z = array[:]['mass_Z']

O_warm = np.log10(Z[:, ID_O, 0] / Z[:, ID_H, 0] / 16.0) + 12.0
O_cold = np.log10(Z[:, ID_O, 1] / Z[:, ID_H, 1] / 16.0) + 12.0
O_star = np.log10(Z[:, ID_O, 2] / Z[:, ID_H, 2] / 16.0) + 12.0

Fe_warm = np.log10(Z[:, ID_Fe, 0] / Z[:, ID_H, 0] / 56.0) + 12.0
Fe_cold = np.log10(Z[:, ID_Fe, 1] / Z[:, ID_H, 1] / 56.0) + 12.0
Fe_star = np.log10(Z[:, ID_Fe, 2] / Z[:, ID_H, 2] / 56.0) + 12.0

N_warm = np.log10(Z[:, ID_N, 0] / Z[:, ID_H, 0] / 14.0) + 12.0
N_cold = np.log10(Z[:, ID_N, 1] / Z[:, ID_H, 1] / 14.0) + 12.0
N_star = np.log10(Z[:, ID_N, 2] / Z[:, ID_H, 2] / 14.0) + 12.0

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

############################# [O/Fe] ~ [Fe/H] ##########################

ax = plt.subplot(211)

plt.xlabel('12+log[Fe/H]')
plt.ylabel('log[O/Fe]')

ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 1))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

istart = 10

plt.plot(Fe_warm[istart:iend], OFe_warm[istart:iend], 'r-', hold = True)
plt.plot(Fe_cold[istart:iend], OFe_cold[istart:iend], 'g-', hold = True)
plt.plot(Fe_star[istart:iend], OFe_star[istart:iend], 'b-', hold = True)

plt.xlim(2.0, 8.0)
plt.ylim(1.1, 3.2)

############################# [O/Fe] ~ [Fe/H] ##########################

ax = plt.subplot(212)

plt.xlabel('12+log[O/H]')
plt.ylabel('log[N/O]')

ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 1))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 1.0))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

plt.plot(O_warm[istart:iend], NO_warm[istart:iend], 'r-', hold = True)
plt.plot(O_cold[istart:iend], NO_cold[istart:iend], 'g-', hold = True)
plt.plot(O_star[istart:iend], NO_star[istart:iend], 'b-', hold = True)

# include observation results (van Zee 1997):
#if True:
if False:
    obs = np.loadtxt('vanZee1997a_NO_All.dat', dtype = float)
    obs_NO = obs[:, 0] - obs[:, 2]
#    print obs_NO
    obs_OH = obs[:, 2]
    plt.plot(obs_OH, obs_NO, 'k1')
    
plt.xlim(4.0, 9.0)
plt.ylim(-2.5, 0.0)

figure_name = 'OFe_NO-' + sys.argv[1] + '.eps'
if len(sys.argv) == 4:
	figure_name = 'OFe_NO-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.eps'

plt.savefig(figure_name)



