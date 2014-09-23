#!/usr/bin/python

import mp
import mp_snap_mc
import sys
import os

if len(sys.argv) < 7:
    print 'gmcStarp: not enough parameter!'
    print '\tUsage: gmcStarp.py dir_name base_name nproc range start end'
    print '\tExample: gmcStarp.py MCT-1 dwarf 4 60.0 0 20'
    sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
nproc = int(sys.argv[3])
size = float(sys.argv[4])
start = int(sys.argv[5])
end = int(sys.argv[6])

#for i in range(start, end + 1):
i = start
while i <= end:

    snap_num = '%04d' % i

    print '##################### snap ', snap_num, ' ######################'
    if mp_snap_mc.is_mc_exist(mp.prefix, dir_name, base_name, \
            snap_num, nproc):

        ntot = 0
        ntot, time, rarr = mp_snap_mc.read_mc(mp.prefix, dir_name, base_name, \
                    snap_num, nproc)

        title = 't = %.2f Myr' % (time)

        mp_snap_mc.gen_snap_star(rarr, dir_name, base_name, snap_num, size, \
            title_name = title)

#        mp_snap.gen_snap_T(rarr, dir_name, base_name, snap_num, size, title_name = title)
#        mp_snap_mc.gen_snap_cold_mass(rarr, dir_name, base_name, snap_num, size, title_name = title)

#        print ' '

    i += 1

######################### end of main function ###########################


