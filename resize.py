#!/usr/bin/python

from numpy import *
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
import os

def resize_single(prefix, cut_time, file_num):
    
    file_target = '%s_%d.dat' % (prefix, file_num)
    print file_target
    file_bak = '%s.bak' % file_target
    cmd = 'mv %s %s' % (file_target, file_bak)
    os.system(cmd)
    fin = open(file_bak, 'r')
    fout = open(file_target, 'w')
    for line in fin:
        strlist = line.split()
        time = float(strlist[1])
        if(time <= cut_time * 1.000001):
            fout.write('%s' % line)

    fin.close()
    fout.close()

prefix = 'record_fb'
nprocs = 16
cut_time = 1.0E3

for i in range(0, nprocs):
    resize_single(prefix, cut_time, i)
