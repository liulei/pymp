#!/usr/bin/python

import mp
import mp_snap
import sys

if len(sys.argv) < 6:
	print 'Dsortp: not enough parameter!'
	print '\tUsage: Dsortp.py dir_name base_name snap_num nproc range'
	print '\tExample: Dsortp.py hd-1 1E3 0001 1 20.0'
	sys.exit(1)

dir_name = sys.argv[1]
base_name = sys.argv[2]
snap_num = sys.argv[3]
nproc = int(sys.argv[4])
size = float(sys.argv[5])

ntot = 0
ntot, rarr = mp.read_dump_paral(mp.prefix, dir_name, base_name, snap_num, nproc)

mp_snap.gen_snap_den(rarr, dir_name, base_name, snap_num, size)


