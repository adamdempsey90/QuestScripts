# Replace the netid's in the first file
# with the names in the second file
#
# Author: Adam Dempsey

import sys

with open(sys.argv[2],'r') as g:
    glines = g.readlines()

with open(sys.argv[1],'r+') as f:
    qf = f.read()
    for line in glines:
        netid,name = line.strip().split('\t')
        netid = netid.strip(':')
        name = name.split()[0]
        qf = qf.replace(netid,name)
    f.seek(0)
    f.write(qf)

