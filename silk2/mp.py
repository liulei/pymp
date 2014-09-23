
import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
from math import *
import sys
import os

TYPE_WARM = 0
TYPE_COLD = 1
TYPE_DM_SINGLE = 2
TYPE_DM_PARAL = 3
TYPE_STAR_SINGLE = 3
TYPE_STAR_PARAL = 2

ID_H    =   0
ID_He   =   1
ID_Z    =   2
ID_C    =   3
ID_N    =   4
ID_O    =   5
ID_Ne   =   6
ID_Mg   =   7
ID_Si   =   8
ID_S    =   9
ID_Ca   =   10
ID_Fe   =   11

TM_TIME     =   0
TM_ALL      =   1
TM_DIVISION =   2
TM_EXCH_PARTICLES   =   3
TM_SETUP_TREE       =   4
TM_MORTON_SORT      =   5
TM_CALC_CM          =   6
TM_EXCH_TREE        =   7
TM_INSERT_CM        =   8
TM_CALC_GRAV        =   9
TM_CREATE_LIST_MP   =   10
TM_EXCH_MP          =   11
TM_NB_LOCAL         =   12
TM_NB_GLOBAL        =   13
TM_SPH              =   14
TM_COOLING          =   15
TM_CE               =   16
TM_COAGULATION      =   17
TM_FRAGMENTATION    =   18
TM_FB               =   19
TM_SF               =   20
TM_HD               =   21
TM_OTHER            =   -1

Pi      =   3.141592654
G       =   6.6704E-11          # (m/s^2) * (m^2/kg)
R_gas   =   8.31447251          # J/(K*mol)
k_gas   =   1.380650424E-23     # J/K
N_A     =   6.022141510E+23     # 1/mol
mu      =   1.6605388628E-27    # kg
mp      =   1.67262163783E-27   # kg
me      =   9.1093821545E-31    # kg
Msol    =   1.98892E+30         # kg
Rsol    =   6.960E+08           # m
Lsol    =   3.839E+26           # J/s
AU      =   1.49597870691E+11   # m
pc      =   3.085677581305E+16  # m
kpc     =   (1.0E+03*pc)        # m
km      =   1.0E+03             # km   -> m
cm3     =   1.0E-06             # cm^3 -> m^3
Year    =   3.1556926E+07       # s
Myr     =   (1.0E+06*Year)      # s
Gyr     =   (1.0E+09*Year)      # s

NH_sol  =   7.86    # Solar Nitrogen abundance

GAMMA   =   1.66666666667
MJU     =   1.3E-03         # kg/mol

KB      =   1024
MB      =   (KB*KB)

MNORM = 1.0E10 # in solar mass
RNORM = 1.0 # in kpc

MNORM   *=  Msol;
RNORM   *= kpc;

VNORM = sqrt(G * MNORM / RNORM)
TNORM = RNORM / VNORM;
DNORM = MNORM / (RNORM * RNORM * RNORM)
ENORM = MNORM * VNORM * VNORM
UNORM = VNORM * VNORM
DUNORM = UNORM / TNORM
ANORM = VNORM / TNORM
PRESSNORM = DNORM * UNORM

prefix = '/home/liulei/program/mp-cd-sph/run'

struct_contr = np.dtype([('time', float), \
                        ('dt', float), \
                        ('ekin', float), \
                        ('ethe', float), \
                        ('epot', float), \
                        ('epot_ext', float), \
                        ('etot', float), \
                        ('detot', float), \
                        ('rcm', float), \
                        ('vcm', float), \
                        ('momx', float), \
                        ('momy', float), \
                        ('momz', float)])

struct_mass = np.dtype([('time', float), \
                ('n', int), \
                ('n_warm', int), \
                ('n_cold', int), \
                ('n_star', int), \
                ('m_tot', float), \
                ('m_warm', float), \
                ('m_cold', float), \
                ('m_star', float), \
                ('mass_Z', float, (20, 3)), \
                ('dummy', float, 7)])

struct_mass_paral = np.dtype([('time', float), \
                ('n', int), \
                ('n_warm', int), \
                ('n_cold', int), \
                ('n_star', int), \
                ('n_dm', int), \
                ('m_tot', float), \
                ('m_warm', float), \
                ('m_cold', float), \
                ('m_star', float), \
                ('m_dm', float), \
                ('mass_Z', float, (20, 3)), \
                ('dummy', float, 7)])


struct_mp_paral = np.dtype([('index', int), \
                ('mass', float), \
                ('pos', float, 3), \
                ('vel', float, 3), \
                ('T', float), \
                ('mass_Z', float, 20), \
                ('m0', float), \
                ('t_beg_sf', float), \
                ('type', int), \
                ('type_sat', int)])

