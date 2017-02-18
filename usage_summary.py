#!/usr/bin/env python

##################################################
#  Print the total CPU hours used on each        #
#  account found in the users history.           #
#                                                #
#  Before running this script the user           #
#  should run the mam-list-usagrecords commad    #
#                                                #
#  mam-list-usagerecords -u username > usage.txt #
#  python usage_summary usage.txt                #
#                                                #
#  Dependencies: NumPy, Pandas                   #
#  Author: Adam M. Dempsey, 2017                 #
##################################################


import pandas as pd
import numpy as np
import sys

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'usage.txt'


print('Reading usage summary in {}'.format(fname))

with open(fname,'r') as f:
    lines = f.readlines()[2:]

dat = pd.read_fwf('usage.txt')

acc = dat['Account'][1:]
procs = dat['Processors'][1:]

myaccs = np.unique(acc)

acc = np.array(acc)

dt = pd.to_datetime(dat['EndTime'][1:]) - pd.to_datetime(dat['StartTime'][1:])

ds = np.array([x.total_seconds()/(3600.) for x in dt])

acc = np.array([ x for i,x in enumerate(acc) if ~np.isnan(ds[i])])
procs = np.array([ x for i,x in enumerate(procs) if ~np.isnan(ds[i])]).astype(int)
ds = np.array(filter(lambda x: ~np.isnan(x),ds))

ds *= procs

print('Account: CPU Hours')
print('-------------------')
for a in myaccs:
    inds = np.argwhere(acc == a)
    tot = (ds[inds]).sum()
    print('{}:\t{:.1e}'.format(a,tot))




