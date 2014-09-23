#!/usr/bin/python

import mp
import mp_snap
import sys
import os

if len(sys.argv) < 5:
	print 'genMc: not enough parameter!'
	print '\tUsage: genMc.py dir_name range start end'
	print '\tExample: genMc.py PKh-1 10.0 10 10'
	sys.exit(1)

dir_name = sys.argv[1]
size = float(sys.argv[2])
start = int(sys.argv[3])
end = int(sys.argv[4])

for i in range(start, end + 1):

	snap_num = '%04d' % i

	print '##################### snap ', snap_num, ' ######################'

	ntot = 0
	ntot, rarr = mp.read_dump(mp.prefix, dir_name, snap_num)

#	title = 't = %04d Myr' % (i * 100)

	mp_snap.gen_snap_cold_mass(rarr, dir_name, snap_num, size)

	print ' '

######################### end of main function ###########################