struct_dump_paral = np.dtype([('index', int), \
                ('type', float), \
                ('mass', float), \
                ('rad', float), \
                ('v', float), \
                ('c_s', float), \
                ('T', float), \
                ('u', float), \
                ('h', float), \
                ('den', float), \
                ('t_c', float), \
                ('t_v', float), \
                ('t_u', float), \
                ('ek', float), \
                ('ep', float), \
                ('ep_ext', float), \
                ('pos', float, 3), \
                ('vel', float, 3), \
                ('pres', float), \
                ('t_cool', float), \
                ('t_ff', float), \
                ('L_J', float), \
                ('M_J', float)])

struct_snap_paral = np.dtype([('type', float), \
                ('mass', float), \
                ('mass_O', float), \
                ('mass_Fe', float), \
                ('T', float), \
                ('den', float), \
                ('pos', float, 3)])


struct_mp_single = np.dtype([('index', int), \
                ('mass', float), \
                ('pos', float, 3), \
                ('vel', float, 3), \
                ('c', float), \
                ('mass_Z', float, 20), \
                ('m0', float), \
                ('t_beg_sf', float), \
                ('type', int), \
                ('type_sat', int)])

struct_m_trans = np.dtype([('time', float), \
                ('evap', float), \
                ('cond', float), \
                ('sn2', float), \
                ('pn', float), \
                ('sn1', float), \
                ('sw', float), \
                ('c2w', float), \
                ('hd', float), \
                ('sf', float)])

struct_e_trans = np.dtype([('time', float), \
                ('sn2', float), \
                ('pn', float), \
                ('sn1', float), \
                ('mech', float), \
                ('uv', float), \
                ('coll', float), \
                ('cooling', float), \
                ('visc', float), \
                ('drag', float)])

struct_e_trans_new = np.dtype([('time', float), \
                ('sn2', float), \
                ('pn', float), \
                ('sn1', float), \
                ('mech', float), \
                ('uv', float), \
                ('coll', float), \
                ('cooling', float), \
                ('visc', float), \
                ('drag', float), \
                ('evap_u', float), \
                ('evap_k', float)])

struct_wc = np.dtype([('time', float), \
                ('ek_w', float), \
                ('eu_w', float), \
                ('ep_w', float), \
                ('epe_w', float), \
                ('ek_c', float), \
                ('eu_c', float), \
                ('ep_c', float), \
                ('epe_c', float)])

struct_timing = np.dtype([('time', float), \
                ('all', float), \
                ('division', float), \
                ('exch_particles', float), \
                ('setup_tree', float), \
                ('morton_sort', float), \
                ('calc_cm', float), \
                ('exch_tree', float), \
                ('insert_cm', float), \
                ('calc_grav', float), \
                ('create_list_mp', float), \
                ('exch_mp', float), \
                ('nb_local', float), \
                ('nb_global', float), \
                ('sph', float), \
                ('cooling', float), \
                ('ce', float), \
                ('coagulation', float), \
                ('fragmentation', float), \
                ('fb', float), \
                ('sf', float), \
                ('hd', float), \
                ('other', float)])

struct_tme = np.dtype([('time', float), \
                ('all', float), \
                ('bef_sph', float), \
                ('mid_sph', float), \
                ('aft_sph', float), \
                ('aft_coag', float), \
                ('aft_div_ng', float), \
                ('aft_fb', float)])

def read_paral(prefix, dir_name, base_name, snap_num, nproc):

# read file header, get total number, time, bounding box, if necessary
    
    file_name = prefix + '/' + dir_name + '/' + base_name + '_' + snap_num
#   if nproc > 1:
    file_name = file_name + 'MP' + str(nproc) + '-0'

    f = open(file_name, 'r')

    strlist = f.readline().split()
    step = int(strlist[0])
    time = float(strlist[1])

    strlist = f.readline().split()
    ntot = int(strlist[0])
    n = int(strlist[1])

    f.close()

# allocate space for array

    arr = np.zeros(ntot, dtype = struct_mp_paral)

# for every single file, read header again to get particle number in this 
# file, then use genfromtxt() load data to a temperatory array, assign 
# data from this array to global array
#   np.genfromtxt(fname, dtype = mp_paral, skip_header = head number)
    nread = 0
    for ifile in range(0, nproc):
        
        file_name = prefix + '/' + dir_name + '/' + base_name + '_' + snap_num
#       if nproc > 1:
        file_name = file_name + 'MP' + str(nproc) + '-' + str(ifile)

        print file_name
        
        f = open(file_name, 'r')
        strlist = f.readline().split()
        strlist = f.readline().split()
        n = int(strlist[1])
        f.close()

        atemp = np.loadtxt(file_name, dtype = struct_mp_paral, skiprows = 4)
        
        if n != len(atemp):
            print 'wrong file parameter!'
            sys.exit(1);
        
        arr[nread: nread + n] = atemp[0:n]
        nread += n

    return ntot, arr

