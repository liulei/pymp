#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 3:
	print 'tOFe: not enough parameter!'
	print '\tUsage: ./tOFe.py dir_name time'
	print '\tExample: ./tOFe.py MW-hd-2 3000'
	sys.exit(0)

dir_name = sys.argv[1]
file_in = prefix + '/' + dir_name + '/out/mass.dat'

rc('font', size = 16)

array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time'] * TNORM / Myr

Z0 = 5.0E-4
lZ_Fe_sol = np.log10(Z0 / 0.02) - 0.8
lZ_O_sol = np.log10(Z0 / 0.02)

frac_O = 8.9 - 12.0 + lZ_O_sol
frac_O = 16.0 * np.power(10.0, frac_O)

frac_Fe = 7.55 - 12.0 + lZ_Fe_sol
frac_Fe = 56.0 * np.power(10.0, frac_Fe)

# now can only do like this:
Z = array[:]['mass_Z']

Z[:, ID_O, 0] += frac_O * Z[:, ID_H, 0]
Z[:, ID_O, 1] += frac_O * Z[:, ID_H, 1]
Z[:, ID_O, 2] += frac_O * Z[:, ID_H, 2]

Z[:, ID_Fe, 0] += frac_Fe * Z[:, ID_H, 0]
Z[:, ID_Fe, 1] += frac_Fe * Z[:, ID_H, 1]
Z[:, ID_Fe, 2] += frac_Fe * Z[:, ID_H, 2]

O_warm = np.log10(Z[:, ID_O, 0] / Z[:, ID_H, 0] / 16.0) - 8.9 + 12.0
O_cold = np.log10(Z[:, ID_O, 1] / Z[:, ID_H, 1] / 16.0) - 8.9 + 12.0
O_star = np.log10(Z[:, ID_O, 2] / Z[:, ID_H, 2] / 16.0) - 8.9 + 12.0

Fe_warm = np.log10(Z[:, ID_Fe, 0] / Z[:, ID_H, 0] / 56.0) - 7.55 + 12.0
Fe_cold = np.log10(Z[:, ID_Fe, 1] / Z[:, ID_H, 1] / 56.0) - 7.55 + 12.0
Fe_star = np.log10(Z[:, ID_Fe, 2] / Z[:, ID_H, 2] / 56.0) - 7.55 + 12.0

N_warm = np.log10(Z[:, ID_N, 0] / Z[:, ID_H, 0] / 14.0) - 7.86 + 12.0
N_cold = np.log10(Z[:, ID_N, 1] / Z[:, ID_H, 1] / 14.0) - 7.86 + 12.0
N_star = np.log10(Z[:, ID_N, 2] / Z[:, ID_H, 2] / 14.0) - 7.86 + 12.0

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
#fig.set_figwidth(6)
#fig.set_figheight(4)
fig.subplots_adjust(left = 0.15, right = 0.95, top = 0.97, bottom = 0.10, \
    hspace = 0.25)

############################# [O/Fe] ~ [Fe/H] ##########################

ax = plt.subplot(111)

plt.xlabel('[Fe/H]')
plt.ylabel('[O/Fe]')

ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 0.5))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

istart = 0

plt.plot(Fe_warm[istart:iend], OFe_warm[istart:iend], 'r-', hold = True)
plt.plot(Fe_cold[istart:iend], OFe_cold[istart:iend], 'g-', hold = True)
plt.plot(Fe_star[istart:iend], OFe_star[istart:iend], 'b-', hold = True)

plt.xlim(-4.0, 0.0)
plt.ylim(-0.5, 1.0)

############################# [N/O] ~ [O/H] ##########################
"""
ax = plt.subplot(212)

plt.xlabel('[O/H]')
plt.ylabel('[N/O]')

ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base = 1.0))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

plt.plot(O_warm[istart:iend], NO_warm[istart:iend], 'r-', hold = True)
plt.plot(O_cold[istart:iend], NO_cold[istart:iend], 'g-', hold = True)
plt.plot(O_star[istart:iend], NO_star[istart:iend], 'b-', hold = True)

plt.xlim(-5.0, 0.0)
plt.ylim(-2.5, 1.5)
"""

figure_name = 'OFe-' + sys.argv[1] + '.png'
if len(sys.argv) == 4:
	figure_name = 'OFe_NO-' + sys.argv[1] + '-' + sys.argv[3] + 'kpc.png'

plt.savefig(figure_name)



