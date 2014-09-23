#!/export/home/liulei/local/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

if len(sys.argv) < 2:
    print 'mass.py: add radius (kpc) parameter for mass within fixed radius (optional)'
    print 'Example: ./mass.py 20.0'
    mass_name = 'mass.dat'
    figure_name = 'Mass-evolve.png'
else:
    mass_name = 'mass_%.1fkpc.dat' % float(sys.argv[1])
    figure_name = 'Mass-evolve-%.1fkpc.png' % float(sys.argv[1])


rc('font', size = 15)
fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(10)

fig.subplots_adjust(left = 0.17, right = 0.95, top = 0.95, bottom = 0.05, \
    hspace = 0.0)

time_end = 500.0

nullFormatter = ticker.NullFormatter()

#dir = ['81-hd-3lsig', '80-hd-3lsig', '91-hd-3.cm1', '90-hd-3.cm1', '101-hd-3', '100-hd-3']
dir = ['81-hd-3Hs3', '80-hd-3Hs3', '91-hd-3Hs1', '90-hd-3Hs1', '101-hd-3Hs1', '100-hd-3Hs1']
############################## 81 ################################
ax = fig.add_subplot(311)

plt.yscale('log')
plt.xlabel('Time [Myr]')
plt.ylabel('Mass [M$_\odot$]')

file_in = prefix + '/' + dir[0] + '/out/' + mass_name
array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time']
warm = array[:]['m_warm']
cold = array[:]['m_cold']
star = array[:]['m_star']

plt.plot(time, warm, 'r-', hold = True)
plt.plot(time, cold, 'g-', hold = True)
plt.plot(time, star, 'b-', hold = True)

######################## 80 ##############################
file_in = prefix + '/' + dir[1] + '/out/' + mass_name
array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time']
warm = array[:]['m_warm']
cold = array[:]['m_cold']
star = array[:]['m_star']

plt.plot(time, warm, 'r--', hold = True)
plt.plot(time, cold, 'g--', hold = True)
plt.plot(time, star, 'b--', hold = True)

ax.xaxis.set_major_formatter(nullFormatter)

plt.xlim(0, time_end)
plt.ylim(1.1e5, 1.0e9)

############################## 91 ################################
ax = fig.add_subplot(312)

plt.yscale('log')
plt.xlabel('Time [Myr]')
plt.ylabel('Mass [M$_\odot$]')

file_in = prefix + '/' + dir[2] + '/out/' + mass_name
array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time']
warm = array[:]['m_warm']
cold = array[:]['m_cold']
star = array[:]['m_star']

plt.plot(time, warm, 'r-', hold = True)
plt.plot(time, cold, 'g-', hold = True)
plt.plot(time, star, 'b-', hold = True)

######################## hdc-90 ##############################
file_in = prefix + '/' + dir[3] + '/out/' + mass_name
array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time']
warm = array[:]['m_warm']
cold = array[:]['m_cold']
star = array[:]['m_star']

plt.plot(time, warm, 'r--', hold = True)
plt.plot(time, cold, 'g--', hold = True)
plt.plot(time, star, 'b--', hold = True)

ax.xaxis.set_major_formatter(nullFormatter)

plt.xlim(0, time_end)
plt.ylim(1.1e6, 1.0e10)

############################## 101 ################################
ax = fig.add_subplot(313)

plt.yscale('log')
plt.xlabel('Time [Myr]')
plt.ylabel('Mass [M$_\odot$]')

file_in = prefix + '/' + dir[4] + '/out/' + mass_name
array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time']
warm = array[:]['m_warm']
cold = array[:]['m_cold']
star = array[:]['m_star']

plt.plot(time, warm, 'r-', hold = True)
plt.plot(time, cold, 'g-', hold = True)
plt.plot(time, star, 'b-', hold = True)

######################## 100 ##############################
file_in = prefix + '/' + dir[5] + '/out/' + mass_name
array = np.loadtxt(file_in, dtype = struct_mass_paral)

time = array['time']
warm = array[:]['m_warm']
cold = array[:]['m_cold']
star = array[:]['m_star']

plt.plot(time, warm, 'r--', hold = True)
plt.plot(time, cold, 'g--', hold = True)
plt.plot(time, star, 'b--', hold = True)

plt.xlim(0, time_end)
plt.ylim(1.0e7, 1.0e11)

######################## label #####################################
label = '$2\\times10^8 \mathsf{M}_\odot$'
plt.figtext(0.8, 0.91, label, ha = 'center', size = 'large')

label = '$2\\times10^9 \mathsf{M}_\odot$'
plt.figtext(0.8, 0.61, label, ha = 'center', size = 'large')

label = '$2\\times10^{10} \mathsf{M}_\odot$'
plt.figtext(0.8, 0.31, label, ha = 'center', size = 'large')

######################## legend ####################################
if len(sys.argv) < 2:
    lg = plt.legend(('Hot/warm', 'Cold', 'Star'), \
#        'Hot/warm, no rotation', 'Cold, no rotation', 'Star, no rotation'), \
            loc = 4)
    lg.get_frame().set_linewidth(0)

#figure_name = 'Mass-evolve.png'
plt.savefig(figure_name)