def read_dump_paral(prefix, dir_name, base_name, snap_num, nproc):

# read file header, get total number, time, bounding box, if necessary
    
    file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
#   if nproc > 1:
    file_name = file_name + 'DUMP' + str(nproc) + '-0'

    f = open(file_name, 'r')

    strlist = f.readline().split()
    step = int(strlist[0])
    time = float(strlist[1])

    strlist = f.readline().split()
    ntot = int(strlist[0])
    n = int(strlist[1])

    f.close()

# allocate space for array

    arr = np.zeros(ntot, dtype = struct_dump_paral)

# for every single file, read header again to get particle number in this 
# file, then use genfromtxt() load data to a temperatory array, assign 
# data from this array to global array
#   np.genfromtxt(fname, dtype = mp_paral, skip_header = head number)
    nread = 0
    for ifile in range(0, nproc):
        
        file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
#       if nproc > 1:
        file_name = file_name + 'DUMP' + str(nproc) + '-' + str(ifile)

        print file_name
        
        f = open(file_name, 'r')
        strlist = f.readline().split()
        strlist = f.readline().split()
        n = int(strlist[1])
        f.close()

        atemp = np.loadtxt(file_name, dtype = struct_dump_paral, skiprows = 4)
        
        if n != len(atemp):
            print 'wrong file parameter!'
            sys.exit(1);
        
        arr[nread: nread + n] = atemp[0:n]
        nread += n

    return ntot, arr

def read_snap_paral(prefix, dir_name, base_name, snap_num, nproc):

# read file header, get total number, time, bounding box, if necessary
    
    file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
    print 'file name:', file_name
#   if nproc > 1:
    file_name = file_name + 'SNAP' + str(nproc) + '-0'

    f = open(file_name, 'r')

    strlist = f.readline().split()
    step = int(strlist[0])
    time = float(strlist[1])

    strlist = f.readline().split()
    ntot = int(strlist[0])
    n = int(strlist[1])

    f.close()

# allocate space for array

    arr = np.zeros(ntot, dtype = struct_snap_paral)

# for every single file, read header again to get particle number in this 
# file, then use genfromtxt() load data to a temperatory array, assign 
# data from this array to global array
#   np.genfromtxt(fname, dtype = struct_snap_paral, skip_header = head number)
    nread = 0
    for ifile in range(0, nproc):
        
        file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
#       if nproc > 1:
        file_name = file_name + 'SNAP' + str(nproc) + '-' + str(ifile)

        print file_name
        
        f = open(file_name, 'r')
        strlist = f.readline().split()
        strlist = f.readline().split()
        n = int(strlist[1])
        f.close()

        atemp = np.loadtxt(file_name, dtype = struct_snap_paral, skiprows = 4)
        
        if n != len(atemp):
            print 'wrong file parameter!'
            sys.exit(1);
        
        arr[nread: nread + n] = atemp[0:n]
        nread += n

    return ntot, time, arr



def read_single(prefix, dir_name, snap_num):

    file_name = prefix + '/' + dir_name + '/' + snap_num + '.dat'

    f = open(file_name, 'r')
    
    strlist = f.readline().split()
    step = int(strlist[0])
    print 'step:', step

    strlist = f.readline().split()
    ntot = int(strlist[0])
    n_warm = int(strlist[1])
    n_cold = int(strlist[2])
    n_dm = int(strlist[3])
    n_star = int(strlist[4])

    print 'total:', ntot, ', warm:', n_warm, ', cold:', n_cold, \
        ', dm:', n_dm, ', star:', n_star

    strlist = f.readline().split()
    time = float(strlist[0])
    print 'time:', time, 'Myr'

    f.close()

    arr = np.loadtxt(file_name, dtype = struct_mp_single, skiprows = 3)
        
    if ntot != len(arr):
        print 'wrong file parameter!'
        sys.exit(1);
        
    return ntot, arr

def read_dump(prefix, dir_name, snap_num):

# read file header, get total number, time, bounding box, if necessary
    
    file_name = prefix + '/' + dir_name + '/' + snap_num + '.dump'

    arr = np.loadtxt(file_name, dtype = struct_dump_paral)
    
    return len(arr), arr

def is_snap_paral_exist(prefix, dir_name, base_name, snap_num, nproc):

    file_name = prefix + '/' + dir_name + '/out/' + base_name + '_' + snap_num
    file_name = file_name + 'SNAP' + str(nproc) + '-0'
    return os.path.isfile(file_name)


