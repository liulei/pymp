#!/usr/bin/python

import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from mp import *

rc('font', size = 17)

fig, ax = plt.subplots(1, 1)
fig.set_figwidth(6)
fig.set_figheight(4)

plt.xlabel('Year')
plt.ylabel('Gas particle resolution [M$_\odot$]')
plt.subplots_adjust(left = 0.15, right = 0.95, top = 0.95, bottom = 0.12)
plt.yscale('log')

subs = np.arange(9, dtype = float) + 1.0
ax.yaxis.set_major_locator(ticker.LogLocator(base = 10))
ax.yaxis.set_minor_locator(ticker.LogLocator(subs = subs))

ax.xaxis.set_major_locator(ticker.MultipleLocator(base = 5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(base = 1))

ms = 8
mew = lw = 2

plt.errorbar(1992, 1.6E7, marker = '1', color = 'b', \
        ms = ms, mew = mew, \
        label = 'Katz (1992)', ls = '')

plt.errorbar(1993, 5.568E7, marker = '2', color = 'g', \
        ms = ms, mew = mew, \
        label = 'Navarro & White (1993)', ls = '')

plt.errorbar(1995, 2E7, marker = '3', color = 'r', \
        ms = ms, mew = mew, \
        label = 'Stein & Mueller (1995)', ls = '')

plt.errorbar(1997, 2.5E5, marker = '4', color = 'c', \
        ms = ms, mew = mew, \
        label = 'Gerristsen & Icke (1997)', ls = '')

plt.errorbar(1999, 4.74E7, marker = '>', color = 'm', \
        ms = ms, markeredgecolor = 'none', \
        label = 'Berczik (1999)', ls = '')

plt.errorbar(2000, 2.5E6, yerr = [[0], [8.75E7]], marker = 's', color = 'y', \
        ms = ms, markeredgecolor = 'none', mew = mew, lw = lw, \
        label = 'Navarro & Steinmetz (2000)', ls = '')

plt.errorbar(2001, 1.2e7, marker = '*', color = 'b', \
        ms = ms, markeredgecolor = 'none', \
        label = 'Thacker & Couchman (2001)', ls = '')

plt.errorbar(2003, 3.57E6, yerr = [[3.56107E6], [0]], marker = 'p', color = 'g', \
        ms = ms, markeredgecolor = 'none', mew = mew, lw = lw, \
        label = 'Springel & Hernquist (2003)', ls = '')

plt.errorbar(2004, 1.285E6, marker = '+', color = 'r', \
        ms = ms, mew = mew, \
        label = 'Brook et al. (2004)', ls = '')

plt.errorbar(2006, 1E5, yerr = [[0], [4.9E6]], marker = 'h', color = 'c', \
        ms = ms, markeredgecolor = 'none', mew = mew, lw = lw, \
        label = 'Stinson et al. (2006)', ls = '')

plt.errorbar(2008, 350, yerr = [[0.], [3150.]], marker = 'H', color = 'm', \
        ms = ms, markeredgecolor = 'none', mew = mew, lw = lw, \
        label = 'Saitoh et al. (2008)', ls = '')

plt.errorbar(2011, 220, yerr = [[195.], [1480.]], marker = 'x', color = 'y', \
        ms = ms, mew = mew, lw = lw, \
        label = 'Hopkins et al. (2011)', ls = '')

plt.errorbar(2012, 2.5E4, yerr = [[2.19E4], [1.75E5]], marker = 'o', color = 'b', \
        ms = ms, markeredgecolor = 'none', mew = mew, lw = lw, \
        label = 'Brook et al. (2012)', ls = '')

plt.errorbar(2012, 3E3, marker = 's', color = 'r', \
        ms = ms, markeredgecolor = 'none', mew = mew, \
        label = 'Pontzen & Governato (2012)', ls = '')

plt.errorbar(2013, 312.5, marker = '^', color = 'g', \
        ms = ms, markeredgecolor = 'none', mew = mew,\
        label = 'Dobbs (2013)', ls = '')

plt.xlim(1990, 2015)
plt.ylim(6, 1E9)

handles, labels = ax.get_legend_handles_labels()
handles = [h[0] for h in handles]

lg = ax.legend(handles, labels, loc = 3, ncol = 2, numpoints = 1, prop = {'size': 6})
lg.get_frame().set_linewidth(0)

figure_name = 'Moore.eps'
plt.savefig(figure_name)
