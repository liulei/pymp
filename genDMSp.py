#!/usr/bin/python

import mp
import mp_snap
import sys
import os

if len(sys.argv) < 7:
    print 'genDMSp: not enough parameter!'
    print '\tUsage: genDMSp.py dir_name base_name nproc range start end'
    print '\tExample: genDMSp.py int-3 INT 8 25.0 0 20'
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

    ntot = 0
    ntot, time, rarr = mp.read_snap_paral(mp.prefix, dir_name, base_name, \
                    snap_num, nproc)
    title = 't = %4d Myr' % int(time + 0.1)
    mp_snap.gen_snap_star_dm(rarr, dir_name, base_name, snap_num, size, \
        title_name = title)

    print ' '
    i += 10

######################### end of main function ###########################


